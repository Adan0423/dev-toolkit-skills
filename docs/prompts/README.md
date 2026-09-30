# Prompts Disponibles

> 4 prompts reutilizables para tareas recurrentes de creación, organización, auditoría y documentación.

## Prompts Meta (Creación y Organización)

### `meta/prompt-skill-creator.md`
- **Propósito:** Guiar paso a paso la creación de una nueva skill (`SKILL.md`, estructura, casos de uso, triggers).
- **Cuándo usarlo:** Cuando identifiques un patrón reutilizable que merece convertirse en skill.
- **Funciones:** Entrevista estructurada → definición de `name/description` → casos de prueba → generación del archivo SKILL.md siguiendo convenciones.
- **Entornos:** Cualquiera (multi-entorno). Ideal para workflows de estandarización de skills.

### `meta/prompt-organizar-skills-repo.md`
- **Propósito:** Analizar proyectos existentes y extraer skills candidatas para centralizarlas.
- **Cuándo usarlo:** Limpieza de repositorios, migración de utilidades a skills, consolidación.
- **Funciones:** Detección de patrones repetidos, clasificación por categorías, propuesta de naming (kebab-case), evaluación de reutilizabilidad.
- **Entornos:** Multi-proyecto / análisis transversal.

## Prompts de Auditoría

### `audit/prompt-auditoria.md`
- **Propósito:** Auditoría full-stack integral (arquitectura, UX, seguridad, rendimiento, operativa, deuda técnica).
- **Cuándo usarlo:** Revisiones de código/sistema completas, pre-release, due diligence técnica.
- **Funciones:** Checklist estructurado, hallazgos priorizados (Crítico/Alto/Medio/Bajo), recomendaciones accionables con ejemplos, riesgos y mitigaciones.
- **Entornos:** Web, Backend, APIs, Mobile, Desktop (multi-entorno).

## Prompts de Documentación

### `docs/prompt-mejorar-readme.md`
- **Propósito:** Sincronizar README.md y documentación con los cambios reales del código/repo.
- **Cuándo usarlo:** Antes de commits/releases, al añadir features, tras refactors importantes.
- **Funciones:** Análisis de diff/estructura → detectar docs desincronizados → proponer README actualizado (verdadero, basado en evidencia) → mantener consistencia entre archivos.
- **Entornos:** Cualquier repositorio (multi-entorno).

## Instalación/Uso

Estos prompts son archivos Markdown planos. Pueden invocarse directamente:

```text
"Carga y ejecuta prompts/meta/prompt-skill-creator.md para crear una skill para X"
```

O copiarse al contexto del agente según tu flujo de trabajo. No requieren empaquetado `.skill/.zip`.