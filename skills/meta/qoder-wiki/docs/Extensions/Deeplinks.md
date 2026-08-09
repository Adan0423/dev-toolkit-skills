# Enlaces profundos

Los enlaces profundos le permiten compartir indicaciones de AI Chat, misiones, reglas y configuraciones del servidor MCP con otras personas a través de una simple URL. Cuando hace clic en un enlace profundo, el IDE se abre y muestra un cuadro de diálogo de confirmación que muestra lo que está a punto de agregarse.

## formato de URL

```
{scheme}://{host}/{path}?{parameters}
```

| componentes | ilustrar | Ejemplo |
| --- | --- | --- |
| `esquema` | protocolo | `qoder` |
| `anfitrión` | Identificación del procesador de cadena profunda | `aicoding.aicoding-enlace profundo` |
| `camino` | Ruta de operación | `/chat`, `/quest`, `/regla`, `/mcp/add` |
| `parámetros` | Parámetros de consulta de URL | `texto=hola&modo=agente` |

## Tipos de enlaces profundos disponibles

| camino | ilustrar | ¿Necesitas iniciar sesión? |
| --- | --- | --- |
| `/chat` | Crea sesiones inteligentes | Sí |
| `/búsqueda` | Crear una misión | Sí |
| `/regla` | Crear reglas | No |
| `/mcp/añadir` | Agregar servidor MCP | No |

## Crear conversación/chat inteligente

Comparta palabras breves que se puedan usar directamente en el chat.

### formato de URL

```
qoder://aicoding.aicoding-deeplink/chat?text={prompt}&mode={mode}
```

### Descripción del parámetro

| parámetro | ¿Es necesario? | ilustrar |
| --- | --- | --- |
| `texto` | Sí | Solicitar que el contenido se complete previamente |
| `modo` | No | Modo de chat: `agente` o `preguntar` |

## Crear misión/misión

Comparta tareas de Quest y permita que la IA complete tareas de desarrollo complejas de forma autónoma.

### Descripción del parámetro

| parámetro | ¿Es necesario? | ilustrar |
| --- | --- | --- |
| `texto` | Sí | Descripción de la tarea |
| `claseagente` | No | Modo de ejecución: `LocalAgent`, `LocalWorktree` o `RemoteAgent` |

## Crear regla/regla

Comparta reglas para guiar el comportamiento de la IA.

### Descripción del parámetro

| parámetro | ¿Es necesario? | ilustrar |
| --- | --- | --- |
| `nombre` | Sí | Nombre de la regla |
| `texto` | Sí | Contenido de la regla |

## Agregar servidor MCP /mcp/add

Comparta la configuración del servidor MCP.

### Descripción del parámetro

| parámetro | ¿Es necesario? | ilustrar |
| --- | --- | --- |
| `nombre` | Sí | Nombre del servidor MCP |
| `configuración` | Sí | Configuración JSON del servidor MCP codificado en Base64 |

## Precauciones de seguridad

- **NO INCLUYA DATOS CONFIDENCIALES**: No incruste claves API, contraseñas ni código propietario en enlaces profundos
- **Verificar fuente**: haga clic únicamente en enlaces profundos de fuentes confiables
- **Verificar antes de confirmar**: El IDE siempre muestra un cuadro de diálogo de confirmación

## Límite de longitud de URL

Las URL de enlaces profundos no deben tener más de **8000 caracteres**.
