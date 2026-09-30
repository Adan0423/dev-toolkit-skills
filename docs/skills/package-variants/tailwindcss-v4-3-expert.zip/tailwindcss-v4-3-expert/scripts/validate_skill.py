from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    root / "SKILL.md",
    root / "README.md",
    root / "references" / "vite-integration.md",
    root / "references" / "official-sources.md",
    root / "references" / "responsive-adaptive-design.md",
    root / "references" / "dark-mode-theming.md",
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print("FAIL: missing required files:")
    for item in missing:
        print(f" - {item}")
    sys.exit(1)

skill = (root / "SKILL.md").read_text(encoding="utf-8")
checks = [
    "name: tailwindcss-v4-3-expert",
    "version: 1.3.0",
    "@tailwindcss/vite",
    '@import "tailwindcss"',
    "analysis first",
    "continuous resize",
    "@container",
    "root-level horizontal overflow",
    "dark mode and theming",
    "light | dark | system",
    "scheme-light",
]
failed = [x for x in checks if x.lower() not in skill.lower()]
if failed:
    print("FAIL: SKILL.md is missing expected guidance:")
    for item in failed:
        print(f" - {item}")
    sys.exit(1)

print("PASS: tailwindcss-v4-3-expert v1.3.0 structure is valid")
