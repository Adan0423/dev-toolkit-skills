"""Inventory skill archives; restore missing sources without overwriting existing ones.

Archived files are data: this utility never runs their scripts or instructions.
Requires PyYAML. Default is audit only; --extract-missing performs additive writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import zipfile
from collections import defaultdict
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAX_FILE = 128 * 1024 * 1024
MAX_ARCHIVE = 512 * 1024 * 1024
WINDOWS_RESERVED = re.compile(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\.|$)", re.I)


def decode(data):
    try:
        return data.decode("utf-8-sig"), "utf-8"
    except UnicodeDecodeError:
        return data.decode("cp1252"), "cp1252"


def frontmatter(data):
    text, encoding = decode(data)
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    error = None
    try:
        metadata = yaml.safe_load(match.group(1)) if match else {}
        if not isinstance(metadata, dict):
            metadata = {}
            error = "Frontmatter no es un mapa YAML"
    except yaml.YAMLError as exc:
        metadata = {}
        error = str(exc).splitlines()[0]
    name = metadata.get("name")
    if not name:
        fallback = re.search(r"^name:\s*([^\n]+)", text, re.M)
        name = fallback.group(1).strip().strip('\"\'') if fallback else None
    return metadata, name, text, encoding, error or (None if match else "Sin frontmatter")


def digest(files):
    value = hashlib.sha256()
    for name, data in sorted(files.items()):
        value.update(name.encode("utf-8") + b"\0" + hashlib.sha256(data).digest())
    return value.hexdigest()


def safe_name(name):
    if "\\" in name or "\0" in name or name.startswith("/"):
        raise ValueError(f"Ruta ZIP inválida: {name!r}")
    parts = PurePosixPath(name).parts
    if not parts or any(
        part in (".", "..") or ":" in part or part.endswith((".", " "))
        or WINDOWS_RESERVED.match(part) or any(c in part for c in '<>\"|?*')
        for part in parts
    ):
        raise ValueError(f"Ruta ZIP no segura en Windows: {name!r}")
    return "/".join(parts)


def load_archive(path):
    files = {}
    seen = set()
    with zipfile.ZipFile(path) as archive:
        if sum(info.file_size for info in archive.infolist()) > MAX_ARCHIVE:
            raise ValueError("Archivo expandido supera límite")
        for info in archive.infolist():
            safe = safe_name(info.filename.rstrip("/"))
            mode = info.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError("ZIP contiene enlace simbólico")
            if info.is_dir():
                continue
            if safe.casefold() in seen:
                raise ValueError(f"Entradas duplicadas: {safe}")
            seen.add(safe.casefold())
            if info.file_size > MAX_FILE:
                raise ValueError(f"Entrada supera límite: {safe}")
            files[safe] = archive.read(info)  # Also verifies CRC.
    return files


def category(name):
    if name.startswith(("marketing-", "meta-ads-", "google-ads-", "tiktok-ads-")):
        return "marketing"
    if name.startswith("android-") or name == "mobile-app-engineering":
        return "mobile"
    if name.startswith("windows-"):
        return "desktop"
    if name in {"pdf", "pptx", "xlsx", "word-document-tools"}:
        return "documents"
    if name in {"modern-software-architect", "software-project-architect", "scalable-database-architect"}:
        return "architecture"
    if name == "secure-software-auditor":
        return "security"
    if name in {"doc-coauthoring", "documentation-repository-curator", "project-readme-documentation", "humanizer", "internal-comms"}:
        return "docs"
    if name in {"mcp-builder", "llm-api-development"}:
        return "integrations"
    if name in {"webapp-testing"}:
        return "quality"
    if name in {"slack-gif-creator", "scrcpy-mobile-dev"}:
        return "automation"
    if name in {"tailwindcss-v4-3-expert"}:
        return "frontend"
    if name in {"adaptive-web-ui-stack-architect", "web-ui-ux-frontend-architect", "brand-guidelines", "canvas-design", "theme-factory", "web-artifacts-builder"}:
        return "design"
    raise ValueError(f"Categoría pendiente para {name}; revisar antes de extraer")


def write_additive(directory, files):
    directory = directory.resolve()
    if not directory.is_relative_to(ROOT):
        raise ValueError("Destino fuera del repositorio")
    # Validate all targets before writing this tree; never replace a differing file.
    targets = []
    for name, data in sorted(files.items()):
        target = (directory / safe_name(name)).resolve()
        if not target.is_relative_to(directory):
            raise ValueError("Destino fuera del árbol previsto")
        if target.exists() and (not target.is_file() or target.read_bytes() != data):
            raise ValueError(f"Colisión de contenido: {target}")
        targets.append((target, data))
    created = 0
    for target, data in targets:
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as handle:
                handle.write(data)
            created += 1
        if target.read_bytes() != data:
            raise ValueError(f"Verificación fallida: {target}")
    return created


def inventory():
    result = []
    for path in sorted((ROOT / "skills").rglob("SKILL.md")):
        metadata, name, text, encoding, error = frontmatter(path.read_bytes())
        issues = []
        if error:
            issues.append("frontmatter: " + error)
        if not metadata.get("description"):
            issues.append("description ausente/no interpretable")
        if encoding != "utf-8":
            issues.append("codificación CP1252; normalizar en revisión")
        if len(text.splitlines()) > 300:
            issues.append("entrada >300 líneas; revisar carga progresiva")
        if re.search(r"cyberdev\.qzz\.io|portafolio-svelte\.pages\.dev", text):
            issues.append("dominio/proyecto fijo")
        if re.search(r"before ANY response|starting any conversation|even a 1%", text, re.I):
            issues.append("activación global o umbral artificial")
        result.append({"name": name, "path": path.relative_to(ROOT).as_posix(),
                       "lines": len(text.splitlines()), "encoding": encoding,
                       "description": metadata.get("description"), "issues": issues})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extract-missing", action="store_true")
    args = parser.parse_args()
    before = inventory()
    existing = defaultdict(list)
    for item in before:
        existing[item["name"]].append(ROOT / item["path"])
    groups = defaultdict(list)
    archives = []
    # Scan every archive before beginning mutations.
    for path in sorted((ROOT / "SKILL").iterdir()):
        if not path.is_file() or path.suffix not in {".skill", ".zip"}:
            continue
        files = load_archive(path)
        entries = [n for n in files if PurePosixPath(n).name == "SKILL.md"]
        if not entries:
            raise ValueError(f"Sin SKILL.md: {path.name}")
        names = []
        for entry in entries:
            _, name, _, _, error = frontmatter(files[entry])
            if not name or not re.fullmatch(r"[a-z0-9-]{1,64}", name):
                raise ValueError(f"Nombre inválido en {path.name}: {entry}")
            names.append(name)
        if len(entries) > 1:
            if path.name != "system-correction-skill-pack.zip":
                raise ValueError(f"Pack múltiple requiere mapa explícito: {path.name}")
            prefix = "system-correction-skill-pack/"
            payload = {n[len(prefix):]: d for n, d in files.items() if n.startswith(prefix)}
            key = "system-correction-skill-pack"
            target = ROOT / "skills/quality" / key
        else:
            key = names[0]
            prefix = str(PurePosixPath(entries[0]).parent)
            prefix = "" if prefix == "." else prefix + "/"
            payload = {n[len(prefix):]: d for n, d in files.items() if n.startswith(prefix)}
            if key in existing:
                target = existing[key][0].parent
            else:
                target = ROOT / "skills" / category(key) / key
        item = {"archive": path.name, "archive_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "names": names, "target": target.relative_to(ROOT).as_posix(),
                "payload_sha256": digest(payload), "files": len(payload),
                "payload": payload, "archive_files": files}
        groups[key].append(item)
        archives.append(item)
    records = []
    created_files = 0
    for key, candidates in sorted(groups.items()):
        # Completeness is a selection policy, not a judgement of recency or quality.
        selected = sorted(candidates, key=lambda c: (-c["files"], c["archive"]))[0]
        destination = ROOT / selected["target"]
        present = key in existing or (key == "system-correction-skill-pack" and destination.exists())
        added = not present
        if added and args.extract_missing:
            if destination.exists():
                raise ValueError(f"Destino existente sin skill reconocida: {destination}")
            created_files += write_additive(destination, selected["payload"])
        canonical_files = (
            {p.relative_to(destination).as_posix(): p.read_bytes()
             for p in destination.rglob("*") if p.is_file()}
            if present or (added and args.extract_missing) else selected["payload"]
        )
        canonical_digest = digest(canonical_files)
        variants = {}
        for candidate in candidates:
            if candidate["payload_sha256"] == canonical_digest:
                candidate["status"] = "equivalente a fuente"
            else:
                candidate["status"] = "variante distinta; sin sobrescribir fuente"
                if candidate["payload_sha256"] not in variants:
                    snapshot = ROOT / "docs/skills/package-variants" / candidate["archive"]
                    if args.extract_missing:
                        created_files += write_additive(snapshot, candidate["archive_files"])
                    variants[candidate["payload_sha256"]] = snapshot.relative_to(ROOT).as_posix()
                candidate["variant_path"] = variants[candidate["payload_sha256"]]
        records.append({"group": key, "names": selected["names"], "target": selected["target"],
                        "was_missing": added, "selected_archive": selected["archive"],
                        "selection": "Mayor número de archivos; no implica más reciente/mejor",
                        "variants": list(variants.values())})
    after = inventory() if args.extract_missing else before
    clean_archives = [{k: v for k, v in c.items() if k not in {"payload", "archive_files"}}
                      for c in archives]
    report = {"mode": "extract-missing" if args.extract_missing else "audit",
              "source_skills_before": len(before), "source_skills_after": len(after),
              "archives": clean_archives, "groups": records, "inventory": after,
              "files_written": created_files}
    output = ROOT / "docs/skills/source-reconciliation.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    recovery = ROOT / "docs/skills/source-recovery.json"
    if args.extract_missing and any(r["was_missing"] for r in records) and not recovery.exists():
        recovery.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"before": len(before), "after": len(after), "archives": len(archives),
                      "groups": len(records), "missing_groups": sum(r["was_missing"] for r in records),
                      "variant_groups": sum(bool(r["variants"]) for r in records),
                      "files_written": created_files, "report": output.relative_to(ROOT).as_posix()},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
