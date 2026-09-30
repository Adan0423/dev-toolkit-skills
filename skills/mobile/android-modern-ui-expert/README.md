# Android Modern UI Expert — instalación

Skill personalizada para Android Studio/agents enfocada en crear, modernizar y revisar interfaces Android modernas con Kotlin y Jetpack Compose.

## Contenido

- `SKILL.md`: instrucciones principales de la skill.
- `references/source-map.md`: documentación oficial Android/Kotlin usada como base.
- `references/ui-quality-gates.md`: checklist de calidad y validación.
- `assets/ui-audit-template.md`: plantilla para auditorías/rediseños de UI.

## Instalación recomendada en Android Studio

La documentación actual de Android Studio admite skills en carpetas de proyecto o usuario como:

```text
.agents/skills/android-modern-ui-expert/
```

o:

```text
.android-studio/skills/android-modern-ui-expert/
```

Copia la carpeta completa `android-modern-ui-expert` dentro de una de esas ubicaciones.

Ejemplo:

```text
<tu-proyecto>/
  .agents/
    skills/
      android-modern-ui-expert/
        SKILL.md
        references/
        assets/
```

Después puedes invocarla desde el chat/agente de Android Studio con una tarea relacionada o, cuando el IDE lo permita, mediante `@android-modern-ui-expert`.

## Ejemplos de uso

- "Moderniza esta pantalla con Jetpack Compose y Material 3 sin cambiar la lógica existente."
- "Haz que toda la navegación y el layout sean adaptativos para móvil, tablet, plegable y ventanas grandes."
- "Revisa el dark mode, edge-to-edge y accesibilidad de este proyecto."
- "Crea una pantalla nueva siguiendo el design system actual y agrega previews y pruebas de UI."
- "Analiza primero este proyecto KMP y decide qué UI debe permanecer específica de Android."

## Principio principal

La skill debe inspeccionar el proyecto antes de modificarlo. No debe adivinar dependencias, versiones, arquitectura, navegación ni estructura de módulos.
