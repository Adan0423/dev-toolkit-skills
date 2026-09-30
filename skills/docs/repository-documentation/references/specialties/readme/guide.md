---
name: project-readme-documentation
description: Analiza un repositorio real y crea o actualiza su README y documentación técnica con evidencia del código, dependencias y configuración. Úsala cuando el usuario pida documentar un proyecto, mejorar README.md, generar docs/ARCHITECTURE.md, docs/PROGRESS.md, docs/AGENTS.md, docs/SKILLS.md, docs/TODO.md o CONTRIBUTING.md, o estandarizar la documentación de un repositorio sin asumir su stack.
---

# Especialidad: readme

Procedencia: `skills/docs/project-readme-documentation/SKILL.md`. Guía derivada; editar fuente y reconstruir, no esta copia.

Aplica el procedimiento solo al modo seleccionado. Las preferencias del usuario, alcance y contrato común de la familia delimitan sus recomendaciones. No invoca otras skills por defecto.

# Documentación de proyectos y README

## Propósito

Analiza primero el repositorio y después redacta documentación útil, verificable y consistente. El resultado debe explicar cómo usar el proyecto, cómo está construido y qué queda pendiente, sin inventar tecnologías, comandos, variables de entorno, agentes, capacidades ni funcionalidades.

Trabaja por defecto en **español** porque es el idioma operativo de esta habilidad. Si el usuario lo solicita, si la documentación existente está claramente escrita en inglés o si el repositorio mantiene una convención inequívoca en otro idioma, conserva ese idioma de forma consistente y declara la decisión en el resumen inicial.

## Principios no negociables

- Inspecciona la estructura, las dependencias, el código fuente y la configuración antes de modificar cualquier documento.
- No asumas el framework, el lenguaje, el gestor de paquetes, los servicios externos ni los comandos de ejecución. Verifícalos mediante archivos reales del repositorio.
- Usa ejemplos de código y comandos que existan en el proyecto. Comprueba los nombres de scripts en `package.json`, `Makefile`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, workflows de CI y archivos equivalentes.
- No expongas secretos. Lee los nombres y descripciones de variables desde `.env.example`, `.env.sample`, esquemas de configuración y código, pero nunca copies valores secretos de `.env`, credenciales, tokens o claves privadas.
- Conserva información correcta de la documentación existente y actualízala solo cuando la evidencia del repositorio lo justifique.
- No modifiques el código de la aplicación para resolver un problema documental, salvo que el usuario lo pida explícitamente.
- No crees secciones vacías. Si una categoría no aplica, indícalo brevemente o exclúyela.
- Evita lenguaje de marketing, afirmaciones no demostradas y placeholders que parezcan información final.
- Usa emojis o iconos con moderación y solo si mejoran la lectura. No sustituyas explicaciones técnicas por iconos.

## Flujo de trabajo obligatorio

### 1. Inventariar el repositorio

Determina la raíz del proyecto y revisa, como mínimo, los siguientes elementos cuando existan:

| Área | Archivos o señales que debes buscar |
|---|---|
| Identidad | `README.md`, `LICENSE*`, `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `composer.json` |
| Código | `src/`, `app/`, `server/`, `client/`, `frontend/`, `backend/`, `lib/`, `tests/` y equivalentes |
| Configuración | `.env.example`, archivos de configuración, `Dockerfile`, `docker-compose*`, gestores de versiones y archivos de build |
| Automatización | `.github/workflows/`, CI/CD, scripts, `Makefile`, hooks y tareas programadas |
| Datos e infraestructura | migraciones, esquemas, proveedores cloud, Terraform, Kubernetes, almacenamiento y bases de datos |
| Producto | rutas, pantallas, comandos CLI, endpoints, integraciones y documentación existente |

Lee los archivos de dependencias reales y las partes relevantes del código. Usa la profundidad necesaria para distinguir, por ejemplo, una dependencia instalada de una tecnología realmente utilizada. Si el proyecto es grande, prioriza los puntos de entrada, scripts, configuración, módulos principales y pruebas, y registra qué partes no fueron inspeccionadas.

### 2. Identificar stack y alcance con evidencia

Clasifica lo detectado por **Frontend**, **Backend**, **Base de datos**, **Infraestructura** y **Herramientas**. Para cada tecnología importante, conserva una evidencia concreta, como el nombre de un archivo, una dependencia o un script. Distingue entre tecnología confirmada, inferida y no determinada; no presentes una inferencia como hecho.

Antes de escribir o sobrescribir documentación, muestra al usuario un diagnóstico breve y una propuesta de índices. Usa este formato adaptable:

```markdown
## Stack detectado

| Área | Tecnología o componente | Evidencia | Confianza |
|---|---|---|---|
| Frontend | [tecnología] | `[archivo o dependencia]` | Confirmada |

## Alcance observado

[Resumen de módulos, entradas, integraciones y documentación existente.]

## Idioma documental propuesto

[Español, inglés u otro, con la razón basada en el repositorio o en la petición.]

## Estructura propuesta

### README.md
1. ...
2. ...

### docs/ARCHITECTURE.md
1. ...

### docs/PROGRESS.md
1. ...

### Otros documentos
[Indicar cuáles aplican y cuáles no.]

¿Apruebas este diagnóstico y esta estructura para generar la documentación?
```

**Detén el flujo y espera aprobación explícita.** No generes el contenido completo en la misma respuesta que el diagnóstico. Si el usuario ya aprobó expresamente el alcance y la estructura en el contexto actual, continúa sin volver a preguntar.

### 3. Crear o actualizar la documentación

Después de la aprobación, crea `docs/` solo cuando sea necesario y actualiza los archivos aplicables. Mantén el mismo idioma, estilo de títulos, nivel de detalle y convenciones de tablas en todos los documentos.

#### `README.md`

Incluye, adaptando el orden al proyecto:

1. Un encabezado con el nombre real del proyecto y badges de build, licencia, versión y stack únicamente cuando exista evidencia para construir cada enlace. Usa [Shields.io](https://shields.io/) o un recurso equivalente; no inventes estados ni versiones.
2. Una descripción precisa de qué hace el proyecto, qué problema resuelve y quién lo utiliza, basada en el código y la configuración.
3. Una tabla del stack agrupada por Frontend, Backend, Base de datos, Infraestructura y Herramientas. Usa iconos de [Skill Icons](https://skillicons.dev/) o badges de Shields.io solo para tecnologías confirmadas.
4. Un diagrama Mermaid sencillo que muestre los componentes y sus conexiones. El diagrama debe reflejar el flujo real observado, no una arquitectura idealizada.
5. Las características principales expresadas como valor para el usuario. No describas como funcionalidad algo que solo aparece en una dependencia sin estar integrado.
6. Instalación y uso mediante pasos numerados y bloques de código con comandos reales del repositorio. Indica requisitos previos, gestor de paquetes, configuración y comandos de desarrollo, pruebas, build o despliegue cuando estén disponibles.
7. Una tabla de variables de entorno con nombre, descripción, requerido u opcional, y fuente de verificación. Nunca incluyas valores sensibles.
8. Un árbol comentado de las carpetas y archivos clave, limitado a lo que ayude a comprender el proyecto.
9. El estado del proyecto con enlace a `docs/PROGRESS.md` y a `docs/TODO.md` cuando ambos existan.
10. Licencia, contacto, enlaces oficiales y contribución solo si pueden verificarse en el repositorio o si el usuario los proporciona.

#### `docs/ARCHITECTURE.md`

Explica las decisiones técnicas que puedan demostrarse: capas, módulos, flujo de datos, límites entre servicios, persistencia, autenticación, integraciones y despliegue. Incluye diagramas Mermaid de flujo de datos cuando aporten claridad. Para cada decisión importante, separa **hecho observado**, **razón documentada** y **suposición pendiente de confirmar**. No conviertas una conjetura en una decisión oficial.

#### `docs/PROGRESS.md`

Registra la última fecha de actualización y organiza el estado por módulo o funcionalidad. Usa las categorías `✅ Implementado`, `🚧 En progreso` y `❌ Pendiente` solo cuando la evidencia lo permita. Relaciona cada elemento con archivos, rutas, pruebas o issues cuando existan. Si el estado no puede determinarse, márcalo como `Por confirmar` en lugar de inventarlo.

#### `docs/AGENTS.md`

Créalo o actualízalo únicamente si el proyecto usa agentes, skills, flujos LLM, automatizaciones inteligentes o componentes equivalentes. Para cada agente documenta propósito, disparador, herramientas o integraciones, entradas, salidas, límites y ubicación del código. Si no existe ese sistema, no generes un archivo vacío.

#### `docs/SKILLS.md`

Créalo o actualízalo únicamente si el proyecto contiene skills, capacidades modulares, plugins o un inventario explícito de funciones. Incluye nombre, propósito, disparador, entradas, salidas, dependencias y ejemplos de uso comprobables. No confundas una librería común con una skill del sistema.

#### `docs/TODO.md`

Crea este archivo como lista priorizada de pendientes cuando no exista una fuente equivalente. Separa `Crítico para el MVP`, `Importante` y `Mejoras futuras` según la evidencia disponible. Distingue los pendientes confirmados de las oportunidades sugeridas y no presentes como deuda técnica algo que solo sea una preferencia personal.

#### `CONTRIBUTING.md`

Créalo o actualízalo si el repositorio es colaborativo, tiene un remoto público, contiene instrucciones de contribución o el usuario lo solicita. Incluye requisitos, instalación, ramas, estilo, pruebas, commits, pull requests y código de conducta solo cuando estén definidos o puedan deducirse con seguridad. No inventes una política de revisión.

### 4. Validar antes de entregar

Revisa la documentación completa y comprueba lo siguiente:

| Control | Criterio |
|---|---|
| Exactitud | Cada tecnología, comando, ruta, script, variable y funcionalidad aparece respaldada por el repositorio o está marcada como pendiente de confirmar. |
| Comandos | Coinciden con scripts y archivos de configuración reales; evita comandos genéricos de otro stack. |
| Variables | Los nombres coinciden con las fuentes de configuración y no se filtran valores secretos. |
| Enlaces | Los enlaces internos apuntan a archivos que existen; los enlaces externos tienen un destino verificable. |
| Mermaid | Los diagramas usan sintaxis válida y nombres coherentes con la arquitectura observada. |
| Consistencia | Los documentos comparten idioma, convenciones de títulos, tablas, fechas y terminología. |
| Alcance | No se han creado documentos vacíos ni se ha modificado código sin autorización. |
| Trazabilidad | Los pendientes y estados importantes indican la evidencia o ubicación relacionada. |

Corrige los errores detectados y vuelve a validar. Si una comprobación requiere ejecutar el proyecto y hacerlo no es seguro o no están disponibles sus dependencias, informa de la limitación en vez de afirmar que pasó.

## Formato de entrega

Después de completar la aprobación, presenta un resumen conciso y luego la lista de archivos creados o actualizados. Para cada archivo, explica su propósito y las decisiones relevantes. Incluye las limitaciones de inspección, los elementos que requieren confirmación del usuario y las comprobaciones que no pudieron ejecutarse.

Usa una salida similar a esta:

```markdown
## Documentación actualizada

Se analizaron [áreas inspeccionadas] y se actualizaron los documentos sin modificar el código de la aplicación.

| Archivo | Acción | Contenido principal |
|---|---|---|
| `README.md` | Actualizado | Uso, stack, arquitectura y configuración |
| `docs/ARCHITECTURE.md` | Creado | Decisiones y flujos de datos |

## Validaciones

- [x] Comandos contrastados con los archivos del proyecto.
- [x] Variables de entorno revisadas sin exponer secretos.
- [ ] [Comprobación no ejecutada y motivo.]

## Requiere confirmación

[Ambigüedades o decisiones que el usuario debe revisar.]
```

## Ejemplos de comportamiento

**Solicitud:** “Mejora el README de este repositorio.”

**Comportamiento esperado:** inspeccionar primero el repositorio, presentar el stack con evidencias y proponer el índice de los documentos; esperar aprobación antes de editar.

**Solicitud:** “Actualiza la documentación de una app React con backend Python.”

**Comportamiento esperado:** no asumir React ni Python por la solicitud; confirmar ambas tecnologías leyendo dependencias, scripts y puntos de entrada. Si se confirman, documentarlas con los comandos reales del proyecto.

**Solicitud:** “Genera `docs/AGENTS.md`.”

**Comportamiento esperado:** buscar agentes o flujos de IA implementados. Si no existen, informar que el archivo no debe crearse vacío y pedir al usuario la información faltante o proponer documentar únicamente lo confirmado.

## Recursos incluidos

Esta habilidad no requiere scripts, plantillas ni referencias adicionales. Mantén el flujo principal en este archivo y agrega recursos solo si una tarea repetitiva, un esquema estable o una plantilla reutilizable lo justifica.
