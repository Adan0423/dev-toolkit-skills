---
name: tailwind-engineering
description: >-
  Configura, migra y depura Tailwind CSS con selección de especialidad para instalación,
  integración, tokens/dark mode, shadcn o consulta de documentación. Úsalo para problemas
  del sistema CSS Tailwind y adapta instrucciones a la versión y framework instalados.
---

# Tailwind Engineering

Inspecciona versión, framework, build, archivos CSS/config y componentes existentes.
Trabaja en español salvo otra necesidad. No supone Tailwind v4.3 por el nombre de una
fuente ni prescribe instalación nueva si basta corregir una regla.

| Necesidad | Guía |
|---|---|
| Instalación, integración con framework, migración o detección de clases | [setup-migration](references/specialties/setup-migration/guide.md) |
| Paleta/tokens, temas, variables semánticas y claro/oscuro | [theming](references/specialties/theming/guide.md) |
| Integrar o reparar shadcn con Tailwind/Vite/React | [shadcn](references/specialties/shadcn/guide.md) |
| Consultar utilidad, variante o documentación, sin cambios innecesarios | [documentation](references/specialties/documentation/guide.md) |

Lee una sola guía inicial. Para una migración lee únicamente referencias del framework
y versión relevantes; no instalación de todos los frameworks. Dark mode no implica
añadir shadcn. Un error de alias/componentes shadcn no es una migración automática.
Las guías son procedimientos internos con recursos relativos a su carpeta; no commands
ni skills registrados. Verifica versiones/APIs con fuente oficial vigente al actuar.

Conserva design system existente. Resuelve clases, orden/cascada, imports, source
detection y variables con evidencia antes de añadir overrides. No confunde cambiar
tokens con rediseñar todo el producto. Claro/oscuro/sistema cuando requerido: prueba
contraste, persistencia, formularios y assets, no solo un selector.
Comprueba build, salida CSS y página real responsive cuando se cambie UI. Entrega
guía usada, archivos, prueba y límites. No promete compatibility por compilar CSS.
