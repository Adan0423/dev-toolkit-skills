# Manos

Fuente: https://docs.qoder.com/en/extensions/hooks

## Descripción general

Los ganchos le permiten insertar lógica personalizada determinista en nodos de ejecución clave de los complementos Qoder IDE y JetBrains sin modificar el propio código de Qoder.

A diferencia de Prompt, los Hooks son un mecanismo de "ejecución cuando se activa un evento".

## Eventos soportados

| evento | tiempo de activación | Si se puede bloquear |
| --- | --- | --- |
| `Pregunta de usuarioEnviar` | Después de que el usuario envía el mensaje y antes del procesamiento del Agente | Sí |
| `Preuso de herramientas` | Antes de la ejecución de la herramienta | Sí |
| `PostToolUse` | Después de que la herramienta tenga éxito | No |
| `PostToolUseFailure` | Después del fallo de la herramienta | No |
| `Detener` | Cuando el Agente completa su respuesta | No |

## Escenario típico

- Interceptar comandos peligrosos
- Limitar la ruta de escritura de archivos
- Ejecute automáticamente lint/format después de escribir el archivo
- Registrar cuando falla la herramienta
- Aparece una notificación en el escritorio después de completar una tarea
- Revisar mensaje de usuario

## Ubicación del archivo de configuración

Las configuraciones multinivel se ejecutarán juntas, con prioridad de menor a mayor:

| camino | Alcance | prioridad |
| --- | --- | --- |
| `~/.qoder/settings.json` | nivel de usuario | 1 |
| `.qoder/configuración.json` | nivel de proyecto | 2 |
| `.qoder/settings.local.json` | Proyecto local | 3 |

ilustrar:

- IDE/JetBrains plug-in/CLI comparten el mismo conjunto de configuraciones de Hook
- La versión actual de la descripción del documento requiere reiniciar el IDE para que las modificaciones surtan efecto.

## Formato de configuración

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.qoder/hooks/block-rm.sh"
          }
        ]
      }
    ]
  }
}
```

## protocolo de guión

- Recibir contexto de evento JSON a través de `stdin`
- `salida 0`: liberación
- `exit 2`: Bloquear y enviar `stderr` al Agente
- Otros códigos de salida: tratados como errores, pero normalmente no interrumpen el proceso principal

## Ejemplo

El documento oficial destaca:

- Evite `rm -rf` con `PreToolUse`
- Utilice `PostToolUse` para ejecutar Lint automáticamente después de escribir un archivo
- Utilice "Detener" para realizar notificaciones en el escritorio

