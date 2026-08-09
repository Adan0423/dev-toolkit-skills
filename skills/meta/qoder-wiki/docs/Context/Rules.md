# regla

Qoder admite la configuración de reglas únicas para cada proyecto. Las reglas se almacenan en el directorio `.qoder/rules` y solo son efectivas para el proyecto actual. Optimizan la adaptación del modelo a sus preferencias de codificación, incluido el marco y el estilo de codificación utilizados por su proyecto.

## Cómo funcionan las reglas

Los modelos de lenguajes grandes (LLM) se basan en conocimientos generales y, por lo tanto, carecen del contexto y las reglas específicas de su proyecto. Las reglas de Qoder compensan esto inyectando estratégicamente un contexto predefinido en las indicaciones, guiando las respuestas de la IA para que se alineen de manera más consistente con los estándares y requisitos de su proyecto.

### Almacenar y compartir

- Los archivos de reglas se almacenan directamente en el directorio del proyecto y se comparten con los miembros del equipo a través de sistemas de control de versiones como Git.
- Para reglas solo locales, agregue el directorio `.qoder/rules` al archivo `.gitignore` de su proyecto

### límite

- **Todos los archivos de reglas activos** combinados permiten hasta **100 000 caracteres** (los excesos se truncarán)
- Sólo admite lenguaje natural, sin imágenes ni enlaces.

## Tipo de regla

| tipo | describir | Escenarios de uso |
| --- | --- | --- |
| Introducción manual | Aplicar manualmente usando `@rule` a través del panel de conversación inteligente o conversación en línea | Flujo de trabajo bajo demanda, palabras de aviso personalizadas |
| decisión modelo | El modelo evalúa la descripción de la regla en modo agente y decide cuándo aplicarla. | Tareas basadas en escenarios (como generar pruebas unitarias o comentarios de código) |
| Siempre efectivo | Se aplica a todas las solicitudes de sesión inteligente y de sesión interlínea | Hacer cumplir los estándares a nivel de proyecto (como el estilo de codificación o el formato de documentación) |
| El archivo especificado entra en vigor | Se aplica a todos los archivos que coinciden con el patrón comodín | Reglas específicas de idioma o directorio |

## Compatibilidad AGENTS.md

Las reglas de Qoder ahora son compatibles con los archivos AGENTS.md. Para habilitar esta característica:

1. Simplemente copie el archivo `AGENTS.md` en el directorio del proyecto.
2. El agente reconocerá y utilizará automáticamente las reglas definidas en el archivo.
3. No se requiere configuración adicional: la integración es perfecta

> Si hay un conflicto entre el contenido de AGENTS.md y el contenido de una regla, el contenido de la regla tiene prioridad.

## mejores practicas

- **Mantenlo simple**: Haz que las reglas sean enfocadas y sin ambigüedades
- **Estructura clara**: utilice viñetas, listas numeradas o formato Markdown para mejorar la legibilidad
- **Incluir ejemplos**: proporcione ejemplos de código "buenos" para guiar el modelo
- **Iteración y optimización**: mejore continuamente las reglas según los resultados y los comentarios del modelo

## Configurar reglas

1. En la esquina superior derecha de Qoder IDE, haga clic en el icono de usuario y seleccione **Configuración de Qoder**
2. En el panel de navegación izquierdo, haga clic en **Reglas**
3. Haga clic en **Agregar**
4. En la barra de búsqueda superior, ingrese un nombre de regla único y presione **Aceptar**
5. Seleccione el tipo de regla:
   - **Introducción manual**
   - **Decisión del modelo**: Ingrese la descripción del escenario
   - **Especifique los archivos para que surtan efecto**: proporcione comodines de ruta de archivo separados por comas (como `*.md`, `src/*.java`)
   - **Siempre válido**
6. Cierra la ventana para guardar los cambios.
