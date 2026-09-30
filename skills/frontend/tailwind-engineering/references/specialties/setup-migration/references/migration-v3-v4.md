# Migration from Tailwind v3 to v4

Do not perform blind syntax replacement.

## Audit first

Check:

- `@tailwind base/components/utilities` directives;
- `tailwind.config.*` content/theme/plugins;
- safelists;
- custom plugins;
- `@apply` usage;
- preprocessors;
- unsupported browser requirements;
- third-party plugins/libraries tied to v3;
- dynamically generated class strings.

## v4 changes to account for

- Tailwind is imported with `@import "tailwindcss"`.
- CSS-first configuration with `@theme` is preferred.
- source detection is automatic by default.
- modern browser requirements are higher than v3.
- removed/deprecated utilities and changed defaults can cause visual regressions.

Use the official upgrade guide/tooling when applicable, then perform visual and functional verification.
