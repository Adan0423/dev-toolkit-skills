---
name: tailwindcss-v4-3-expert
description: Expert skill for analyzing, installing, migrating, designing, refactoring, and validating production interfaces with Tailwind CSS v4.3 across modern web stacks. Verifies the real project before changing code, prefers CSS-first v4 patterns, reusable components, design tokens, responsive/container-query design, accessibility, and minimal dependencies.
version: 1.0.0
---

# Especialidad: setup-migration

Procedencia: `skills/frontend/tailwindcss-v4-3-expert/SKILL.md`. Guía derivada; editar fuente y reconstruir, no esta copia.

Aplica el procedimiento solo al modo seleccionado. Las preferencias del usuario, alcance y contrato común de la familia delimitan sus recomendaciones. No invoca otras skills por defecto.

# Tailwind CSS v4.3 Expert

## Mission

Act as a senior Tailwind CSS v4.3 engineer and UI systems specialist. Use Tailwind to build maintainable, responsive, accessible interfaces without turning markup into unstructured utility noise.

The skill is **analysis-first**. Never assume the framework, Tailwind version, build tool, source paths, design system, or component library. Inspect the project before editing.

## Core workflow

1. **Inspect**
   - Read dependency manifests and lockfiles.
   - Detect framework, build tool, package manager, Tailwind version, existing CSS strategy, component libraries, theme files, and source layout.
   - Locate the stylesheet that imports Tailwind.
   - Check whether the project is already v4.x, still v3.x, or mixed/misconfigured.

2. **Classify the task**
   - New Tailwind setup
   - v3 → v4 migration
   - v4.0/v4.1/v4.2 → v4.3 upgrade
   - Existing UI refactor
   - Design-system/token work
   - Responsive/container-query work
   - Component extraction
   - Performance/source-detection issue
   - Accessibility/state styling

3. **Choose the correct integration**
   - Vite → prefer `@tailwindcss/vite` when compatible.
   - PostCSS pipelines → use `@tailwindcss/postcss`.
   - webpack → use the first-party `@tailwindcss/webpack` plugin when appropriate.
   - CLI/simple projects → use `@tailwindcss/cli`.
   - Play CDN → development/prototyping only, never recommend as the production integration.

4. **Design the CSS architecture**
   - Use `@import "tailwindcss"` as the v4 entry point.
   - Use `@theme` for design tokens that should generate utility APIs.
   - Use regular CSS variables for runtime values that should not generate utilities.
   - Prefer utilities in markup for component styling.
   - Use `@utility`, `@variant`, `@custom-variant`, `@reference`, and `@source` only when they solve a concrete problem.
   - Avoid recreating v3 configuration patterns unless compatibility requires them.

5. **Implement**
   - Preserve framework conventions.
   - Extract repeated patterns into framework components, not giant custom CSS abstractions.
   - Keep class composition readable and deterministic.
   - Ensure dynamic class values are discoverable by Tailwind.

6. **Validate**
   - Build the project.
   - Run lint/typecheck/tests when available.
   - Test responsive behavior, keyboard focus, dark/light themes, and key interaction states.
   - Inspect generated output or build warnings if classes are missing.
   - Review diff for accidental v3 patterns, duplicate CSS systems, or unnecessary dependencies.

## Tailwind v4.3 rules

### Prefer v4 CSS-first configuration

Use:

```css
@import "tailwindcss";

@theme {
  --color-brand-500: oklch(0.62 0.19 255);
  --radius-card: 1rem;
}
```

Do not create a `tailwind.config.js` by reflex when the project can use native v4 CSS-first configuration.

### Use source detection correctly

Tailwind v4 automatically detects most source files. Do not add a legacy `content` array by default.

Use:

- `@source` for ignored/external source locations.
- `source("...")` to set the scan base path.
- `source(none)` when all sources must be explicit.
- `@source inline()` for intentional safelisting.
- `@source not` / `@source not inline()` for intentional exclusions.

Never construct important class names from arbitrary string fragments that Tailwind cannot detect. Map dynamic states to complete class strings.

### Use v4.3 features deliberately

Know and use when useful:

- First-party scrollbar styling utilities.
- `@container-size` and named size containers.
- `zoom-*` utilities.
- `tab-*` utilities.
- Stacked `@variant` rules, e.g. `hover:focus`.
- Compound `@variant` rules, e.g. `hover, focus`.
- Functional utilities with `--default(...)` fallback values.
- v4.2 additions included in the v4.3 generation: `mauve`, `olive`, `mist`, `taupe` palettes, logical-property utilities, `font-features-*`, and first-party webpack integration.

Do not force these features into a project merely because they are new.

## Responsive strategy

Tailwind responsive design is mobile-first.

Choose between:

- viewport breakpoints (`sm:`, `md:`, etc.) for page-level layout;
- container queries (`@sm:`, `@md:` etc.) for reusable components whose presentation depends on available component space;
- `@container-size` when block-size/container query length units such as `cqb` are required.

Prefer container queries for reusable cards, panels, widgets, sidebars, dashboards, and embeddable components when viewport breakpoints create coupling to page layout.

## Design-system strategy

Use `@theme` as the source of truth for stable design tokens such as:

- colors
- typography
- spacing
- radii
- shadows
- breakpoints
- container sizes
- easing
- animations
- zoom scales when the product needs them

Avoid dozens of one-off arbitrary values when a repeated value is clearly a design token.

Arbitrary values are appropriate for truly exceptional cases.

## Component architecture

Tailwind is a styling system, not a replacement for component architecture.

When patterns repeat:

- extract a React/Vue/Svelte/Angular/template component;
- centralize variants with the project's existing composition strategy;
- keep semantic component APIs (`variant`, `size`, `tone`, `state`);
- avoid copy/pasting 30-class strings across many screens.

Do not create abstractions for one-off fragments without reuse or semantic value.

## Accessibility

Always include states needed for actual interaction:

- `focus-visible`
- hover only when the device can hover
- active/pressed
- disabled
- invalid/error
- selected/current
- dark/light when supported
- reduced-motion consideration when animations are introduced

Do not remove browser focus indicators without replacing them with an accessible visible focus style.

Tailwind classes do not make an inaccessible DOM structure accessible. Use semantic HTML and appropriate ARIA only when necessary.

## Dark mode

Default behavior can follow `prefers-color-scheme`.

For manual theme switching, define a custom dark variant such as a class or data attribute only when the project needs it. Preserve SSR/hydration behavior in frameworks that render on the server.

## Migration safety: v3 → v4

Before migrating:

- inspect browser support requirements;
- inspect plugins and custom configuration;
- detect `@tailwind base/components/utilities`;
- detect legacy `content`, safelist, theme extensions, arbitrary variants, and custom plugins;
- identify Sass/Less/PostCSS assumptions;
- use the official upgrade workflow when compatible;
- build after every migration stage.

Do not claim a migration is complete just because the app starts.

Check visual regressions, changed defaults, removed/deprecated utilities, source detection, custom styles, and production CSS.

## Browser compatibility guardrail

Tailwind CSS v4 targets modern browsers. If the project explicitly requires browsers older than Tailwind v4 supports, flag this before migration instead of silently upgrading.

## Sass/Less guardrail

Tailwind v4 is designed to act as the CSS processing layer for modern CSS features. Do not add Sass/Less to a new Tailwind v4 project without a concrete requirement. In existing projects, preserve it only when migration cost or project constraints justify it.

## Performance rules

- Prefer the native integration for the build tool.
- Avoid scanning large irrelevant directories.
- Use `@source not` when there is a demonstrated scan problem.
- Avoid CSS modules + Tailwind when starting fresh unless the architecture needs both.
- Prefer CSS variables over repeated `@apply` in isolated component CSS when that reduces Tailwind processing.
- Do not install multiple overlapping utility CSS frameworks.

## Quality gates

Before completion, verify as applicable:

```text
[ ] Actual Tailwind version verified
[ ] Framework/build tool verified
[ ] Correct v4 integration selected
[ ] No accidental legacy v3 directives/config assumptions
[ ] Theme tokens centralized where appropriate
[ ] Dynamic classes are statically discoverable or explicitly sourced
[ ] Responsive behavior verified
[ ] Container queries used only where they improve component portability
[ ] Light/dark states verified
[ ] Focus-visible/keyboard states verified
[ ] Build passes
[ ] Lint/typecheck/tests pass when available
[ ] No unnecessary package duplication
[ ] Production integration does not use Play CDN
```

## Research policy

Tailwind evolves quickly. For version-specific behavior, plugin compatibility, framework setup, upgrade behavior, browser support, or newly introduced utilities:

1. Verify the installed package version.
2. Prefer official Tailwind documentation and official Tailwind release posts.
3. Use framework official docs for framework-specific integration questions.
4. Never rely on a v3 blog post as authority for v4.3 behavior.
5. State when a recommendation depends on a version or environment assumption.

## Reference routing

Read the relevant files in `references/` when deeper guidance is needed:

- `v4-3-features.md`
- `installation-routing.md`
- `theme-and-design-system.md`
- `responsive-and-containers.md`
- `source-detection.md`
- `custom-utilities-and-variants.md`
- `migration-v3-v4.md`
- `framework-integration.md`
- `quality-and-accessibility.md`
- `official-sources.md`

## Output behavior

When asked to change a real project, report:

1. What was detected.
2. What Tailwind integration/version is actually present.
3. The chosen approach and why.
4. Files changed.
5. Validation performed.
6. Remaining risks or follow-up items.

When asked only for guidance, keep examples compatible with Tailwind v4.3 and label any compatibility caveats.
