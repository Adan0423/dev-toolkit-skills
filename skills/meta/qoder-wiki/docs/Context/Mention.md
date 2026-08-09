# @Mencionar contexto

Qoder admite entradas contextuales enriquecidas, como archivos de código, directorios, imágenes, confirmaciones de git (gitCommit) y reglas. Puede utilizar estos recursos para complementar sus preguntas y expresar sus necesidades con mayor claridad.

## Cómo agregar contexto

Abra la ventana de selección de contexto utilizando cualquiera de los siguientes métodos:

- **Método 1**: haga clic en **+ Agregar contexto** en el cuadro de entrada
- **Método 2**: Ingrese `@` en el cuadro de entrada y continúe escribiendo para buscar archivos. Seleccione un tipo de contexto, como `@file`, `@folder` o `@gitCommit`, y busque contenido específico. Admite selección múltiple.
- **Método 3**: arrastre y suelte o copie y pegue archivos de código e imágenes para agregarlos como contexto

## Tipos de contexto admitidos

### @archivo

Utilice este comando para hacer preguntas o modificar uno o más archivos.

Escriba `@file` en el cuadro de entrada para seleccionar uno o más archivos de código. También puedes arrastrar archivos desde el Explorador al cuadro de chat.

### @regla

La incorporación de reglas en las indicaciones del sistema para cada llamada de modelo proporciona un contexto persistente y reutilizable para una guía coherente en la generación de código, la refactorización y la automatización del flujo de trabajo.

### @carpeta

Utilice este comando para consultar o modificar fragmentos de código. Útil al buscar, refactorizar, agregar comentarios o generar pruebas unitarias.

Ingrese `@folder` para buscar una carpeta por nombre.

### @imagen

Utilice este comando para agregar imágenes y generar código, corregir errores o visualizar contenido. Por ejemplo, puede generar una página de inicio basada en el borrador del diseño.

Ingrese `@image` y Qoder le pedirá que cargue la imagen. También puedes copiar y pegar la imagen directamente en el cuadro de chat.

### @codeChanges

Para ver los cambios de código en el área de preparación de Git actual, use el comando `@codeChanges`. Por ejemplo, puede hacer que Qoder revise y optimice su código, o lo complemente con pruebas unitarias, antes de enviarlo a un repositorio de Git.

### @gitCommit

Para cambios de código en confirmaciones de Git, use `@gitCommit` para agregar detalles de confirmación. Por ejemplo, puede seleccionar uno o más registros de confirmación de Git para tareas como resolución de problemas, corrección de defectos y generación de pruebas unitarias.
