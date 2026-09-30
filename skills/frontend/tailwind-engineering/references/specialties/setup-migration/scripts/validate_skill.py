#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    root / "guide.md",
    root / "README.md",
    root / "references" / "v4-3-features.md",
    root / "references" / "installation-routing.md",
    root / "references" / "theme-and-design-system.md",
    root / "references" / "responsive-and-containers.md",
    root / "references" / "source-detection.md",
    root / "references" / "custom-utilities-and-variants.md",
    root / "references" / "migration-v3-v4.md",
    root / "references" / "framework-integration.md",
    root / "references" / "quality-and-accessibility.md",
    root / "references" / "official-sources.md",
    root / "scripts" / "audit_tailwind.py",
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print("FAIL: missing required files")
    for item in missing:
        print(f" - {item}")
    sys.exit(1)
text = (root / "guide.md").read_text(encoding="utf-8")
for needle in ["@theme", "@source", "@container-size", "v4.3", "analysis-first"]:
    if needle.lower() not in text.lower():
        print(f"FAIL: guide.md missing expected concept: {needle}")
        sys.exit(1)
print("PASS: tailwindcss-v4-3-expert skill structure is valid")
