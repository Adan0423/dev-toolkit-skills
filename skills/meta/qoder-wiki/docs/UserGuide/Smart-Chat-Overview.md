#Resumen de la sesión inteligente

Qoder ofrece dos modos: respuesta inteligente a preguntas y agente. Estas capacidades pueden ayudar a los desarrolladores a resolver problemas de codificación, corregir errores, depurar y solucionar problemas de tiempo de ejecución. Qoder también admite la edición de múltiples archivos, la toma de decisiones autónoma, el conocimiento del entorno y la invocación de herramientas para ayudar a completar tareas de codificación de un extremo a otro.

## Funciones principales

### 1. Múltiples modos de chat

En el mismo proceso de conversación, los desarrolladores pueden cambiar libremente entre los modos inteligentes de preguntas y respuestas y de agente. Esta flexibilidad aumenta la productividad y la eficiencia en todo tipo de flujos de trabajo de desarrollo.

### 2. Conciencia ambiental automática

Qoder identificará automáticamente el marco del proyecto, la pila de tecnología, los archivos de código requeridos y los mensajes de error de la descripción de la tarea. Esto elimina la necesidad de agregar contexto manualmente y hace que las descripciones de las tareas sean más concisas.

### 3. Uso de herramientas

Qoder puede llamar de forma independiente a más de 10 herramientas integradas para ayudar en la lectura y escritura de archivos, consulta de códigos y resolución de problemas de errores. También admite la configuración de herramientas MCP (Protocolo de contexto modelo), lo que permite a los desarrolladores personalizar el conjunto de herramientas según sea necesario.

### 4. Ejecución del comando

Qoder puede juzgar, generar y ejecutar de forma independiente los comandos necesarios, mejorando significativamente la eficiencia de la ejecución de tareas.

### 5. Cambios a nivel de proyecto

Según la descripción de la tarea, Qoder admite la modificación de varios archivos de código en el proyecto. A través de múltiples rondas de diálogo, se puede realizar la optimización del código o la reversión de instantáneas para completar las tareas de manera más eficiente.

### 6. Percepción de la memoria

Qoder tiene capacidades de memoria autónoma basadas en LLM. Aprende de cada conversación, construyendo gradualmente un rico banco de memoria relevante para el desarrollador individual, los proyectos específicos y los problemas encontrados.

## Iniciar un nuevo chat

### Abre el panel de conversación inteligente

Para iniciar una conversación de IA, inicie sesión en Qoder y active la barra lateral secundaria en la esquina superior derecha.

O use el atajo de teclado:

| Acciones | MacOS | Ventanas |
| --- | --- | --- |
| Abrir/cerrar el panel de sesión inteligente | `⌘` `L` | `Ctrl` `L` |

### Seleccionar modo

- **Preguntas y respuestas inteligentes**: un modo simple de preguntas y respuestas para responder preguntas de programación. Proporciona soluciones y sugerencias basadas en el contexto, pero no modifica el código.
- **Agente**: un modo de ejecución de tareas de codificación autónoma con capacidad de toma de decisiones, percepción del entorno y uso de herramientas.

### Requisitos de entrada

Después de seleccionar el modo de chat, ingrese la descripción del requisito en el cuadro de entrada. sugerencia:

- Estructura tu solicitud: indica claramente lo que quieres que Qoder logre
- Proporcionar contexto: incluir archivos, imágenes, cambios de código y otra información relacionada.
- Dejar claras las expectativas: indicar preferencias o normas.
- Dar comentarios iterativos: proporcionar comentarios sobre sugerencias o respuestas de código.

## Modificación y revisión de código

### Edición de múltiples archivos

En modo agente, Qoder puede realizar modificaciones en varios archivos de código. Cada modificación de un archivo consta de dos fases: "construir" y "aplicar".

### Revisar, aceptar o rechazar cambios

Haga clic en el botón **Ver cambios** en el espacio de trabajo o en archivos individuales para comparar los cambios. Entonces:

- Utilice las flechas hacia arriba y hacia abajo para navegar dentro del archivo actual y ver los cambios
- Elige rechazar o aceptar cada cambio.
- Utilice las flechas hacia adelante/atrás en el área de acción a nivel de archivo para cambiar entre archivos modificados

## herramienta

Qoder proporciona una variedad de herramientas para ayudar con diversas tareas de programación:

- Búsqueda de archivos
- Lectura de archivos
- Lectura de directorio
- Búsqueda de símbolos semánticos
- Edición de archivos
- Comprobación de errores
- ejecución de comando
