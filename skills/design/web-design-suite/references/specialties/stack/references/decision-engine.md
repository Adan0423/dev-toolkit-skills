# Decision Engine

## 1. Determine the problem class
Classify the requested capability:
- styling/layout
- accessible primitive behavior
- styled components
- enterprise/data density
- forms
- tables/grids
- charts
- icons
- animation
- 2D/3D
- cross-framework components
- full design system

Choose only categories required by the problem.

## 2. Detect existing constraints
Capture:
- framework and version
- SSR/SSG/RSC/client-only model
- package manager and lockfile
- TypeScript status
- CSS tooling/PostCSS/Sass
- current UI libraries
- current design tokens/theme
- browser targets
- accessibility requirements
- bundle/performance constraints
- team conventions
- licensing constraints

## 3. Preserve before replace
Prefer:
1. existing healthy capability
2. extension/plugin to existing system
3. focused new dependency
4. partial migration
5. full migration only when evidence supports it

## 4. Choose ownership model
- **Utility/low-level:** maximum visual control, more application-owned composition.
- **Headless:** library owns interaction/accessibility; app owns appearance.
- **Copy-owned:** source lives in project; app owns component evolution.
- **Styled suite:** vendor owns component API and much of visual behavior.
- **Enterprise design system:** stronger conventions and product consistency.

## 5. Detect conflicts
Flag:
- competing resets/preflight layers
- duplicated focus/dialog/menu primitives
- duplicated theme providers
- conflicting CSS-in-JS runtimes
- duplicate icon packs
- overlapping animation engines
- global CSS specificity conflicts
- server/client boundary incompatibilities

## 6. Choose and validate
Provide a primary choice and at most two serious alternatives when uncertainty matters. Do not dump a giant list.
