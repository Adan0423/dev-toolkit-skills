# Custom utilities and variants

## @utility

Create custom utilities only for reusable low-level styling APIs.

## Functional utilities

Tailwind v4 supports functional utilities. In v4.3, default values can be supplied using `--default(...)` within `--value(...)`/`--modifier(...)` workflows.

## @variant

Apply Tailwind variants from CSS when custom CSS is the right layer.

v4.3 supports stacked and compound variants in CSS.

## @custom-variant

Use for semantic project-specific states such as a data-driven theme.

## @reference

Use when component-isolated CSS (CSS modules or Vue/Svelte style blocks) needs awareness of global theme/custom utilities/variants.

## @apply

Use sparingly. Prefer framework components and direct utilities for most reusable UI. `@apply` is appropriate for third-party overrides or unavoidable custom CSS that should reuse project tokens/utilities.
