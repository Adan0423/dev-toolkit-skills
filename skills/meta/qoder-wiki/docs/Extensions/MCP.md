# MCP (Protocolo de contexto modelo)

El Model Context Protocol (MCP) amplía las capacidades de Qoder a través de una perfecta integración con sistemas externos y fuentes de datos.

## ¿Qué es MCP?

MCP es un protocolo abierto que estandariza cómo las aplicaciones proporcionan contexto y herramientas a modelos de lenguajes grandes (LLM). Al exponer la funcionalidad en una interfaz consistente, MCP permite que LLM interactúe con sistemas externos como API, bases de datos y herramientas locales de manera estructurada y segura.

### ¿Por qué utilizar MCP?

MCP permite que el agente Qoder se conecte a varios sistemas externos y fuentes de datos a través de interfaces estandarizadas, mejorando así las capacidades del agente en las siguientes áreas:

- Obtener información en tiempo real
- Realizar operaciones en sistemas externos.
- Procesar datos estructurados o no estructurados.

### Métodos de transmisión admitidos

- **Entrada/Salida estándar (STDIO)**: se comunica a través de flujos stdin/stdout, adecuado para herramientas nativas
- **Eventos de envío de servicio (SSE)**: solicitud HTTP POST + respuesta de transmisión de eventos, alojado de forma remota, fácil de configurar

> **Nota:** Los servicios MCP solo se admiten en modo agente y se pueden usar hasta 10 servicios MCP simultáneamente.

## Configurar el servicio MCP

1. En la esquina superior derecha de Qoder IDE, haga clic en el icono de usuario y seleccione **Configuración de Qoder**
2. En el panel de navegación izquierdo, haga clic en **MCP**
3. Elija cualquiera de los siguientes métodos:

### Conéctese a su propio servicio MCP

En la pestaña **Mis servicios**, haga clic en **+Agregar** en la esquina superior derecha para agregar la configuración en el archivo JSON:

```json
{
  "mcpServers": {
    "github": {
      "comando": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "entorno": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<TU_TOKEN>"
      }
    }
  }
}
```

### Instalar desde MCP Square

1. Haga clic en la pestaña **MCP Plaza**
2. Explore la lista de servicios disponibles y haga clic en **Instalar** en el servicio de destino.

## Uso de herramientas MCP

Qoder selecciona automáticamente la herramienta MCP adecuada en función de:

- su mensaje de entrada
- Nombre y descripción de la herramienta.

Antes de que Qoder llame a la herramienta MCP, le pedirá confirmación.

## Ejemplo: recuperar el contenido de una página web

Utilice el servicio MCP para obtener contenido web de HTML y convertirlo a Markdown:

```json
{
  "mcpServers": {
    "buscar": {
      "tipo": "sse",
      "url": "https://mcp.api-inference.modelscope.net/******/sse"
    }
  }
}
```

Luego en modo agente ingresa:

```
Para resumir esta documentación: https://docs.qoder.com/user-guide/chat/overview
```

## Ejemplo: Consultar el clima

```json
{
  "mcpServers": {
    "clima": {
      "comando": "npx",
      "args": ["-y", "@h1deya/mcp-server-weather"]
    }
  }
}
```
