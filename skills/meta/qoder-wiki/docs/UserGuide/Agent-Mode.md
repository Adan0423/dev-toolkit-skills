# Modo agente

Fuente: https://docs.qoder.com/zh/user-guide/chat/agent

## Descripción general

El modo agente tiene capacidad de toma de decisiones autónoma, conocimiento del entorno y programación de herramientas, y es adecuado para completar tareas de codificación de un extremo a otro.

## Competencias básicas

- Cambios en varios archivos a nivel de proyecto
- Desarrollar automáticamente planes de ejecución.
- Identificar automáticamente el marco del proyecto, la pila de tecnología y los mensajes de error.
- Utilizar de forma independiente herramientas como búsqueda, lectura y escritura, y terminales.
-Soporte de descubrimiento automático e invocación de herramientas MCP.

## Cómo trabajar

### Planificación

Para tareas complejas, se generarán planes para que los usuarios los revisen y luego los ejecuten después de la confirmación.

### Lista de tareas pendientes

Qoder genera una lista de tareas pendientes y muestra el estado:

- Círculo abierto: no iniciado
- Círculo giratorio: en progreso
- Casilla de verificación: Listo

### Ejecutar comando

- De forma predeterminada, se requiere confirmación antes de ejecutar cada comando.
- La lista de permisos de ejecución automática se puede configurar en la configuración
- El comando en segundo plano mostrará el estado de ejecución y realizará un seguimiento continuo de la salida.

### Herramientas MCP

- Después de configurar MCP, se puede llamar al Agente a pedido
- Generalmente se busca la confirmación antes de la ejecución.

## Funciones adicionales

- Palabras de aviso de optimización con un solo clic
-Múltiples rondas de sesiones con iteración continua.
- Se utiliza junto con la revisión de diferencias y la reversión de instantáneas.

