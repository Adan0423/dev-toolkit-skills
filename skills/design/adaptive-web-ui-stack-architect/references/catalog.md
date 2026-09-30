# Adaptive UI Technology Catalog

This catalog is a routing index, not a popularity ranking. Verify current framework/version support and licensing from official sources before a consequential selection.

## Utility-first / atomic / low-level styling
- Tailwind CSS
- UnoCSS
- Master CSS
- Bootstrap utilities when Bootstrap is already the project foundation

## Static / zero-runtime styling and design-token engines
- Panda CSS
- StyleX
- Vanilla Extract

## Runtime CSS-in-JS (use only when project architecture benefits)
- Emotion
- styled-components

## Headless / unstyled primitives
- Radix Primitives (React)
- Base UI (React)
- Headless UI (React/Vue)
- React Aria / React Spectrum primitives
- Ark UI (React/Solid/Vue/Svelte)
- Ariakit (React)
- Kobalte (Solid)
- Bits UI (Svelte)
- Melt UI (Svelte, verify current status before new adoption)

## React / Next component ecosystems
- shadcn/ui (copy-owned; inspect whether project uses Base UI or Radix primitives)
- HeroUI
- daisyUI
- Park UI
- MUI / Material UI
- Ant Design
- Mantine
- Chakra UI
- Blueprint
- PrimeReact
- Tremor for data/dashboard-oriented UI when appropriate
- specialized visual component collections such as Magic UI / Aceternity UI only for targeted high-impact sections, not as default application architecture

## Vue / Nuxt
- Vuetify
- PrimeVue
- Nuxt UI
- Element Plus
- Quasar
- Naive UI

## Angular
- Angular Material
- PrimeNG
- NG-ZORRO
- Taiga UI

## Svelte / SvelteKit
- Bits UI
- Flowbite Svelte
- Skeleton
- Svelte Material UI (verify maintenance/framework compatibility)

## Web Components / multi-framework
- Web Awesome (successor ecosystem related to Shoelace; verify package path/current status)
- Spectrum Web Components
- FAST / FAST Element ecosystem (verify current project status before new adoption)
- Lion Web Components

## Classic CSS frameworks
- Bootstrap
- Bulma
- Foundation
- UIkit
- Pico CSS
- Pure.css

## Enterprise design systems
- Carbon Design System
- Fluent UI
- Polaris
- Lightning Design System
- Adobe Spectrum

## Icons
- Lucide
- Phosphor
- Material Symbols / MUI Icons when aligned with Material
- Ant Design Icons when already using Ant Design
- Carbon Icons when already using Carbon
- Fluent icons when already using Fluent
- Iconify when broad multi-pack access is required, while enforcing one visual family per product surface

## Animation / interactions
- CSS transitions/animations first for simple effects
- Motion for React/JavaScript/Vue when state/layout/gesture animation warrants a library
- GSAP for complex timelines, scroll choreography, SVG or advanced animation control
- Lenis only when deliberate smooth-scroll behavior is a product requirement; never as decorative default

## 2D/3D
- Three.js for WebGL/WebGPU 3D experiences
- PixiJS for high-performance 2D rendering
- Spline embeds/components for authored 3D experiences when product workflow accepts an external design tool/runtime

## Specialized categories to evaluate when needed
### Forms
Use framework-native forms or an established form library only when complexity justifies it. Evaluate schema validation separately from form state.

### Data grids
For large editable/virtualized datasets, evaluate dedicated grid libraries instead of forcing a generic Table component.

### Charts
Choose chart libraries based on interaction, accessibility, rendering model, SSR needs, volume, theming, and bundle constraints.

### Editors
Rich text/code editors are specialized subsystems. Do not implement them from generic UI components if robust editing behavior is required.
