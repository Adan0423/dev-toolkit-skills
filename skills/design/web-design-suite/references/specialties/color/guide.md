---
name: color-palette-studio
description: >-
  Elige, aplica y revisa paletas de color para interfaces web, apps y contenido visual;
  convierte colores de marca o referencias en tokens, estados y temas claro/oscuro
  con contraste comprobado. Úsalo al crear un sistema de color o corregir su aplicación.
---

# Especialidad: color

Procedencia: `skills/design/color-palette-studio/SKILL.md`. Guía derivada; editar fuente y reconstruir, no esta copia.

Aplica el procedimiento solo al modo seleccionado. Las preferencias del usuario, alcance y contrato común de la familia delimitan sus recomendaciones. No invoca otras skills por defecto.

# Color Palette Studio

Parte del proyecto: marca, audiencia, tarea, componentes, tokens y temas existentes.
Trabaja en español salvo preferencia. No cambia una identidad aprobada por gusto ni
exige investigación extensa para corregir el contraste de un botón.

## Selección de guía

| Necesidad | Leer |
|---|---|
| Elegir paleta, adaptar Color Hunt o construir dirección de color | [Selección y roles](references/palette-selection.md) |
| Contraste, estados, daltonismo y comprobaciones | [Accesibilidad](references/accessibility.md) |
| CSS, tokens, frameworks/CMS y temas claro/oscuro/sistema | [Implementación](references/implementation.md) |
| Categorías, escalas y colores en gráficos | [Visualización de datos](references/data-visualization.md) |

Carga una guía primero y añade otra solo cuando la tarea lo necesite. Una consulta
de colores devuelve una propuesta útil; no añade modo oscuro a un proyecto por una
petición de cambiar un color. Si crea un sistema de temas, define ambos de forma coherente.

## Trabajo del agente

1. Inspecciona sistema y alcance. Si no hay paleta, usa referencias verificables y
   recomienda una dirección con roles y motivo; opciones solo si ayudan a decidir.
2. Separa colores primitivos de roles: fondo/superficie, texto, borde funcional,
   acción/on-action, enlace, focus y estados. Ajusta cada pareja que se use realmente.
3. Implementa en el mecanismo existente (variables, theme, estilos globales o tokens
   nativos). Conserva rutas, lógica, tamaño/layout y marca fuera del alcance solicitado.
4. Verifica pares afectados, estados y componentes reales en temas/placements pertinentes.
   No declara accesibilidad por inspección visual, uso de OKLCH o una paleta popular.

El color no es el único indicador de error, selección o serie. Preserva etiquetas,
iconos, foco y otras señales. No sustituye texto legible por una estética de baja opacidad.

## Recursos y verificación

[Ejemplo de paleta](assets/palette-example.json) y [CSS derivado](assets/tokens-example.css)
son adaptación propia de una referencia Color Hunt, no una paleta universal obligatoria.
[Contrato y herramienta](references/tool-contract.md): `scripts/contrast_audit.py`
calcula pares sRGB opacos y genera CSS desde el JSON; no inspecciona el DOM.

Sin navegador o tooling puede entregar tokens, matriz de contraste y cambios preparados;
marca la comprobación visual pendiente. No instala plugins ni publica cambios externos
por pedir una paleta. Si un CMS/MCP está conectado, confirma sitio/entorno y autorización
antes de aplicar; acceso a diseño no presupone permiso de publicación.

Entrega paleta con procedencia, tabla rol/valor por tema, combinaciones comprobadas,
código o configuración y límites. Usa [plantilla de entrega](assets/palette-handoff.md)
cuando aporte. [Fuentes investigadas](references/research-sources.md).
