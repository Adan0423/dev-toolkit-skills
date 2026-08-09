#RepoWiki

Repo Wiki generará automáticamente documentación estructurada para su proyecto y realizará un seguimiento continuo de los cambios de código y documentación.

Cuando consulta puntos de conocimiento, explicaciones de código y agrega características funcionales durante el proceso de desarrollo, Repo Wiki realizará un análisis en profundidad de la estructura del proyecto y la implementación del código, y combinará Repo Wiki e información contextual para proporcionar respuestas y soporte de documentos más precisos y detallados.

## Momento de actualización de Wiki

La wiki se actualiza en tres situaciones clave:

### 1. Generar Wiki por primera vez

Cuando abres un proyecto por primera vez, la wiki no existe de forma predeterminada. Puedes crearlo desde cero con un solo clic.

### 2. Cambios de código detectados

Después de la generación inicial, el sistema continuará monitoreando los cambios en el código. Si modifica contenido que ha sido documentado por el wiki (como firmas de funciones, definiciones de clases, puntos finales de API), el sistema detectará inconsistencias entre el código actual y el wiki existente. Puede hacer clic en **Actualizar** para regenerar solo las partes afectadas.

### 3. Sincronización de directorios Git

Si edita archivos Markdown directamente en el directorio de Git, el sistema detectará que el contenido de Git no es coherente con el Wiki. Puede hacer clic en **Sincronizar** para sincronizar los cambios en Git y actualizar la wiki.

## límite

- Máximo 10.000 archivos por proyecto
- Solo admite repositorios Git y contiene al menos una confirmación.

## Compartir wiki

Cuando generas un wiki localmente, el sistema crea automáticamente un directorio dedicado en el repositorio de código: `.qoder/repowiki`.

Puede confirmar y enviar este directorio a la rama remota. Luego, los miembros del equipo pueden extraer el contenido wiki generado a través de `git pull`; no se requiere configuración adicional.

## Soporte en varios idiomas

El sistema wiki admite varios idiomas; puede seleccionar su idioma preferido al generar el wiki. Actualmente admite **inglés** y **chino**.

## Escenarios de uso

- **Consultas relacionadas con la arquitectura y la implementación**: los agentes confían en el conocimiento arquitectónico prediseñado para responder rápidamente preguntas como "¿Cómo se implementa X?" casi sin necesidad de llamar a herramientas.
- **Tareas de desarrollo impulsadas por agentes**: cuando el ancho del contexto es limitado, Repo Wiki puede acelerar el posicionamiento del código y respaldar tareas como agregar nuevas funciones y corregir vulnerabilidades.
