from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    root / "SKILL.md",
    root / "README.md",
    root / "references" / "repository-reorganization.md",
    root / "references" / "framework-routing.md",
    root / "references" / "decision-engine.md",
    root / "references" / "research-policy.md",
    root / "references" / "tailwind-bootstrap.md",
    root / "references" / "iconography.md",
    root / "references" / "responsive-accessibility.md",
    root / "references" / "visual-qa.md",
    root / "references" / "output-contracts.md",
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
text = (root / "SKILL.md").read_text(encoding="utf-8") if (root / "SKILL.md").exists() else ""
checks = {
    "frontmatter": text.startswith("---\n") and "\n---\n" in text[4:],
    "name": "name: web-ui-ux-frontend-architect" in text,
    "analysis-first": "Analysis First" in text,
    "reorganization": "reorganizar automáticamente" in text,
    "responsive-qa": "RESPONSIVE QA" in text or "Responsive QA" in text,
}
failed = [k for k, v in checks.items() if not v]
if missing or failed:
    print("FAIL")
    if missing:
        print("Missing:", ", ".join(missing))
    if failed:
        print("Checks:", ", ".join(failed))
    sys.exit(1)
print("PASS: web-ui-ux-frontend-architect skill structure is valid")
