# Windows launcher pattern

## Objetivo

Crear un launcher mínimo para `scrcpy` que no ejecute mirroring/control antes de que ADB tenga un target válido.

## Implementación recomendada

Usar Python 3 + Tkinter con un `INICIAR.bat` pequeño.

El BAT debe ser ASCII-safe y solo resolver el intérprete. Toda la UI, configuración y lógica ADB debe permanecer en Python.

## Flujo

```text
resolver scrcpy.exe / adb.exe
→ adb start-server
→ adb devices -l
→ parsear estados
→ seleccionar serial
→ scrcpy --serial=<serial>
```

Si el estado no es `device`, no ejecutar scrcpy.

## Estados

- `device`: permitir lanzamiento.
- `unauthorized`: pedir autorización RSA en el teléfono y reescanear.
- `offline`: intentar `adb reconnect offline`, reiniciar servidor y reescanear.
- vacío: ofrecer USB, emulador o Wireless Debugging.

## Codificación

- guardar `app.py`, Markdown y JSON como UTF-8;
- usar `ensure_ascii=False` al persistir JSON;
- mantener `.bat` en ASCII cuando sea posible;
- capturar subprocess como bytes;
- decodificar primero UTF-8 y después usar fallbacks de Windows;
- usar `errors="replace"` solo como último recurso.

## Threading con Tkinter

No acceder a `StringVar`, widgets o `messagebox` directamente desde un thread de trabajo.

Capturar las rutas/endpoints en el hilo principal, ejecutar `adb` en background y utilizar `root.after(...)` para actualizar la interfaz.
