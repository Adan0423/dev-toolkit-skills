# Comandos personalizados

La función de comando personalizado le permite encapsular mensajes y flujos de trabajo de uso común en comandos reutilizables. Simplemente ingrese `/` en el cuadro de diálogo Agente para llamar rápidamente a estas instrucciones, lo que mejora significativamente la eficiencia del desarrollo diario.

## Tipo de instrucción y alcance

| característica | directivas a nivel de usuario | Directivas a nivel de proyecto |
| --- | --- | --- |
| **Alcance** | Válido para todos los proyectos del usuario actual. | Solo tiene efecto en el directorio raíz del proyecto actual y sus subdirectorios. |
| **ruta de almacenamiento** | `~/.qoder/commands/` | `<Directorio raíz del proyecto>/.qoder/commands/` |
| **Escenarios aplicables** | Tareas de desarrollo comunes, como revisar código y generar pruebas unitarias. | Tareas específicas del proyecto, como verificar las especificaciones API de este proyecto. |
| **Método de compartir** | Disponible solo para el usuario actual | Se puede compartir con los miembros del equipo a través de sistemas de control de versiones como Git. |

> **Nota**: Las directivas a nivel de usuario no admiten la sincronización entre dispositivos; puede migrar manualmente los archivos de configuración.

## Crear directivas personalizadas

1. **Abra la interfaz de administración de comandos**
   - Método 1: Ingrese a la página de comandos en la configuración de Qoder y haga clic en el botón **Agregar**
   - Método 2: Ingrese `/` en el cuadro de diálogo y haga clic en la entrada rápida **Agregar comando** en la parte inferior

2. Ingrese un **nombre de comando único** (como `gen-test`) en la barra de búsqueda superior y presione **Entrar**

3. Seleccione el tipo de instrucción:
   - **Nivel de usuario**: comandos comunes aplicables a todos los proyectos
   - **Nivel de proyecto**: solo disponible en el proyecto actual

4. Complete el contenido completo de las palabras clave en el área de copia de orientación y sus instrucciones se guardarán automáticamente después de guardar el archivo.

5. Regrese a la sesión e ingrese `/` en el cuadro de diálogo para ver el comando recién creado.

## Instrucciones de ejemplo

### /código-inspeccionar

Un marco sistemático para evaluar el código fuente, que incluye:
- Control de implementación técnica
- Verificación de estándares de desarrollo.
- gestión de riesgos
- evaluación de mantenibilidad

### /control-de-seguridad

Inspección sistemática de la postura de seguridad del sistema:
-Seguridad de la aplicación
- Sistema de autenticación
- Protección de datos
- Arquitectura del sistema

### /crear-pr

Proceso estandarizado para enviar código:
-Garantía de Calidad del Código
- Cambiar documento
- Verificación de prueba

### /proyecto-prueba

Ejecute el conjunto de pruebas del proyecto:
- Configuración del entorno
- ejecución de prueba
-resolucion de problemas
