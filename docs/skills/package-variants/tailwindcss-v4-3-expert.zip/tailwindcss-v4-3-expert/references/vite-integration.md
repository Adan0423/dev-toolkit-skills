# Tailwind CSS v4.3 — Vite Integration

## Decision rule

When the project actually uses Vite, prefer the first-party `@tailwindcss/vite` plugin unless an official framework guide or project-specific constraint requires another route.

## Standard install

Use the active package manager:

```bash
npm install tailwindcss @tailwindcss/vite
```

Equivalent package-manager commands are acceptable.

## Standard config

Add Tailwind to the existing Vite plugin chain instead of replacing it:

```ts
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

Framework Vite plugins must remain present. Follow official framework guides where plugin order, CSS loading, SSR, or route integration differs.

## CSS entry

```css
@import "tailwindcss";
```

Tailwind v4 automatically detects most sources. Add `@source` only for sources that automatic detection does not cover.

## Existing PostCSS projects

A Vite project can have PostCSS for reasons unrelated to Tailwind. Before changing:

- inspect `postcss.config.*`;
- inspect all PostCSS dependencies;
- identify which plugins are used;
- move only Tailwind's integration path when appropriate;
- never remove a required transform just because Tailwind no longer needs it.

## Framework routing

When Vite is used indirectly through a framework, check Tailwind's official framework guide before editing configuration. Common examples include Laravel, SvelteKit, React Router, Nuxt, SolidJS, Qwik, and AdonisJS.

## Validation

After setup or migration:

1. Run the project's dev command.
2. Run production build.
3. Confirm the global CSS entry is loaded by the app.
4. Confirm representative Tailwind classes generate styles.
5. Check source detection for workspace/shared component packages.
6. Verify no duplicate Tailwind processing path remains.
7. Verify the responsive viewport mechanism/meta tag is correct.
8. Run continuous-resize responsive QA from narrow mobile through ultrawide layouts, plus relevant orientation/input states.
9. Confirm there is no accidental root-level horizontal overflow and that shared components adapt in narrow containers.
