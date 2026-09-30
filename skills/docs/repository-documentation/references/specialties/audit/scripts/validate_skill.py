from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    root / "guide.md",
    root / "README.md",
    root / "references" / "source-baseline.md",
    root / "references" / "research-policy.md",
    root / "references" / "document-map.md",
    root / "references" / "preflight-template.md",
    root / "references" / "readme-quality.md",
    root / "references" / "cleanup-policy.md",
    root / "references" / "project-evidence.md",
    root / "scripts" / "audit_docs.py",
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print("FAIL: missing files:")
    for p in missing:
        print(" -", p)
    sys.exit(1)

text = (root / "guide.md").read_text(encoding="utf-8")
for needle in ["analyze before writing", "Evidence preflight and authorized scope", "Safe deletion protocol", "Never print secret values"]:
    if needle.lower() not in text.lower():
        print(f"FAIL: guide.md missing required concept: {needle}")
        sys.exit(1)

print("PASS: documentation-repository-curator skill structure is valid")
