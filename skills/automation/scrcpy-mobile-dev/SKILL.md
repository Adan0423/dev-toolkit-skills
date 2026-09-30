---
name: scrcpy-mobile-dev
description: Usa scrcpy y ADB de forma segura y reproducible durante desarrollo Android en Windows para detectar dispositivos, abrir espejado/control, lanzar apps, trabajar por USB o Wi-Fi, diagnosticar errores de conexión y evitar ejecutar scrcpy cuando no existe un target ADB válido.
metadata:
  version: "1.1.0"
  tags: "android, adb, scrcpy, windows, mobile-development, debugging"
  source: "https://github.com/Genymobile/scrcpy"
  tested-target: "scrcpy-4.1"
---

# scrcpy Mobile Development Skill

## Propósito

Usar `scrcpy` como herramienta de desarrollo y pruebas Android sin tratarlo como sustituto de ADB, Android Studio, el emulador o las herramientas de compilación.

Este Skill debe priorizar siempre esta secuencia:

```text
resolver herramientas
→ verificar ADB
→ detectar target
→ reparar conexión si procede
→ seleccionar dispositivo
→ ejecutar scrcpy con serial explícito
→ ejecutar acciones de desarrollo
```

Nunca ejecutar `scrcpy` directamente cuando todavía no se ha comprobado que exista un dispositivo ADB en estado `device`.

## Cuándo activar

Activa este Skill cuando el usuario:

- trabaje con `scrcpy`, ADB o mirroring Android;
- quiera probar una app Android en un dispositivo físico;
- quiera lanzar una app desde el PC y observarla/controlarla;
- reporte `Could not find any ADB device`;
- reporte `Server connection failed` junto a un fallo ADB;
- tenga dispositivos `unauthorized`, `offline` o múltiples targets;
- quiera conectar por USB o Wi-Fi;
- quiera automatizar el arranque de `scrcpy` en Windows;
- necesite capturar una sesión manual de QA, demostración o debugging.

## Principio central

`scrcpy` usa ADB para descubrir y comunicarse con Android. Por tanto:

- primero diagnostica ADB;
- después lanza `scrcpy`;
- si ADB no ve un target válido, no atribuyas automáticamente el problema a `scrcpy`;
- nunca ocultes el estado real de `adb devices -l`.

## Descubrimiento de herramientas en Windows

Resuelve ejecutables en este orden:

1. carpeta explícita configurada por el usuario;
2. carpeta del launcher/proyecto;
3. `PATH` mediante `Get-Command`;
4. carpeta que contiene `scrcpy.exe`, buscando `adb.exe` junto a él;
5. Android SDK `platform-tools` si `ANDROID_SDK_ROOT` o `ANDROID_HOME` están definidos.

Requisitos mínimos:

```text
scrcpy.exe
adb.exe
```

Si falta `scrcpy.exe`, detén la ejecución y muestra la ruta buscada.
Si falta `adb.exe`, detén la ejecución y explica que `scrcpy` no podrá descubrir dispositivos.

## Preflight obligatorio

Antes de iniciar `scrcpy`:

```powershell
adb start-server
adb devices -l
```

Clasifica cada target:

- `device`: usable;
- `unauthorized`: requiere autorización en el teléfono;
- `offline`: conexión ADB degradada;
- `no permissions`: problema de permisos/driver, según plataforma;
- ausente: ADB no detecta el dispositivo.

## Caso: exactamente un dispositivo válido

Usa siempre el serial explícito:

```powershell
scrcpy --serial=<SERIAL>
```

No dependas de selección implícita cuando una automatización puede conservar conexiones TCP/IP previas.

## Caso: varios dispositivos válidos

No elijas silenciosamente.

Presenta:

```text
[1] SERIAL_A  model:...
[2] SERIAL_B  model:...
```

Después ejecuta:

```powershell
scrcpy --serial=<SERIAL_ELEGIDO>
```

## Caso: unauthorized

No reinicies autorizaciones del teléfono automáticamente.

Indica al usuario:

1. desbloquear el dispositivo;
2. confirmar el diálogo de depuración USB;
3. opcionalmente activar “Permitir siempre desde este equipo” si confía en el PC;
4. volver a ejecutar `adb devices -l`.

Es válido realizar reintentos temporizados mientras el usuario autoriza.

## Caso: offline

Primero intenta una reparación no destructiva:

```powershell
adb reconnect offline
adb devices -l
```

Si sigue offline:

```powershell
adb kill-server
adb start-server
adb devices -l
```

No borres claves ADB ni revoques autorizaciones automáticamente.

## Caso: ningún dispositivo

No ejecutar `scrcpy`.

Ofrecer estas rutas:

1. reintentar USB;
2. reiniciar servidor ADB;
3. conectar por TCP/IP a un endpoint conocido;
4. emparejar por Wi-Fi en Android compatible;
5. iniciar un Android Emulator existente;
6. salir con diagnóstico accionable.

En Windows, si USB debugging está activado pero `adb devices` sigue vacío, considera driver USB/OEM.

## USB

Requisitos:

- Opciones para desarrolladores habilitadas;
- Depuración USB habilitada;
- cable con datos, no solo carga;
- driver ADB/OEM correcto en Windows cuando corresponda;
- autorización RSA aceptada.

Validación:

```powershell
adb devices -l
```

## Wi-Fi: scrcpy TCP/IP clásico

Cuando el dispositivo está conectado por USB y el usuario desea migrar a TCP/IP, puede utilizarse la función integrada de scrcpy:

```powershell
scrcpy --tcpip
```

Solo usarla después de confirmar que existe un dispositivo USB ADB válido.

Para un endpoint ya disponible:

```powershell
adb connect <IP>:<PORT>
scrcpy --serial=<IP>:<PORT>
```

No asumas que el puerto siempre es `5555` en Wireless Debugging moderno.

## Wi-Fi: Android 11+ con pairing

Cuando el dispositivo muestre “Emparejar dispositivo con código”:

```powershell
adb pair <IP>:<PAIR_PORT>
```

Tras emparejar, usar el endpoint de conexión mostrado por Android:

```powershell
adb connect <IP>:<ADB_PORT>
adb devices -l
scrcpy --serial=<IP>:<ADB_PORT>
```

El puerto de pairing y el puerto ADB pueden ser distintos.

Nunca persistas el código temporal de pairing en archivos o logs.

## Android Emulator

Si no hay dispositivo físico y el usuario acepta usar un emulador:

```powershell
emulator -list-avds
emulator -avd <AVD_NAME>
```

Espera a que aparezca como `device` en ADB antes de lanzar `scrcpy`.

Para esperar al boot cuando haga falta:

```powershell
adb -s <SERIAL> wait-for-device
adb -s <SERIAL> shell getprop sys.boot_completed
```

No asumas que un proceso `emulator.exe` iniciado implica que Android terminó de arrancar.

## Flujo recomendado para desarrollo de apps

Si el repositorio es Android/Gradle:

```text
compilar
→ instalar build debug
→ comprobar paquete
→ lanzar scrcpy
→ iniciar app
→ observar interacción
→ capturar logs si existe fallo
```

Comandos típicos:

```powershell
.\gradlew.bat installDebug
adb -s <SERIAL> shell pm list packages
scrcpy --serial=<SERIAL> --start-app=<PACKAGE>
```

Si `--start-app` no es apropiado para la versión detectada, inicia la actividad con ADB según el manifest real del proyecto; no inventes package names ni activities.

## Perfiles útiles

### Desarrollo normal

```powershell
scrcpy --serial=<SERIAL> --stay-awake
```

### Rendimiento limitado

```powershell
scrcpy --serial=<SERIAL> --max-size=1280 --max-fps=60
```

### Presentación / QA manual

```powershell
scrcpy --serial=<SERIAL> --show-touches
```

### Solo observación

```powershell
scrcpy --serial=<SERIAL> --no-control
```

No actives opciones adicionales sin una razón de desarrollo concreta.

## App package

Cuando el usuario proporcione un package real, puede iniciarse junto con `scrcpy`:

```powershell
scrcpy --serial=<SERIAL> --start-app=<PACKAGE>
```

Antes de asumir que existe:

```powershell
adb -s <SERIAL> shell pm path <PACKAGE>
```

Si no existe, informa si debe instalarse primero.

## Logs durante debugging

Para problemas de app, no mezcles automáticamente toda la salida de Logcat con el diagnóstico de scrcpy.

Usa filtros por package/PID cuando sea posible.

Nunca imprimas ni conserves voluntariamente:

- access tokens;
- refresh tokens;
- contraseñas;
- cookies de sesión;
- headers Authorization;
- secretos de API.

## APK drag-and-drop

`scrcpy` soporta instalación mediante drag-and-drop de APK. Para flujos reproducibles de agentes, prefiere:

```powershell
adb -s <SERIAL> install -r <APK>
```

o el task Gradle correspondiente, porque permite capturar exit code y salida.

## Guardrails

- No ejecutes `scrcpy` si no existe target ADB válido.
- No ejecutes comandos destructivos para “arreglar” ADB.
- No borres `~/.android/adbkey*` o equivalentes automáticamente.
- No ejecutes `adb usb`/`adb tcpip` sobre un target distinto al seleccionado.
- No cambies settings del dispositivo sin explicar el efecto.
- No uses `adb root` como requisito general.
- No instales APKs no solicitados.
- No desbloquees bootloader.
- No habilites ADB por red en redes no confiables sin advertencia.
- No guardes pairing codes.
- No expongas datos sensibles de Logcat.
- Si hay múltiples dispositivos, exige selección explícita o un serial ya configurado.

## Diagnóstico mínimo que debe mostrar el agente

```text
scrcpy: encontrado / no encontrado
adb: encontrado / no encontrado
adb server: iniciado / error
targets:
  serial | state | model | transport
selección: <serial o none>
acción: launch / retry / pair / connect / emulator / stop
```

## Launcher recomendado en Windows

Para un launcher local pequeño y mantenible, prefiere Python 3 + Tkinter antes que una cadena grande de scripts PowerShell/BAT. Tkinter no requiere dependencias runtime externas en una instalación estándar de Python para Windows.

Estructura recomendada:

```text
ScrcpyQuickLaunch/
├── INICIAR.bat
├── app.py
└── README.md
```

`INICIAR.bat` debe ser únicamente el bootstrap: localizar `pyw.exe`, `pythonw.exe`, `py.exe` o `python.exe` y ejecutar `app.py`. Mantén el BAT en ASCII para evitar problemas con la code page de `cmd.exe`.

La aplicación Python debe:

1. resolver `scrcpy.exe` y `adb.exe`;
2. ejecutar `adb start-server`;
3. leer `adb devices -l`;
4. impedir el lanzamiento si no existe un target en estado `device`;
5. distinguir `unauthorized` y `offline`;
6. permitir selección explícita con múltiples dispositivos;
7. soportar `adb pair` y `adb connect` para Wireless Debugging;
8. ejecutar `scrcpy --serial=<SERIAL>` solo después del preflight;
9. guardar configuración en UTF-8;
10. decodificar stdout/stderr con fallback seguro para Windows.

No leas ni escribas widgets de Tkinter desde threads secundarios. Captura los parámetros de UI en el hilo principal, ejecuta ADB en background y devuelve actualizaciones al hilo de Tkinter mediante `after(...)`.

## Referencias internas

Consulta según necesidad:

- `references/troubleshooting.md`
- `references/development-workflows.md`
- `references/command-reference.md`
- `references/windows-launcher.md`

No cargues todas las referencias si una sola resuelve la tarea.
