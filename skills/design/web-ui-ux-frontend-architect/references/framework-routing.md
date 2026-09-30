# Routing por framework

## React / Vite

Favorece features cohesivas, componentes reutilizables y lógica compartida en hooks/services cuando realmente se reutilice. Mantén componentes definidos en el nivel superior y divide archivos cuando mejore escaneabilidad/reutilización.

## Next.js

Respeta App Router/Pages Router del proyecto. No rompas server/client boundaries. Coloca componentes cerca de la ruta cuando sean específicos y eleva a shared UI solo cuando exista reutilización real.

## Vue / Nuxt

Usa componentes y composables coherentes con el proyecto. Respeta convenciones de auto-import y estructura Nuxt si existen.

## Angular

Prefiere organización por features/áreas funcionales sobre carpetas globales por tipo cuando el proyecto lo permita. Mantén servicios, componentes y tests cerca de su feature cuando mejore ownership.

## Svelte / SvelteKit

Respeta routing y convenciones de `src/routes`. Extrae componentes/stores/utilidades por cohesión, no por tamaño arbitrario.

## Laravel / Blade, Django, ASP.NET

Respeta templates/layouts/partials/components del framework. No introduzcas SPA/framework JS si no es necesario. Extrae UI repetida usando mecanismos nativos.
