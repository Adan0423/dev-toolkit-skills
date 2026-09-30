# Migration Safety

## Never perform a blind UI-library migration
Before removing a library:
1. search imports
2. search dynamic references and aliases
3. inspect theme providers and global CSS
4. inspect tests/stories/examples
5. inspect SSR/app providers
6. replace usage in bounded slices
7. build and test
8. only then remove dependency and lockfile entries

## Styling migration
Watch for:
- reset/preflight behavior
- CSS variables
- portal stacking/z-index
- focus rings
- typography defaults
- form normalization
- dark mode implementation
- specificity/order changes

## shadcn-specific
Inspect component source and `components.json`/project configuration where available. Do not infer primitive implementation from the `shadcn/ui` label alone.
