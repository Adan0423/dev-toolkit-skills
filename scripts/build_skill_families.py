"""Build standalone family guides/packages from canonical source skills.

Only generated specialties and family metadata are refreshed. Original skills and
hand-authored family SKILL.md files are never overwritten. --check is read-only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "scripts/skill-families.json"
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
EXCLUDE = {".git", "__pycache__", "node_modules"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def text(data):
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return data.decode("cp1252")


def metadata(content):
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.S)
    if not match:
        raise ValueError("SKILL.md sin frontmatter")
    value = yaml.safe_load(match.group(1))
    if not isinstance(value, dict) or not value.get("name") or not value.get("description"):
        raise ValueError("Metadata de skill incompleta")
    return value, content[match.end():].lstrip()


def inside(path, parent):
    resolved = path.resolve()
    if not resolved.is_relative_to(parent.resolve()):
        raise ValueError(f"Ruta fuera de destino: {path}")
    return resolved


def adapt_markdown(content, source_file, source_root, mapping, adaptations):
    # Remove runtime-specific mandatory preparation; preserve the domain procedure.
    lines = []
    for line in content.splitlines():
        if re.match(r"^Invoke /impeccable\b", line):
            lines.append("Usa el contexto disponible de audiencia, tarea e identidad; "
                         "pregunta solo lo decisivo que falte. No requiere comandos externos.")
            adaptations.append("Preparación Impeccable sustituida por contexto de familia")
        else:
            line = line.replace("/impeccable craft", "la especialidad direction de esta familia")
            line = line.replace("/impeccable teach", "la preparación de contexto de esta familia")
            line = line.replace("/impeccable", "la especialidad direction de esta familia")
            lines.append(line)
    content = "\n".join(lines) + "\n"

    def local_link(match):
        label, target = match.groups()
        target = target.strip()
        if "://" in target or target.startswith(("#", "mailto:", "data:")):
            return match.group(0)
        path_part, separator, fragment = target.partition("#")
        resolved = (source_file.parent / path_part).resolve()
        if resolved.is_relative_to(source_root.resolve()):
            if resolved in mapping:
                # Retain local paths except references to the renamed entrypoint.
                if resolved.name == "SKILL.md":
                    new = path_part.rsplit("/", 1)
                    new[-1] = "guide.md"
                    return f"[{label}]({'/'.join(new)}{separator}{fragment})"
                return match.group(0)
            if resolved.exists():
                return match.group(0)
        adaptations.append(f"Dependencia no autocontenida eliminada: {target}")
        return f"{label} (recurso externo no incluido; usa herramientas disponibles si hace falta)"

    return LINK.sub(local_link, content)


def expected_family(name, specification):
    family = inside(ROOT / specification["path"], ROOT / "skills")
    parent_file = family / "SKILL.md"
    parent_metadata, _ = metadata(parent_file.read_text(encoding="utf-8"))
    if parent_metadata["name"] != name:
        raise ValueError(f"Nombre de familia inconsistente: {name}")
    expected = {}
    provenance = {"family": name, "generated_by": "scripts/build_skill_families.py",
                  "specialties": {}, "generated_files": []}
    for mode, relative in specification["specialties"].items():
        source = inside(ROOT / relative, ROOT / "skills")
        if family == source or family.is_relative_to(source):
            raise ValueError("Familia no puede copiarse a sí misma")
        source_files = [p for p in sorted(source.rglob("*")) if p.is_file()
                        and not (set(p.relative_to(source).parts) & EXCLUDE)
                        and p.suffix != ".pyc"
                        and not p.relative_to(source).as_posix().startswith("agents/")]
        mapping = {}
        for p in source_files:
            relative_file = p.relative_to(source).as_posix()
            if p.name == "SKILL.md" and relative_file != "SKILL.md":
                raise ValueError(f"Sub-skill anidada necesita mapa explícito: {p}")
            mapping[p.resolve()] = "guide.md" if relative_file == "SKILL.md" else relative_file
        sources = {}
        adaptations = []
        source_metadata = None
        supplemental = specification.get("resources", {}).get(mode, {})
        for virtual in supplemental:
            mapping[inside(source / virtual, source)] = virtual
        supplemental_hashes = {}
        for virtual, actual in supplemental.items():
            resource = inside(ROOT / actual, ROOT / "skills")
            data = resource.read_bytes()
            supplemental_hashes[actual] = sha(data)
            expected[f"references/specialties/{mode}/{virtual}"] = data
        for p in source_files:
            data = p.read_bytes()
            sources[p.relative_to(source).as_posix()] = sha(data)
            output = mapping[p.resolve()]
            if p.suffix == ".md":
                content = text(data)
                if p.name == "SKILL.md":
                    original_content = content
                    source_metadata, content = metadata(content)
                    original_header = original_content[:re.match(r"^---\s*\n(.*?)\n---", original_content, re.S).end()]
                    content = (original_header + "\n\n" + f"# Especialidad: {mode}\n\n"
                               f"Procedencia: `{relative}/SKILL.md`. Guía derivada; editar fuente "
                               "y reconstruir, no esta copia.\n\n"
                               "Aplica el procedimiento solo al modo seleccionado. Las preferencias "
                               "del usuario, alcance y contrato común de la familia delimitan "
                               "sus recomendaciones. No invoca otras skills por defecto.\n\n" + content)
                content = adapt_markdown(content, p, source, mapping, adaptations)
                if mode == "audit" and name == "repository-documentation":
                    replacements = {
                        "Produce a preflight proposal and wait for approval before writing, moving, merging, or deleting documentation files.": "Review evidence and scope, then carry out authorized reversible documentation edits. Ask only for missing authorization for expanded scope or destructive changes.",
                        "Mandatory preflight approval gate": "Evidence preflight and authorized scope",
                        "Before modifying anything, show the user:": "Before modifying documentation, review the following evidence; summarize what matters for the requested scope:",
                        "Then WAIT for explicit approval before full generation or destructive repository changes.": "Proceed with already authorized documentation work. Seek explicit approval only for destructive changes or expanded scope without prior authorization.",
                        "Quality pass after approval and generation": "Quality pass after implementation",
                        "After approved changes, summarize:": "After changes, summarize:",
                        "## Approval request": "## Scope and authorization",
                        "Ask for explicit approval to proceed with the proposed writes and cleanup operations.": "Proceed with authorized reversible writes. Ask only for missing authorization for destructive cleanup or expanded scope.",
                    }
                    for old, new in replacements.items():
                        if old in content:
                            content = content.replace(old, new)
                            adaptations.append("Documentación: respeta autorización existente para cambios reversibles")
                data = content.encode("utf-8")
            # Copied helpers that inspect their entrypoint must use the renamed file.
            elif p.suffix == ".py" and b"SKILL.md" in data:
                data = data.replace(b"SKILL.md", b"guide.md")
                if mode == "audit" and name == "repository-documentation":
                    data = data.replace(b"Mandatory preflight approval gate", b"Evidence preflight and authorized scope")
                adaptations.append(f"Helper {output}: referencia SKILL.md adaptada a guide.md")
            expected[f"references/specialties/{mode}/{output}"] = data
        provenance["specialties"][mode] = {
            "source": relative, "source_metadata": source_metadata,
            "supplemental_files_sha256": supplemental_hashes,
            "source_files_sha256": sources, "adaptations": sorted(set(adaptations))}
    display = {
        "react-engineering": ("React: ingeniería selectiva", "React por tarea: componentes, datos y rendimiento"),
        "tailwind-engineering": ("Tailwind: configuración y temas", "Tailwind por tarea: instalación, temas y shadcn"),
        "web-design-suite": ("Diseño web: especialidades", "Diseño por tarea: responsive, estilo y acabado"),
        "repository-documentation": ("Documentación de repositorios", "Auditoría, README y actualización por cambios"),
        "wordpress-suite": ("WordPress: selector de especialidad", "WordPress por tarea: código, builder y contenido"),
        "cv-suite": ("CV: formato y adaptación ATS", "CV por tarea: formato Harvard, logros y ATS"),
    }[name]
    ui = {"interface": {"display_name": display[0], "short_description": display[1],
                         "default_prompt": f"Usa ${name} para esta tarea y carga solo la especialidad necesaria."}}
    ui_text = "interface:\n" + "".join(
        f"  {key}: {json.dumps(value, ensure_ascii=False)}\n"
        for key, value in ui["interface"].items())
    expected["agents/openai.yaml"] = ui_text.encode("utf-8")
    provenance["generated_files"] = sorted(expected)
    expected["family-manifest.json"] = (json.dumps(provenance, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return family, expected


def package_files(family, expected):
    return {"SKILL.md": (family / "SKILL.md").read_bytes(), **expected}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    planned = [(name, *expected_family(name, spec)) for name, spec in config.items()]
    # Validate every family before writing; paths are fixed by repository config.
    for name, family, expected in planned:
        actual = {p.relative_to(family).as_posix() for p in family.rglob("*") if p.is_file()}
        unexpected = actual - {"SKILL.md", *expected}
        if unexpected:
            raise ValueError(f"Archivos no mapeados en {name}: {sorted(unexpected)}; revisar antes de reconstruir")
    writes = 0
    summary = []
    for name, family, expected in planned:
        for relative, data in expected.items():
            target = inside(family / relative, family)
            if args.check:
                if not target.is_file() or target.read_bytes() != data:
                    raise ValueError(f"Recurso derivado desactualizado: {target}")
            elif not target.is_file() or target.read_bytes() != data:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                writes += 1
        actual = {p.relative_to(family).as_posix() for p in family.rglob("*") if p.is_file()}
        supported = {"SKILL.md", *expected}
        unexpected = actual - supported
        if unexpected:
            raise ValueError(f"Archivos no mapeados en {name}: {sorted(unexpected)}; revisar antes de empaquetar")
        packaged = package_files(family, expected)
        output = ROOT / "SKILL" / f"{name}.zip"
        if args.check:
            with zipfile.ZipFile(output) as archive:
                if archive.testzip() is not None:
                    raise ValueError(f"ZIP corrupto: {output}")
                if set(archive.namelist()) != {f"{name}/{n}" for n in packaged}:
                    raise ValueError(f"Entradas ZIP no coinciden: {output}")
                for relative, data in packaged.items():
                    if archive.read(f"{name}/{relative}") != data:
                        raise ValueError(f"ZIP desactualizado: {name}/{relative}")
        else:
            with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
                for relative, data in sorted(packaged.items()):
                    archive.writestr(f"{name}/{relative}", data)
        summary.append({"family": name, "specialties": len(config[name]["specialties"]),
                        "files": len(packaged), "entrypoint_lines": len(packaged["SKILL.md"].splitlines()),
                        "zip": output.relative_to(ROOT).as_posix()})
    print(json.dumps({"mode": "check" if args.check else "build", "files_written": writes,
                      "families": summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
