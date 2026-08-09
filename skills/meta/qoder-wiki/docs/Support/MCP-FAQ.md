Preguntas frecuentes sobre #MCP

Esta guía le ayuda a diagnosticar y resolver problemas comunes al instalar y ejecutar el servicio Model Context Protocol (MCP).

## No se puede agregar o instalar el servicio MCP

### Problema: falta el entorno de ejecución NPX

**Mensaje de error:**
```
No se pudo iniciar el comando: ejecutivo: "npx": archivo ejecutable no encontrado en $PATH
```

**Causa:** La herramienta de línea de comando `npx` no está instalada o no está disponible en la `PATH` del sistema.

**Solución:** Instale Node.js V18 o superior (incluye NPM V8 y superior).

### Problema: falta el entorno UVX

**Mensaje de error:**
```
No se pudo iniciar el comando: exec: "uvx": archivo ejecutable no encontrado en $PATH
```

**Causa:** El comando `uvx` no se ha instalado.

**Solución:** Instalar `uv`:
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Problema: No se puede inicializar el cliente MCP

**mensaje de error:**
```
No se pudo inicializar el cliente MCP: se excedió la fecha límite de contexto
```

**Posibles motivos:**
- La configuración de los parámetros del servicio MCP es incorrecta
- Los problemas de red impiden que se descarguen recursos
-La política de seguridad de la red empresarial impide la inicialización

**Solución:**
1. Haga clic en **Copiar comando completo** en la interfaz de usuario.
2. Ejecute este comando en la terminal para obtener un resultado de error más detallado.
3. Analizar y manejar errores específicos.

## Problemas relacionados con el uso de herramientas

### Problema: falló la ejecución de la herramienta

**Razón:** Algunos servidores MCP (como MasterGo, Figma) necesitan configurar manualmente `API_KEY` o `TOKEN` en los parámetros al realizar la configuración.

**Solución:**
1. Vaya a Configuración de Qoder > MCP
2. Busque el servidor correspondiente y haga clic en **Editar**
3. Verifique los parámetros en **Argumentos** y reemplácelos con los valores correctos.

### Problema: LLM no puede llamar a la herramienta MCP

**Causa 1:** No en modo Agente

**Solución:** Abra el directorio del proyecto y cambie al modo Agente

**Causa 2:** El servidor MCP no está conectado

**Solución:** Haga clic en el ícono Reintentar en la interfaz

> **Mejores prácticas:** Evite el uso de nombres demasiado similares para los servidores MCP y sus herramientas para evitar ambigüedades al llamarlos.

### Problema: la lista de servidores MCP no se puede cargar

**Síntomas:** La lista de servidores sigue cargando

**Solución:** Reinicie Qoder IDE y vuelva a intentarlo
