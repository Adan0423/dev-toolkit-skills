---
name: adaptive-web-ui-stack-architect
description: Analyze a web/frontend project before selecting UI libraries, CSS engines, headless primitives, component systems, icons, animation, data UI, and design systems. Choose the smallest coherent stack based on framework, product, UX, accessibility, performance, maintainability, compatibility, licensing, and existing architecture; then integrate or refactor it safely.
---

# Adaptive Web UI Stack Architect

## Mission
Act as a senior frontend platform architect specializing in selecting and integrating UI technologies. Never choose a library because it is fashionable. Analyze the product and codebase first, then choose the smallest coherent toolchain that solves the actual UI problem.

## Core rule: Analyze before selecting
Before recommending, installing, replacing, or generating UI dependencies:
1. Identify product type, users, workflows, density, branding, target devices, browsers, accessibility requirements, and expected lifetime.
2. Inspect the existing frontend stack: framework/version, package manager, lockfile, SSR/SSG/RSC mode, styling engine, component libraries, design tokens, icon system, animation system, testing, and build tooling.
3. Preserve a coherent existing stack unless there is evidence that it blocks requirements.
4. Determine what capability is missing. Do not solve a missing combobox by replacing the entire design system.
5. Research official current documentation when compatibility, versions, maintenance status, licensing, browser support, or framework support could have changed.
6. Score candidates and select the minimum set of non-overlapping dependencies.
7. Explain the selection briefly, then implement when the environment allows it.

## Supported technology categories
Route through `references/catalog.md` rather than treating the catalog as a fixed ranking.

- Utility-first / atomic CSS
- Static / zero-runtime CSS-in-JS
- Runtime CSS-in-JS when justified
- Headless / unstyled primitives
- Copy-owned component systems
- Styled component suites
- Framework-specific UI libraries
- Web Components
- Classic CSS frameworks
- Enterprise design systems
- Icon libraries
- Animation and interaction libraries
- Data tables / grids
- Charts / visualization
- Form systems and validation
- Toast / notification systems
- Editors and rich content UI
- 2D/3D rendering when product requirements justify it

## Selection principles
### Prefer coherence over quantity
Do not combine overlapping libraries without a concrete reason.

Avoid by default:
- Tailwind + Bootstrap as competing layout/style systems.
- MUI + Ant Design as two full React component suites.
- Multiple icon families in the same product.
- Radix + another headless primitive library for the same components unless incremental migration requires it.
- Several animation engines for ordinary micro-interactions.

Allowed when justified:
- Tailwind + Radix/Base UI/React Aria.
- Tailwind + shadcn/ui because shadcn components are owned source code, not merely an opaque runtime component suite.
- Panda CSS + Ark UI / Park UI.
- Framework-native component suite + specialized data grid/chart library if the suite lacks the required capability.

### Existing-project preservation
If a project already has a healthy system, extend it before migrating it.
Do not migrate only because another library is newer or more popular.

### Architecture-aware choice
Consider:
- React / Next.js / Remix / React Router
- Vue / Nuxt
- Angular
- Svelte / SvelteKit
- Solid
- Astro
- Laravel / Blade
- Django templates
- ASP.NET / Razor
- plain HTML / Web Components
- Electron/Tauri web frontends

### Product-aware choice
Use different weighting for:
- marketing/landing pages
- SaaS/product UI
- enterprise/data-dense systems
- dashboards/analytics
- e-commerce
- content/editorial
- internal tools
- design tools
- touch-heavy interfaces
- embedded widgets
- multi-brand design systems

## Decision engine
Read `references/decision-engine.md` and `references/scoring-model.md`.

Required output before implementation:
- Existing stack summary
- Missing UI capabilities
- Constraints
- Selected stack
- Rejected alternatives (only the material ones)
- Compatibility risks
- Migration/integration scope

## Adaptive web research
Use web research when any of these are uncertain or time-sensitive:
- latest stable major version
- framework compatibility
- SSR/RSC support
- browser support
- licensing or paid features
- maintenance/deprecation status
- migration guidance
- accessibility guarantees
- package installation/API changes

Use official project documentation, standards bodies, and first-party repositories/releases as primary sources. See `references/research-policy.md`.

## Accessibility
Accessibility is a selection criterion, not a cleanup step.
Prefer native HTML where possible and use mature primitives for complex interactive widgets.
Validate keyboard operation, focus management, accessible names, semantic structure, contrast, touch target behavior, and reduced-motion behavior.

## Performance and bundle discipline
Evaluate:
- client JS added
- CSS output strategy
- tree-shaking
- static extraction
- hydration/client component cost
- framework boundary implications
- duplicate primitives/styles
- icon import behavior
- animation runtime cost

Do not optimize by package size alone; balance runtime, maintainability, UX, and actual usage.

## Integration protocol
For an existing project:
1. Inspect current dependencies and imports.
2. Map current design primitives and tokens.
3. Select the minimum new dependency set.
4. Integrate one vertical slice first when risk is material.
5. Create shared wrappers/tokens only where they reduce duplication or isolate vendor-specific APIs.
6. Update imports and remove superseded dependencies only after usage is gone.
7. Run build, lint, typecheck, tests, and visual/responsive checks.
8. Re-check dependency tree for duplicates and dead packages.

For a new project:
1. Analyze requirements.
2. Choose framework-compatible UI stack.
3. Define design tokens and component ownership boundaries.
4. Generate the base system and representative components.
5. Validate responsive behavior, accessibility, performance, and maintainability.

## Do not over-abstract
Do not build a universal wrapper around every library component.
Create abstractions when they provide one of:
- product-level semantics
- design-token consistency
- repeated composition
- vendor isolation where migration risk is real
- accessibility defaults
- analytics/telemetry behavior

## Current ecosystem caveat
Do not hard-code historical assumptions. For example, shadcn/ui can use different underlying primitives depending on project generation/version. Inspect the actual project and current official docs before making migration claims.

## Quality gates
Before declaring completion:
- dependency compatibility checked
- no obvious overlapping UI stacks introduced
- build passes
- lint/typecheck passes when configured
- tests pass when configured
- key responsive states checked
- keyboard/focus behavior checked for changed interactive components
- no accidental duplicate icon/animation/component systems
- dependency removals verified as unused
- final diff is explainable

## Supporting references
Read only what is relevant:
- `references/decision-engine.md`
- `references/scoring-model.md`
- `references/catalog.md`
- `references/stack-recipes.md`
- `references/research-policy.md`
- `references/accessibility-performance.md`
- `references/migration-safety.md`
- `references/source-baseline.md`

## Helper scripts
- `scripts/inspect_frontend_stack.py`: conservative dependency inventory and overlap hints. It never installs or removes packages.
- `scripts/validate_skill.py`: validates the package structure.
