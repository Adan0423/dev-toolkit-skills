# Tarea: Actualizar README y documentación del proyecto

## Contexto
Analiza el proyecto completo (estructura de carpetas, package.json/requirements, 
código fuente, configuración) antes de escribir nada. No asumas tecnologías: 
verifícalas leyendo los archivos de dependencias reales.

## 1. README.md
Rediseña el README con:
- **Header**: nombre del proyecto, badges (build, license, versión, stack) usando shields.io
- **Descripción**: qué hace el proyecto, problema que resuelve, para quién es
- **Stack tecnológico**: tabla o lista con iconos (usar https://skillicons.dev o badges de shields.io) 
  agrupado por: Frontend / Backend / Base de datos / Infraestructura / Herramientas
- **Arquitectura**: diagrama simple (Mermaid) de cómo se conectan las piezas
- **Características principales**: bullets con emojis, enfocado en valor, no en implementación
- **Instalación y uso**: pasos numerados, comandos en bloques de código
- **Variables de entorno**: tabla con nombre, descripción, requerido/opcional
- **Estructura de carpetas**: árbol comentado de las carpetas clave
- **Roadmap / Estado**: enlace a PROGRESS.md o TODO.md
- **Licencia y contacto**

## 2. Documentación adicional a generar
Crea estos archivos si no existen, o actualízalos si existen:

- **docs/ARCHITECTURE.md**: decisiones técnicas, por qué se eligió cada tecnología, 
  diagramas de flujo de datos
- **docs/PROGRESS.md**: qué está implementado (✅), en progreso (🚧), pendiente (❌), 
  organizado por módulo/feature, con fecha de última actualización
- **docs/AGENTS.md**: si el proyecto usa agentes/skills de IA, documentar cada uno: 
  propósito, herramientas que usa, cuándo se dispara, inputs/outputs esperados
- **docs/SKILLS.md**: inventario de skills/capacidades del sistema, con ejemplos de uso
- **docs/TODO.md** o sección "Pendientes": lista priorizada de lo que falta 
  implementar, separando "crítico para MVP" vs "mejoras futuras"
- **CONTRIBUTING.md**: si es un proyecto colaborativo, cómo contribuir

## 3. Reglas de estilo
- Todo en [ESPAÑOL/INGLÉS — especifica cuál]
- Usar iconos/emojis con moderación, solo donde aporten claridad visual
- Tono profesional pero accesible, sin relleno de marketing
- Ejemplos de código reales del proyecto, no genéricos
- Mantener consistencia de formato entre todos los documentos (mismos headers, mismo estilo de tablas)

## 4. Antes de escribir
Primero muéstrame:
1. Un resumen de lo que detectaste en el stack (para confirmar que es correcto)
2. El índice/estructura propuesta para cada documento
Y espera mi aprobación antes de generar el contenido completo.