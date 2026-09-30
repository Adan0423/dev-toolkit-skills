from __future__ import annotations
from pathlib import Path
import hashlib
import sys

DOC_EXTS = {".md", ".mdx", ".rst", ".txt"}
SKIP_DIRS = {".git", "node_modules", ".next", "dist", "build", "target", ".venv", "venv", "__pycache__"}
BACKUP_MARKERS = (".bak", ".old", ".orig", " copy", " copia", "backup")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.exists():
        print(f"Path not found: {root}")
        return 2

    docs: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in DOC_EXTS:
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts):
            continue
        docs.append(p)

    print(f"Documentation files: {len(docs)}")
    for p in sorted(docs):
        rel = p.relative_to(root)
        print(f" - {rel} ({p.stat().st_size} bytes)")

    by_hash: dict[str, list[Path]] = {}
    for p in docs:
        try:
            by_hash.setdefault(sha256(p), []).append(p)
        except OSError:
            pass

    dupes = [group for group in by_hash.values() if len(group) > 1]
    if dupes:
        print("\nExact duplicate content candidates:")
        for group in dupes:
            print(" * " + " | ".join(str(p.relative_to(root)) for p in group))

    backups = [p for p in docs if any(marker in p.name.lower() for marker in BACKUP_MARKERS)]
    if backups:
        print("\nBackup/old-looking documentation candidates (review only):")
        for p in backups:
            print(" -", p.relative_to(root))

    print("\nREAD-ONLY AUDIT: no files were changed or deleted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
