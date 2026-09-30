#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED_REFS = [
    "architecture-selection.md",
    "repository-hygiene.md",
    "project-structure.md",
    "scalability-resilience.md",
    "security-architecture.md",
    "refactoring-protocol.md",
    "quality-gates.md",
    "research-policy.md",
    "output-contracts.md",
    "source-baseline.md",
]

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)

if not SKILL.exists():
    fail("SKILL.md missing")
text = SKILL.read_text(encoding="utf-8")
if not text.startswith("---\n"):
    fail("YAML front matter missing")
parts = text.split("---", 2)
if len(parts) < 3:
    fail("YAML front matter malformed")
front = parts[1]
for key in ("name:", "description:", "compatibility:", "metadata:"):
    if key not in front:
        fail(f"front matter missing {key}")
if not re.search(r"^name:\s*modern-software-architect\s*$", front, re.M):
    fail("unexpected skill name")
for ref in REQUIRED_REFS:
    if not (ROOT / "references" / ref).exists():
        fail(f"missing reference: {ref}")
for script in ("audit_repo_hygiene.py", "validate_skill.py"):
    if not (ROOT / "scripts" / script).exists():
        fail(f"missing script: {script}")
print("PASS: modern-software-architect skill structure is valid")
