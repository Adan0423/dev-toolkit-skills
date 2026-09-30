# Installation routing

Select integration after detecting the project's real build system.

## Vite

Prefer the first-party `@tailwindcss/vite` plugin when the framework supports normal Vite plugin integration.

CSS entry:

```css
@import "tailwindcss";
```

## PostCSS

Use `@tailwindcss/postcss` for frameworks/build systems where PostCSS is the supported path.

## webpack

Tailwind v4.2+ includes first-party webpack integration via `@tailwindcss/webpack`. Prefer it when webpack is the native project build system and compatibility is verified.

## CLI

Use `@tailwindcss/cli` for simple/static projects and build scripts where a standalone Tailwind compilation step is appropriate.

## Play CDN

Use only for prototyping/development demonstrations. Do not use it as the production setup.

## Never assume

Read package manifests, framework config, build scripts, and lockfiles first. Do not install Vite into a project merely because it is Tailwind's fastest integration.
