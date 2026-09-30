# Accessibility and Performance Gates

## Accessibility
For interactive primitives verify:
- semantic element choice
- accessible names/descriptions
- keyboard navigation
- visible focus
- focus trapping/restoration where appropriate
- screen-reader semantics
- touch/pointer usability
- reduced motion

Headless libraries reduce implementation burden but do not make application composition automatically accessible.

## Performance
Evaluate:
- CSS emitted at build time vs runtime styling
- client-side JavaScript added
- tree-shaking and modular imports
- duplicate dependency versions
- SSR/hydration effects
- icon import granularity
- animation runtime
- large grid/editor/chart subsystems

Do not reject a library merely for having a larger package if it replaces substantial bespoke code and only used modules ship.
