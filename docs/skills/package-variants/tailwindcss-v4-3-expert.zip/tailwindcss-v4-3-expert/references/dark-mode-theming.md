# Tailwind CSS v4.3 — Dark Mode & Theme Architecture Standard

## Objective

Treat dark mode as a first-class product requirement, not a late cosmetic inversion. Every interface that supports theming must remain readable, accessible, coherent, and responsive in light mode, dark mode, and system-controlled mode across mobile, tablet, desktop, and wide screens.

## Supported strategies

Choose the strategy from product requirements and existing architecture; do not hard-code one globally without analysis.

### 1. System preference (default Tailwind behavior)

Tailwind's `dark:` variant targets `prefers-color-scheme: dark` by default. Use this when the product should simply follow the operating system/browser preference and no manual theme selector is required.

```html
<div class="bg-white text-slate-950 dark:bg-slate-950 dark:text-slate-50">
  ...
</div>
```

### 2. Manual class selector

When the user must explicitly choose a theme, define the dark variant using a selector:

```css
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));
```

Then apply the theme at the document root:

```html
<html class="dark">
```

Do not scatter theme-state classes throughout the application. Prefer one root source of truth.

### 3. Data-attribute selector

Use a data attribute when it better fits an existing theme system or design-system API:

```css
@import "tailwindcss";

@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

```html
<html data-theme="dark">
```

Do not mix `.dark` and `[data-theme=dark]` unless integration constraints clearly require both.

### 4. Three-way theme: light / dark / system

For products with a theme control, prefer the semantic model:

```text
light | dark | system
```

Behavior:

- `light`: force light theme;
- `dark`: force dark theme;
- `system`: follow `prefers-color-scheme` and react to OS changes where the application architecture supports it.

Persist an explicit user preference in an appropriate client or server store. Do not persist `system` as an accidentally resolved light/dark value; preserve the user's actual choice.

## Flash-of-wrong-theme prevention

Avoid a visible light→dark or dark→light flash during page startup.

When the theme is client-controlled:

1. Resolve the saved/system theme before first paint when practical.
2. Apply the root class/attribute as early as the framework allows.
3. In SSR frameworks, prefer server-provided theme state when available and safe.
4. Avoid hydration mismatches caused by rendering one theme on the server and immediately replacing it on the client.

Do not add blocking JavaScript blindly. Use the framework's established theming/SSR pattern when one exists.

## Color-scheme integration

Use Tailwind `scheme-*` utilities when native browser controls should match the active theme:

```html
<html class="scheme-light dark:scheme-dark">
```

This is especially important for native form controls such as date inputs, scrollable controls, and browser-rendered UI. `color-scheme` complements visual theme classes; it does not replace them.

## Semantic theme tokens

Prefer semantic tokens over scattering literal palette choices through every component.

Conceptual token model:

```text
surface
surface-muted
surface-elevated
text
text-muted
border
brand
brand-foreground
success
warning
danger
focus-ring
```

The concrete implementation can use Tailwind theme variables, CSS custom properties, or an existing design-system token layer. Preserve the project's current token architecture when it is coherent.

Dark mode is not simply `white → black`. Tune surfaces, borders, muted text, shadows, overlays, charts, syntax highlighting, images, and interactive states independently.

## Component requirements

For every reusable component, verify both themes for:

- background/surface;
- primary and secondary text;
- borders/dividers;
- icons;
- hover, focus-visible, active, selected, disabled;
- error/success/warning/info states;
- overlays, dialogs, popovers, drawers, menus, tooltips;
- input placeholder, autofill, validation, and native controls;
- shadows/rings that remain visible against dark surfaces;
- code blocks and syntax highlighting;
- charts/data visualizations;
- skeleton/loading states.

Do not ship components that are only partially themed.

## Responsive + dark mode interaction

Dark mode must pass the same adaptive requirements as light mode. Test both themes through continuous resizing.

At minimum verify both light and dark at representative ranges:

- narrow mobile;
- large mobile;
- tablet portrait/landscape;
- compact laptop;
- desktop;
- very wide desktop.

A layout that is responsive in light mode but clips, loses borders, obscures controls, or becomes unreadable in dark mode is a failed responsive implementation.

## Accessibility

Dark mode must preserve accessibility rather than merely reduce luminance.

Verify:

- text/background contrast;
- focus-visible indicators;
- disabled state distinction;
- error/success meaning not conveyed by color alone;
- `contrast-more` and `forced-colors` behavior where applicable;
- reduced-motion behavior independent of theme;
- readable links and interactive affordances;
- charts/graphs with non-color-only differentiation where needed.

Avoid pure-black/pure-white defaults by habit if they create excessive glare or contrast for the product; choose colors based on the design system and accessibility checks.

## Media, images, logos, and assets

When assets differ by theme:

- prefer one asset when it remains legible in both themes;
- otherwise use intentional light/dark variants;
- ensure logos do not disappear against a surface;
- verify transparent PNG/SVG artwork against both backgrounds;
- do not apply blanket CSS inversion to product imagery or brand assets;
- test screenshots, charts, maps, and embedded content independently.

## Theme toggle UX

If the product includes a theme selector:

- make it keyboard accessible;
- expose a clear accessible name;
- reflect current state visibly and semantically;
- use `light`, `dark`, and `system` labels/icons consistently;
- do not make theme switching dependent on hover;
- ensure the control remains reachable on mobile navigation layouts.

## Anti-patterns

Do not:

- add `dark:` classes randomly without a token/system strategy;
- duplicate whole components only to support dark mode;
- force dark mode with JavaScript on every render;
- use `invert` on the entire application;
- use low-contrast gray-on-gray text;
- assume every `bg-white` should become `dark:bg-black`;
- theme only page backgrounds while leaving dialogs/forms/charts broken;
- support a manual toggle without persisting or restoring the user's explicit preference;
- introduce a second theme library if the project already has a coherent solution.

## Dark mode QA matrix

A themed task is incomplete until the following pass where applicable:

```text
[ ] Default/system theme behavior verified
[ ] Manual theme behavior verified when supported
[ ] Light / dark / system preference logic verified
[ ] No flash-of-wrong-theme on initial load where preventable
[ ] No hydration mismatch caused by theme resolution
[ ] Root color-scheme/native controls match active theme
[ ] All shared components checked in both themes
[ ] Hover/focus/active/selected/disabled states checked in both themes
[ ] Forms, dialogs, menus, popovers, tables, charts, code blocks checked
[ ] Mobile/tablet/desktop responsive behavior checked in both themes
[ ] Continuous resizing checked in both themes
[ ] Images/logos remain legible in both themes
[ ] Contrast/focus accessibility checked
[ ] No accidental theme-specific horizontal overflow or clipping
[ ] Theme preference persists correctly when product supports persistence
[ ] Build/lint/typecheck/tests pass
```

## Completion rule

Do not declare dark mode complete because a root background changes color. Complete it only when the entire product experience, reusable components, interaction states, native controls, responsive behavior, and accessibility remain coherent in every supported theme.
