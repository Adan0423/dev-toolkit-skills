# Framework integration

Preserve the framework's conventions.

## React / Next.js

- Keep class strings statically detectable.
- Extract repeated UI into components.
- Be careful with server/client theme toggles and hydration.
- Choose the official Tailwind integration supported by the framework's current toolchain.

## Vue / Nuxt

- Prefer utilities directly in templates.
- If scoped `<style>` blocks require Tailwind features, use `@reference` appropriately.
- Avoid mixing large amounts of component-scoped CSS with Tailwind without a reason.

## Svelte / SvelteKit

- Prefer utilities in markup.
- Use `@reference` for isolated style blocks that must access theme/custom Tailwind constructs.

## Laravel / Blade / server templates

- Ensure source detection includes real template locations.
- Avoid dynamic class fragments generated in ways Tailwind cannot detect.

## Monorepos / shared UI packages

- Explicitly register external/shared sources when they are ignored by default.
- Share theme CSS rather than duplicating tokens.
