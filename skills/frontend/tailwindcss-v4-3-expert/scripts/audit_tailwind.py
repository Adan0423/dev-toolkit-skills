#!/usr/bin/env python3
"""Read-only Tailwind integration audit."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

MANIFESTS = ["package.json", "pnpm-lock.yaml", "yarn.lock", "package-lock.json", "bun.lock", "bun.lockb"]
LEGACY_PATTERNS = {
    "legacy @tailwind directives": re.compile(r"@tailwind\s+(base|components|utilities)\s*;"),
    "v4 @import": re.compile(r"@import\s+[\"']tailwindcss[\"']"),
    "@theme": re.compile(r"@theme\b"),
    "@source": re.compile(r"@source\b|source\("),
}

print(f"Tailwind audit: {ROOT}")
print("READ-ONLY: no files will be changed.\n")

pkg = ROOT / "package.json"
if pkg.exists():
    try:
        data = json.loads(pkg.read_text(encoding="utf-8"))
        deps = {}
        for key in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
            deps.update(data.get(key, {}) or {})
        found = {k: v for k, v in deps.items() if "tailwind" in k.lower()}
        print("Tailwind-related packages:")
        if found:
            for k, v in sorted(found.items()):
                print(f"  - {k}: {v}")
        else:
            print("  (none declared in package.json)")
    except Exception as exc:
        print(f"Could not parse package.json: {exc}")
else:
    print("package.json not found")

print("\nManifest/lockfile clues:")
for name in MANIFESTS:
    if (ROOT / name).exists():
        print(f"  - {name}")

print("\nCSS/Tailwind syntax clues:")
matched = 0
skip_dirs = {"node_modules", ".git", ".next", "dist", "build", "coverage", ".cache"}
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in {".css", ".pcss", ".scss", ".sass", ".less"}:
        continue
    if any(part in skip_dirs for part in path.parts):
        continue
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        continue
    tags = [label for label, pattern in LEGACY_PATTERNS.items() if pattern.search(text)]
    if tags:
        matched += 1
        print(f"  - {path.relative_to(ROOT)}: {', '.join(tags)}")

if not matched:
    print("  (no obvious Tailwind CSS directives found)")

print("\nAudit complete.")
