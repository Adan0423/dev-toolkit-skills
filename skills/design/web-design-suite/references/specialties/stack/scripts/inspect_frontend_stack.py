#!/usr/bin/env python3
"""Conservative frontend dependency inventory. Never modifies the target project."""
import json
import sys
from pathlib import Path

GROUPS = {
    "utility_css": ["tailwindcss", "unocss", "@unocss/", "@master/css"],
    "static_css": ["@pandacss/", "@stylexjs/", "@vanilla-extract/"],
    "runtime_css": ["@emotion/", "styled-components"],
    "headless": ["radix-ui", "@radix-ui/", "@base-ui-components/", "@headlessui/", "react-aria", "react-aria-components", "@ark-ui/", "ariakit", "@kobalte/", "bits-ui"],
    "react_suites": ["@mui/", "antd", "@mantine/", "@chakra-ui/", "@blueprintjs/", "primereact", "@heroui/"],
    "vue_suites": ["vuetify", "primevue", "@nuxt/ui", "element-plus", "quasar", "naive-ui"],
    "angular_suites": ["@angular/material", "primeng", "ng-zorro-antd", "@taiga-ui/"],
    "css_frameworks": ["bootstrap", "bulma", "foundation-sites", "uikit", "@picocss/pico", "purecss"],
    "icons": ["lucide", "lucide-react", "lucide-vue-next", "@phosphor-icons/", "@mui/icons-material", "@ant-design/icons", "@iconify/"],
    "animation": ["motion", "framer-motion", "gsap", "lenis", "@studio-freight/lenis"],
}


def matches(pkg: str, patterns):
    return any(pkg == p or pkg.startswith(p) for p in patterns)


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    package = root / "package.json"
    if not package.exists():
        print(f"No package.json found at {root}")
        return 1
    data = json.loads(package.read_text(encoding="utf-8"))
    deps = {}
    for key in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        deps.update(data.get(key, {}) or {})

    print(f"Project: {data.get('name', root.name)}")
    print(f"Dependencies scanned: {len(deps)}")
    found = {}
    for group, patterns in GROUPS.items():
        items = sorted([p for p in deps if matches(p, patterns)])
        if items:
            found[group] = items
            print(f"\n[{group}]")
            for p in items:
                print(f"  - {p}: {deps[p]}")

    print("\nOverlap hints (not automatic errors):")
    potential = []
    if len(found.get("react_suites", [])) > 1:
        potential.append("Multiple full React UI suites detected; verify whether they overlap intentionally.")
    if "bootstrap" in deps and "tailwindcss" in deps:
        potential.append("Bootstrap and Tailwind both detected; verify ownership of reset, layout and utilities.")
    if len(found.get("icons", [])) > 2:
        potential.append("Several icon packages detected; check for visual inconsistency and unused packs.")
    if "motion" in deps and "framer-motion" in deps:
        potential.append("Both motion and framer-motion detected; inspect migration/duplicate usage.")
    if not potential:
        print("  - No obvious overlaps from dependency names alone.")
    else:
        for item in potential:
            print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
