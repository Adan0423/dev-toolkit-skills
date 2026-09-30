#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "references" / "decision-engine.md",
    ROOT / "references" / "catalog.md",
    ROOT / "references" / "research-policy.md",
    ROOT / "scripts" / "inspect_frontend_stack.py",
]
missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    raise SystemExit("FAIL missing: " + ", ".join(missing))
text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not text.startswith("---\n") or not re.search(r"^name:\s*adaptive-web-ui-stack-architect\s*$", text, re.M):
    raise SystemExit("FAIL invalid SKILL.md frontmatter")
for ref in re.findall(r"`(references/[^`]+\.md)`", text):
    if not (ROOT / ref).exists():
        raise SystemExit(f"FAIL missing referenced file: {ref}")
print("PASS: adaptive-web-ui-stack-architect skill structure is valid")
