"""Check declared opaque sRGB HEX pairs or emit CSS tokens. No DOM audit or network."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

THRESHOLDS = {"text": 4.5, "large": 3.0, "ui": 3.0}
TOKEN = re.compile(r"[a-z][a-z0-9-]*")


def normalize_hex(value):
    if not isinstance(value, str) or not re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", value.strip()):
        raise ValueError("Color requiere HEX sRGB opaco #RGB o #RRGGBB; resolver otros formatos antes de medir")
    value = value.strip()[1:]
    if len(value) == 3:
        value = "".join(part * 2 for part in value)
    return "#" + value.upper()


def luminance(value):
    normalized = normalize_hex(value)[1:]
    channels = [int(normalized[index:index+2], 16) / 255 for index in (0, 2, 4)]
    linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
              for channel in channels]
    return sum(channel * weight for channel, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast_ratio(foreground, background):
    first, second = luminance(foreground), luminance(background)
    return (max(first, second) + 0.05) / (min(first, second) + 0.05)


def meets_requirement(ratio, kind):
    if kind not in THRESHOLDS:
        raise ValueError("Tipo de pareja desconocido: text, large o ui")
    return ratio >= THRESHOLDS[kind]


def pair_result(foreground, background, kind="text"):
    value = contrast_ratio(foreground, background)
    return {"foreground": normalize_hex(foreground), "background": normalize_hex(background),
            "kind": kind, "ratio": value, "threshold": THRESHOLDS.get(kind),
            "passes": meets_requirement(value, kind)}


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"Clave JSON duplicada: {key}")
        value[key] = item
    return value


def load_palette(path):
    value = json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object)
    themes = value.get("themes") if isinstance(value, dict) else None
    if not isinstance(themes, dict) or not themes or not set(themes).issubset({"light", "dark"}):
        raise ValueError("themes debe contener light y/o dark")
    for theme, tokens in themes.items():
        if not isinstance(tokens, dict) or not tokens:
            raise ValueError(f"Tema sin tokens: {theme}")
        for token, color in tokens.items():
            if not TOKEN.fullmatch(token):
                raise ValueError(f"Nombre de token no válido: {token}")
            normalize_hex(color)
    return value


def audit_palette(value):
    checks = value.get("checks")
    if not isinstance(checks, list) or not checks:
        raise ValueError("checks requiere parejas declaradas; lista vacía no acredita contraste")
    results, ids, checked = [], set(), set()
    for index, check in enumerate(checks, 1):
        if not isinstance(check, dict):
            raise ValueError(f"Pareja {index}: objeto requerido")
        theme = check.get("theme")
        foreground, background = check.get("foreground"), check.get("background")
        if not isinstance(theme, str) or theme not in value["themes"]:
            raise ValueError(f"Pareja {index}: tema desconocido")
        tokens = value["themes"][theme]
        if not isinstance(foreground, str) or not isinstance(background, str) or foreground not in tokens or background not in tokens:
            raise ValueError(f"Pareja {index}: token desconocido")
        identifier = check.get("id", f"pair-{index}")
        if not isinstance(identifier, str) or not identifier.strip() or identifier in ids:
            raise ValueError(f"Pareja {index}: id vacío o duplicado")
        ids.add(identifier)
        result = pair_result(tokens[foreground], tokens[background], check.get("kind", "text"))
        results.append({"id": identifier, "theme": theme, "tokens": [foreground, background], **result})
        checked.add(theme)
    return {"scope": "declared_pairs_only", "checked_pairs": len(results),
            "unchecked_themes": sorted(set(value["themes"]) - checked),
            "passes_all_declared_pairs": all(result["passes"] for result in results),
            "results": results,
            "limitations": ["No inspecciona DOM, estados, opacidad, gradients o fuentes",
                            "El tipo text/large/ui lo declara el usuario; no valida tamaño ni criterio completo"]}


def emit_css(value):
    themes = value["themes"]
    default = "light" if "light" in themes else "dark"

    def block(selector, theme, indent=""):
        lines = [f"{indent}{selector} {{", f"{indent}  color-scheme: {theme};"]
        lines += [f"{indent}  --color-{token}: {normalize_hex(color)};" for token, color in themes[theme].items()]
        return "\n".join([*lines, f"{indent}}}"])

    sections = ["/* Derived semantic tokens. Adapt to project roles; contrast checks are separate. */", block(":root", default)]
    if set(themes) == {"light", "dark"}:
        sections.append(block(':root[data-theme="dark"]', "dark"))
        sections.append('@media (prefers-color-scheme: dark) {\n' +
                        block(':root:not([data-theme="light"]):not([data-theme="dark"])', "dark", "  ") + '\n}')
    return "\n\n".join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    pair = sub.add_parser("pair")
    pair.add_argument("--foreground", required=True)
    pair.add_argument("--background", required=True)
    pair.add_argument("--kind", choices=THRESHOLDS, default="text")
    for command in ("check", "css"):
        sub.add_parser(command).add_argument("palette", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "pair":
            result = pair_result(args.foreground, args.background, args.kind)
            success = result["passes"]
        else:
            value = load_palette(args.palette)
            if args.command == "css":
                print(emit_css(value), end="")
                return 0
            result = audit_palette(value)
            success = result["passes_all_declared_pairs"]
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        return 0 if success else 1
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
