"""Package one standalone source skill in SKILL/, or check its package without writes."""
from __future__ import annotations

import argparse
import json

from build_skill_families import EXCLUDE, ROOT, inside, metadata, package


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_path", help="Ruta a una carpeta skill bajo skills/")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = inside(ROOT / args.skill_path, ROOT / "skills")
    if not (source / "SKILL.md").is_file():
        parser.error("No hay SKILL.md en esa carpeta")
    name = metadata((source / "SKILL.md").read_text(encoding="utf-8-sig"))[0]["name"]
    if source.name != name:
        parser.error("Nombre de carpeta y skill no coinciden")
    files = {}
    for item in sorted(source.rglob("*")):
        relative = item.relative_to(source)
        if not item.is_file() or set(relative.parts) & EXCLUDE or item.suffix == ".pyc":
            continue
        inside(item, source)
        if item.name.casefold() == ".env" or item.name.casefold().startswith(".env."):
            parser.error("Revisar y retirar archivos de entorno antes de empaquetar")
        if item.name == "SKILL.md" and relative.as_posix() != "SKILL.md":
            parser.error("Las skills anidadas requieren un empaquetador específico")
        files[relative.as_posix()] = item.read_bytes()
    output = package(name, files, args.check)
    print(json.dumps({"skill": name, "mode": "check" if args.check else "package",
                      "files": len(files), "zip": output.relative_to(ROOT).as_posix()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
