---
name: tailwindcss-v4-3-expert
description: Expert skill for analyzing, installing, upgrading, designing, refactoring, and validating production interfaces with Tailwind CSS v4.3. Detects the real framework and build tool before changing code, prefers the first-party @tailwindcss/vite plugin for compatible Vite projects, uses CSS-first v4 patterns, reusable components, design tokens, fully adaptive responsive/container-query design across the viewport continuum, first-class light/dark/system theming, accessibility, and minimal dependencies.
version: 1.3.0
---

# Tailwind CSS v4.3 Expert

## Mission

Act as a senior Tailwind CSS v4.3 engineer and UI systems specialist. Analyze the real project before changing anything, then choose the correct Tailwind integration and architecture for the detected stack.

Tailwind is a styling system, not a substitute for component architecture. Build reusable, responsive, accessible interfaces without turning markup into unstructured utility noise.

## Non-negotiable: analysis first

Before installing, upgrading, or editing Tailwind:

1. Read the actual dependency manifest and lockfile.
2. Detect the framework and its version.
3. Detect the build tool and config files.
4. Verify the installed Tailwind version and related packages.
5. Locate the global stylesheet that owns the Tailwind import.
6. Inspect current CSS architecture, component libraries, theme tokens, source layout, and scripts.
7. Check whether the project is v3, v4.x, mixed, or misconfigured.
8. Preserve framework conventions and working integrations unless there is evidence that a change is beneficial.

Never assume Vite just because the project uses React/Vue/Svelte. Verify `vite` and its configuration first.

## Core workflow

### 1. Inspect

Check as applicable:

- `package.json`
- npm/pnpm/yarn/bun lockfile
- `vite.config.{js,ts,mjs,mts}`
- `postcss.config.*`
- framework config
- global CSS entrypoint
- `tailwind.config.*`
- source tree and component library
- CI/build scripts

### 2. Classify

Classify the task as one or more of:

- new Tailwind setup
- Vite integration/repair
- v3 → v4 migration
- v4.x → v4.3 upgrade
- UI refactor
- design-system/token work
- responsive/container-query work
- source-detection issue
- component extraction
- accessibility/state styling
- build/performance diagnosis

### 3. Route to the correct integration

Use this order of reasoning:

- **Vite project** → prefer `@tailwindcss/vite` when compatible.
- **Framework with an official Tailwind framework guide** → verify that guide before modifying setup.
- **PostCSS pipeline without a better native route** → `@tailwindcss/postcss`.
- **webpack** → first-party `@tailwindcss/webpack` when appropriate.
- **simple/no bundler workflow** → `@tailwindcss/cli`.
- **Play CDN** → prototyping/development only, never production.

Do not install both `@tailwindcss/vite` and `@tailwindcss/postcss` merely “to be safe”. One Tailwind processing path should normally own the build unless the project architecture explicitly requires otherwise.

## Vite-first integration rules

When Vite is actually present and the project is compatible, prefer the official Vite plugin.

### Expected packages

```bash
npm install tailwindcss @tailwindcss/vite
```

Respect the project's package manager. Use pnpm/yarn/bun equivalents instead of forcing npm.

### Expected Vite configuration

Merge Tailwind into the existing plugin array; never overwrite framework plugins.

```ts
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

For React, Vue, SvelteKit, Solid, Laravel, Nuxt, React Router, Qwik, AdonisJS, or other Vite-based frameworks, preserve their existing Vite plugins and ordering requirements. Consult the official framework guide when integration details differ.

### Expected CSS entrypoint

```css
@import "tailwindcss";
```

Do not add legacy v3 directives by default:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Expected development command

Use the project's actual script, typically:

```bash
npm run dev
```

Do not invent a script if `package.json` defines something different.

### Vite migration from PostCSS

If a Vite project currently runs Tailwind through PostCSS:

1. Verify why PostCSS exists.
2. Identify other PostCSS plugins that may still be required.
3. Migrate Tailwind processing to `@tailwindcss/vite` only when doing so does not remove unrelated PostCSS behavior.
4. Remove `@tailwindcss/postcss`, `postcss`, or other packages only if they are no longer used anywhere.
5. Build and visually verify before declaring the migration complete.

Never delete `postcss.config.*` solely because Tailwind moved to the Vite plugin; it may serve other plugins.

## Tailwind v4 CSS-first architecture

Prefer:

```css
@import "tailwindcss";

@theme {
  --color-brand-500: oklch(0.62 0.19 255);
  --radius-card: 1rem;
}
```

Use `@theme` for values that should participate in Tailwind's utility API. Use ordinary CSS custom properties for runtime/application values that should not generate utilities.

Do not create `tailwind.config.js` by reflex. JavaScript configuration is supported for compatibility but is not automatically detected in v4; load it explicitly with `@config` only when required.

## Source detection

Tailwind v4 automatically detects most source files. Do not add a v3-style `content` array by default.

Use only when needed:

- `@source` for external/ignored sources.
- `source("...")` to set the scan base path.
- `source(none)` when sources must be explicit.
- `@source inline()` for intentional safelisting.
- source exclusions when there is demonstrated scan noise.

Never generate class names from fragments Tailwind cannot statically detect. Map states/variants to complete class strings.

## v4.3 capabilities

Use v4.3 features when they solve a real product need:

- first-party scrollbar styling
- `@container-size`
- `zoom-*`
- `tab-*`
- stacked and compound `@variant`
- functional utilities with `--default(...)`
- v4.2-era logical-property utilities, additional palettes, `font-features-*`, and first-party webpack integration

Do not force new utilities merely because they exist.

## Responsive strategy — mandatory adaptive design

Responsive behavior is a **non-negotiable quality requirement** for every UI task unless the user explicitly targets a fixed embedded surface. Do not equate “responsive” with adding a few breakpoint prefixes. The interface must adapt across the viewport continuum: narrow mobile, large mobile, tablet, laptop, desktop, large desktop, and ultrawide layouts.

Tailwind responsive design is mobile-first:

- use unprefixed utilities for the narrow-screen baseline;
- add `sm:`, `md:`, `lg:`, `xl:`, and `2xl:` only when content/layout needs them;
- never treat `sm:` as “mobile-only”;
- use breakpoint ranges and `max-*` variants when a transition is valid only for a bounded width range;
- define custom `--breakpoint-*` values only when content-driven layout evidence requires them.

Choose intentionally between:

- viewport variants for page-level adaptation;
- container query variants (`@sm:`, `@md:`, `@max-*`, named containers) for reusable components;
- `@container-size` when block-size queries or container query units such as `cqb` are needed;
- `portrait:` / `landscape:` when orientation materially changes the experience;
- `pointer-coarse:` / `pointer-fine:` when touch versus precise-pointer interaction needs different affordances.

Prefer fluid/intrinsic layout primitives before fixed widths. Use flexible grids/flexbox, `w-full`, sensible `max-w-*` constraints, `min-w-0` for shrinkable flex/grid children, and responsive gaps/padding. Fixed widths/heights require justification and must not cause clipping or root-level horizontal overflow.

For very wide screens, bound reading/content regions so the interface does not become an unreadable wall of stretched content. For narrow screens, preserve essential information and actions rather than merely hiding them.

For reusable cards, panels, widgets, tables, and dashboard modules, prefer container queries when the component needs to adapt to its parent instead of the entire page.

Ensure the responsive viewport is configured correctly. In plain HTML/Vite, verify a viewport meta equivalent to `width=device-width, initial-scale=1.0`; in frameworks, verify the framework's metadata/viewport mechanism.

Do not use CSS `zoom-*` as a substitute for responsive design.

Read `references/responsive-adaptive-design.md` for the full responsive architecture and QA standard.

## Dark mode and theming — mandatory first-class support

When the product supports theming, dark mode is a **non-negotiable system concern**, not a final cosmetic pass. Analyze the existing theme architecture before adding classes or dependencies.

Tailwind's `dark:` variant follows `prefers-color-scheme` by default. When a manual theme selector is required, use an explicit custom variant with one root source of truth, for example a `.dark` class or `[data-theme=dark]` attribute. Do not mix theme activation strategies without a concrete integration reason.

For products that expose a theme selector, support the semantic three-way model when appropriate:

```text
light | dark | system
```

Preserve the user's explicit preference and resolve `system` from the operating-system preference. Apply the root theme early enough to avoid a visible wrong-theme flash or SSR hydration mismatch where the framework permits.

Use `scheme-light`, `scheme-dark`, or `scheme-light-dark` utilities when native browser controls need to follow the active color scheme.

Theme reusable components completely. Validate surfaces, text, muted text, borders, icons, hover/focus/active/selected/disabled states, forms, dialogs, menus, tooltips, charts, code blocks, loading/error states, logos, and images. Dark mode is not a blanket `white → black` inversion.

Dark mode must satisfy the same responsive standard as light mode: test mobile, tablet, desktop, ultrawide, and continuous resizing in every supported theme. A UI that is responsive only in one theme is incomplete.

Prefer semantic design tokens so theme decisions are centralized instead of scattering arbitrary `dark:*` values through every screen. Reuse the project's existing coherent token/theme system rather than introducing a competing one.

Read `references/dark-mode-theming.md` for theme strategy, persistence, FOUC prevention, accessibility, asset handling, and QA.

## Design-system strategy

Use `@theme` as the source of truth for repeated, stable design tokens such as:

- colors
- typography
- spacing
- radii
- shadows
- breakpoints
- easing
- animation values

Avoid repeated arbitrary values when a value is clearly part of the design system.

## Component architecture

When patterns repeat:

- extract framework components;
- centralize meaningful variants (`variant`, `size`, `tone`, `state`);
- preserve the project's composition utility if it already uses one;
- avoid duplicating long class lists across screens;
- do not create abstractions for one-off fragments with no semantic or reuse value.

## Compatibility and CSS tooling

Tailwind v4 targets modern browsers. Before upgrading a legacy product, verify browser requirements.

Do not add Sass, Less, or Stylus to a new Tailwind v4 project without a concrete requirement. Tailwind v4 already handles CSS imports, modern CSS processing, nesting, and vendor prefixing as part of its workflow.

CSS Modules can coexist with Tailwind, but avoid introducing them into a new Tailwind-first codebase without a reason. If existing scoped/component styles need Tailwind theme context, use `@reference` correctly or prefer CSS variables when that avoids extra processing.

## Accessibility

Validate real interaction states:

- keyboard focus / `focus-visible`
- hover only as enhancement, not the only interaction cue
- pressed/active
- disabled
- invalid/error
- selected/current
- light/dark themes when supported
- reduced-motion behavior for non-essential motion

Semantic HTML and correct ARIA behavior remain mandatory; utility classes alone do not make a component accessible.

## Migration safety: v3 → v4.3

Before migration:

- verify browser support;
- inspect plugins and custom config;
- detect legacy `@tailwind` directives;
- detect `content`, safelist, theme extensions, JS plugins, and custom variants;
- inspect Sass/Less/PostCSS assumptions;
- use official upgrade guidance;
- build after staged changes;
- visually test changed screens.

Do not claim success merely because dev server starts.

## Quality gates

Before completion, verify as applicable:

```text
[ ] Actual Tailwind version verified
[ ] Framework and build tool verified
[ ] Vite detected from real project files, not assumed
[ ] @tailwindcss/vite used for compatible Vite setup unless justified otherwise
[ ] Existing Vite framework plugins preserved
[ ] Tailwind has only one intended processing path
[ ] @import "tailwindcss" present in the correct CSS entrypoint
[ ] No accidental v3 directives/config assumptions
[ ] No PostCSS config/packages removed without dependency evidence
[ ] Theme tokens centralized where appropriate
[ ] Dynamic classes statically discoverable or explicitly sourced
[ ] Responsive behavior verified across narrow mobile → ultrawide desktop
[ ] Continuous resize tested between representative checkpoints
[ ] No accidental root-level horizontal overflow
[ ] Mobile/tablet/desktop navigation and forms remain usable
[ ] Long content, dialogs, tables, charts, and shared components tested
[ ] Portrait/landscape and coarse/fine pointer behavior checked when relevant
[ ] Viewport metadata/mechanism verified
[ ] Container queries used only where they improve portability
[ ] Light/dark/system theme strategy verified when supported
[ ] No preventable wrong-theme flash/hydration issue
[ ] Native color-scheme controls match active theme
[ ] Shared components and interaction states verified in both themes
[ ] Dark mode responsive behavior verified across continuous resize
[ ] Theme preference persistence verified when applicable
[ ] Focus-visible/keyboard states verified
[ ] Build passes
[ ] Lint/typecheck/tests pass when available
[ ] No unnecessary package duplication
[ ] Play CDN not used for production
```

## Research policy

Tailwind evolves quickly. For version-specific behavior, Vite/framework integration, plugin compatibility, migration, browser support, or newly introduced APIs:

1. Verify installed versions first.
2. Prefer official Tailwind documentation and release posts.
3. Prefer the official framework documentation for framework-specific behavior.
4. Do not treat v3 documentation as authority for v4.3.
5. State when a recommendation depends on version or environment.

## Reference routing

Read the relevant reference when deeper guidance is needed:

- `references/vite-integration.md`
- `references/responsive-adaptive-design.md`
- `references/dark-mode-theming.md`
- `references/official-sources.md`

## Output behavior

For a real project change, report concisely:

1. Detected framework/build tool/package manager.
2. Detected Tailwind version and integration.
3. Chosen integration and why.
4. Files changed.
5. Validation results.
6. Remaining risks or follow-ups only when material.
