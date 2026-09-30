# Tailwind CSS v4.3 Expert Skill v1.3.0

Reusable skill for production-grade Tailwind CSS v4.3 work, with first-class **Vite integration**.

## Highlights

- Analyze the project before changing Tailwind.
- Detect the real framework, package manager, build tool, and Tailwind version.
- Prefer `@tailwindcss/vite` for compatible Vite projects.
- Preserve existing framework plugins in `vite.config.*`.
- Avoid redundant Tailwind PostCSS + Vite processing.
- Use v4 CSS-first configuration with `@import "tailwindcss"` and `@theme`.
- Handle source detection, `@source`, `@reference`, custom utilities, and variants.
- Support v3 → v4.3 migration safely.
- Build fully adaptive, accessible, reusable component systems across mobile, tablet, desktop, and ultrawide layouts.
- Enforce mobile-first, content-driven breakpoints, container queries, fluid sizing, orientation/input adaptation, and continuous-resize QA.
- Treat dark mode as a first-class system: light/dark/system strategies, semantic tokens, native `color-scheme`, preference persistence, FOUC/hydration safety, and full dark-theme QA.
- Treat root-level horizontal overflow, clipped controls, broken intermediate widths, and unusable touch/navigation states as responsive failures.
- Validate dev/build/lint/typecheck/tests and visual behavior.

## Vite baseline

```bash
npm install tailwindcss @tailwindcss/vite
```

```ts
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

```css
@import "tailwindcss";
```

The skill must merge this with the project's real Vite configuration instead of overwriting existing plugins.

## Validation

```bash
python scripts/validate_skill.py
```

## Read-only project audit

```bash
python scripts/audit_tailwind.py /path/to/project
```

## Mandatory responsive standard

The skill does not design for a few named devices. It treats viewport width as a continuum and validates representative checkpoints plus continuous resizing. It uses Tailwind viewport variants for page-level changes and container queries for components that must adapt to their parent.

See `references/responsive-adaptive-design.md`.

## Mandatory dark mode standard

When theming is supported, the skill validates the complete interface in light and dark modes across the same responsive continuum. It can use system `prefers-color-scheme`, a manual root `.dark` selector, or a `[data-theme=dark]` strategy according to the existing architecture. For theme switchers it can support `light | dark | system`, preserving user preference and preventing avoidable wrong-theme flashes.

See `references/dark-mode-theming.md`.
