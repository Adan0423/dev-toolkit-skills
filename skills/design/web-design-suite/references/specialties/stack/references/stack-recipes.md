# Example Stack Recipes

These are starting hypotheses, never automatic defaults.

## Highly customized React SaaS
- Tailwind or Panda CSS
- Base UI / Radix / React Aria depending interaction and accessibility needs
- copy-owned application components
- one icon family
- Motion only if interaction complexity requires it

## React enterprise/data-heavy
- Ant Design, MUI, Blueprint, PrimeReact, or Mantine based on widget requirements
- dedicated data grid if required
- use the suite's own theming and icons unless there is a strong brand reason not to

## Next.js branded product
- inspect RSC/client boundaries first
- prefer styling/component choices with documented compatibility
- copy-owned UI can reduce vendor lock-in, but increases maintenance ownership

## Vue/Nuxt product
- Nuxt UI for Nuxt-native workflow when requirements align
- PrimeVue/Vuetify/Element Plus/Quasar when broader styled suites are needed
- Ark UI for headless multi-framework design-system work

## SvelteKit custom design system
- Bits UI or Ark UI for primitives
- Tailwind/Panda/plain CSS depending architecture
- avoid importing React-centric solutions through wrappers

## Multi-framework design system
- evaluate Web Components or Ark UI-style multi-framework primitives
- centralize tokens independently of framework
- do not assume one runtime component API can be perfectly shared across all frameworks

## Simple content site
- semantic HTML + modern CSS or Pico/Bootstrap when speed and consistency matter
- avoid React-scale component dependencies without interaction needs
