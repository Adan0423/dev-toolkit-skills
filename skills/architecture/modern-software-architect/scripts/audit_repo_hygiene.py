#!/usr/bin/env python3
"""Conservative repository hygiene audit. Reports candidates; never deletes files."""
from __future__ import annotations
import argparse
from pathlib import Path

DIR_NAMES = {
    "node_modules", ".next", ".nuxt", "dist", "build", "out", "target",
    "bin", "obj", ".gradle", ".dart_tool", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", "__pycache__", ".cache", "coverage", ".coverage_html",
}
FILE_SUFFIXES = {".log", ".tmp", ".temp", ".bak", ".swp", ".swo", ".pyc", ".pyo"}
FILE_NAMES = {"Thumbs.db", ".DS_Store", "desktop.ini"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Report likely generated/cache/temp repository artifacts. Never deletes files.")
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    candidates: list[tuple[str, str]] = []
    for p in root.rglob("*"):
        try:
            rel = p.relative_to(root)
        except ValueError:
            continue
        if ".git" in rel.parts:
            continue
        if p.is_dir() and p.name in DIR_NAMES:
            candidates.append((str(rel), "generated/cache directory"))
            continue
        if p.is_file() and (p.name in FILE_NAMES or p.suffix.lower() in FILE_SUFFIXES):
            candidates.append((str(rel), "temporary/generated file"))

    print(f"Repository: {root}")
    print("Mode: audit-only (no deletions)\n")
    if not candidates:
        print("No obvious generated/cache/temp candidates found by conservative heuristics.")
        return 0

    for rel, reason in sorted(set(candidates)):
        print(f"- {rel}  [{reason}]")
    print("\nIMPORTANT: Verify .gitignore, git tracking, build/release/CI references, and run tests before deleting anything.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
