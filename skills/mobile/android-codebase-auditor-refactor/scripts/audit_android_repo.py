#!/usr/bin/env python3
"""Read-only Android/Kotlin repository audit helper.

Scans Kotlin/XML/Gradle text files for line-count hotspots and selected security
signals. It never modifies the target repository.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

IGNORED_DIRS = {
    ".git", ".gradle", ".idea", "build", "out", "node_modules",
    "generated", ".cxx", ".externalNativeBuild",
}

TEXT_SUFFIXES = {".kt", ".kts", ".java", ".xml", ".properties", ".toml", ".gradle", ".json"}

PATTERNS = [
    ("SEC-STORAGE", "SharedPreferences usage", re.compile(r"\b(SharedPreferences|getSharedPreferences|PreferenceManager)\b")),
    ("SEC-CLEARTEXT", "Cleartext HTTP URL", re.compile(r"http://(?!localhost\b|127\.0\.0\.1\b|10\.0\.2\.2\b)", re.I)),
    ("SEC-MANIFEST", "Cleartext traffic enabled", re.compile(r"usesCleartextTraffic\s*=\s*[\"']true[\"']", re.I)),
    ("SEC-TLS", "Permissive HostnameVerifier", re.compile(r"hostnameVerifier\s*\{[^\n]*(true|return@\w+\s+true)", re.I)),
    ("SEC-LOG", "Sensitive value near logging call", re.compile(r"(?:Log\.[divew]|Timber\.[divew]|println)\s*\([^\n]*(authorization|bearer|access.?token|refresh.?token|password|cookie|session)", re.I)),
    ("SEC-HTTPLOG", "HTTP BODY logging", re.compile(r"HttpLoggingInterceptor\.Level\.BODY")),
    ("STAB-GLOBALSCOPE", "GlobalScope usage", re.compile(r"\bGlobalScope\b")),
    ("STAB-RUNBLOCKING", "runBlocking usage", re.compile(r"\brunBlocking\s*\{")),
]

SECRET_ASSIGNMENT = re.compile(
    r"\b(api[_-]?key|client[_-]?secret|password|access[_-]?token|refresh[_-]?token|private[_-]?key)\b"
    r"\s*[:=]\s*[\"']([^\"']{8,})[\"']",
    re.I,
)


def walk_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"AndroidManifest.xml", "gradle.properties"}:
            yield path


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def audit(root: Path) -> dict:
    kotlin_files = []
    findings = []
    total_text_files = 0

    for path in walk_files(root):
        text = read_text(path)
        if text is None:
            continue
        total_text_files += 1
        rel = relative(path, root)
        lines = text.splitlines()

        if path.suffix.lower() == ".kt":
            loc = len(lines)
            kotlin_files.append({"file": rel, "lines": loc})

        for code, title, pattern in PATTERNS:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append({
                    "code": code,
                    "title": title,
                    "file": rel,
                    "line": line,
                    "evidence": lines[line - 1].strip()[:240] if line <= len(lines) else "",
                })

        for match in SECRET_ASSIGNMENT.finditer(text):
            value = match.group(2)
            if value.startswith(("${", "$", "<", "your_", "YOUR_")):
                continue
            line = text.count("\n", 0, match.start()) + 1
            findings.append({
                "code": "SEC-SECRET",
                "title": "Possible hardcoded secret",
                "file": rel,
                "line": line,
                "evidence": f"{match.group(1)} = <redacted>",
            })

    kotlin_files.sort(key=lambda item: item["lines"], reverse=True)
    over_300 = [item for item in kotlin_files if item["lines"] > 300]
    over_1000 = [item for item in kotlin_files if item["lines"] > 1000]

    return {
        "repository": str(root),
        "summary": {
            "text_files_scanned": total_text_files,
            "kotlin_files": len(kotlin_files),
            "kotlin_over_300": len(over_300),
            "kotlin_over_1000": len(over_1000),
            "security_and_stability_signals": len(findings),
        },
        "largest_kotlin_files": kotlin_files[:100],
        "kotlin_over_300": over_300,
        "kotlin_over_1000": over_1000,
        "signals": findings,
        "notice": "Pattern matches are audit signals, not automatically confirmed vulnerabilities. Review context before assigning severity.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Android/Kotlin repository audit")
    parser.add_argument("repository", nargs="?", default=".", help="Repository root (default: current directory)")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    args = parser.parse_args()

    root = Path(args.repository).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(json.dumps({"error": f"Not a directory: {root}"}, ensure_ascii=False), file=sys.stderr)
        return 2

    result = audit(root)
    if args.compact:
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
