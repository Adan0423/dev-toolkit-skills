# Theme variables and design systems

Tailwind v4 uses CSS-first theme variables.

Use `@theme` for tokens that should create utility APIs:

```css
@import "tailwindcss";

@theme {
  --font-display: "Inter", sans-serif;
  --color-brand-500: oklch(0.62 0.19 255);
  --spacing-panel: 1.5rem;
  --radius-card: 1rem;
  --shadow-card: 0 12px 32px rgb(0 0 0 / 0.08);
}
```

Use ordinary `:root` variables for runtime/config values that should not produce Tailwind utilities.

## Shared tokens

In monorepos, shared theme CSS can be imported by multiple apps. Prefer a dedicated shared theme package/file rather than copying the same token declarations.

## Avoid

- huge arbitrary-value repetition;
- duplicate token definitions across modules;
- hard-coded color literals repeated in JSX/templates;
- theme variables with no semantic or reuse value.
