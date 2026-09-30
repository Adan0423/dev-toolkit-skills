from pathlib import Path
import argparse
import json

GEN_DIRS = {"node_modules", "dist", "build", ".next", ".nuxt", ".svelte-kit", "coverage", ".cache"}
CODE_EXTS = {".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html", ".css", ".scss"}
GENERIC_DIRS = {"misc", "common", "helpers", "utils"}


def audit(root: Path):
    findings = []
    for p in root.rglob("*"):
        if any(part in GEN_DIRS for part in p.parts):
            continue
        if p.is_dir() and p.name.lower() in GENERIC_DIRS:
            files = [x for x in p.rglob("*") if x.is_file()]
            if len(files) >= 12:
                findings.append({"type": "generic_bucket", "path": str(p), "files": len(files)})
        if p.is_file() and p.suffix.lower() in CODE_EXTS:
            try:
                lines = p.read_text(encoding="utf-8", errors="ignore").count("\n") + 1
            except OSError:
                continue
            if lines >= 500:
                findings.append({"type": "large_file", "path": str(p), "lines": lines})
    return findings

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Conservative frontend structure audit; never modifies files.")
    ap.add_argument("path", nargs="?", default=".")
    args = ap.parse_args()
    root = Path(args.path).resolve()
    result = audit(root)
    print(json.dumps({"root": str(root), "findings": result}, indent=2, ensure_ascii=False))
