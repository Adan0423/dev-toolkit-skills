# Troubleshooting scrcpy + ADB on Windows

## Error: Could not find any ADB device

Interpretación: `scrcpy` no encontró un target que ADB pudiera usar.

Orden de diagnóstico:

1. `adb start-server`
2. `adb devices -l`
3. comprobar estado devuelto
4. si no hay filas: USB debugging, cable, puerto USB y driver/OEM
5. si `unauthorized`: aceptar autorización RSA en Android
6. si `offline`: `adb reconnect offline`, luego reinicio de servidor si persiste
7. si hay varios targets: seleccionar serial explícitamente

## Error: Server connection failed

No asumir causa única.

Primero determinar si aparece después de un fallo de descubrimiento ADB. Si `adb devices -l` está vacío, resolver ADB primero.

Si el dispositivo sí está en estado `device`:

1. ejecutar `scrcpy --version`;
2. confirmar que cliente y archivos pertenecen a la misma instalación;
3. lanzar con `--serial=<serial>`;
4. capturar salida completa;
5. revisar si hay otro ADB en PATH diferente al incluido con scrcpy;
6. comprobar que no se mezclan instalaciones antiguas y nuevas.

## unauthorized

No se arregla repitiendo `scrcpy`.

El usuario debe autorizar el PC desde el dispositivo. Mantener el teléfono desbloqueado y revisar el diálogo RSA.

## offline

Intentar:

```powershell
adb reconnect offline
adb devices -l
```

Después, solo si persiste:

```powershell
adb kill-server
adb start-server
adb devices -l
```

## Windows driver

Si el dispositivo no aparece en ADB aunque USB debugging esté activo:

- revisar Administrador de dispositivos;
- instalar driver OEM adecuado;
- para dispositivos Google, considerar Google USB Driver;
- evitar instalar paquetes de drivers de fuentes aleatorias.

## Varios ADB

Problema común en Windows:

```powershell
where.exe adb
where.exe scrcpy
```

Si hay varias copias de `adb.exe`, registrar cuál se está usando.

El launcher incluido resuelve primero el ADB junto a `scrcpy.exe` cuando es posible para minimizar incompatibilidades.
