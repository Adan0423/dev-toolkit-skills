from pathlib import Path
import json
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
print(f"Tailwind audit (read-only): {root}")

pkg = root / "package.json"
if pkg.exists():
    try:
        data = json.loads(pkg.read_text(encoding="utf-8"))
        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        for name in ["vite", "tailwindcss", "@tailwindcss/vite", "@tailwindcss/postcss", "postcss"]:
            if name in deps:
                print(f"{name}: {deps[name]}")
    except Exception as exc:
        print(f"package.json parse warning: {exc}")
else:
    print("package.json: not found")

vite_files = []
for name in ["vite.config.js", "vite.config.ts", "vite.config.mjs", "vite.config.mts"]:
    p = root / name
    if p.exists():
        vite_files.append(p)
        text = p.read_text(encoding="utf-8", errors="ignore")
        print(f"Vite config: {name}")
        print(f"  has @tailwindcss/vite: {'@tailwindcss/vite' in text}")

postcss = [p.name for p in root.glob("postcss.config.*")]
if postcss:
    print("PostCSS config(s): " + ", ".join(postcss))

css_files = []
for base in [root / "src", root / "app", root / "resources", root]:
    if base.exists() and base.is_dir():
        for p in base.rglob("*.css"):
            if "node_modules" in p.parts or "dist" in p.parts or "build" in p.parts:
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if "tailwindcss" in text or "@tailwind" in text or "@theme" in text:
                css_files.append(p)
                rel = p.relative_to(root)
                print(f"Tailwind CSS clue: {rel}")
                print(f"  @import tailwindcss: {'@import \"tailwindcss\"' in text or "@import 'tailwindcss'" in text}")
                print(f"  legacy @tailwind directives: {'@tailwind ' in text}")
                print(f"  @theme: {'@theme' in text}")
                print(f"  custom dark variant: {'@custom-variant dark' in text}")
                print(f"  dark utilities: {'dark:' in text}")
                print(f"  color-scheme utilities: {'scheme-' in text}")

if vite_files and pkg.exists():
    print("Recommendation clue: Vite detected; verify whether @tailwindcss/vite should be the Tailwind processing path.")
print("No files were modified.")
