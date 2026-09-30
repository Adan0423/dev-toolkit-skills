# Development workflows

## Ciclo Android nativo

```powershell
.\gradlew.bat assembleDebug
.\gradlew.bat installDebug
adb devices -l
scrcpy --serial=<SERIAL> --start-app=<PACKAGE>
```

Usa tasks reales del proyecto. No asumir que el módulo se llama `app` si Gradle declara otro nombre.

## React Native

Después de instalar/arrancar la app, scrcpy sirve para interacción rápida con el dispositivo. Los atajos de scrcpy no sustituyen Metro ni el debugger de React Native.

## Flutter

Usa Flutter para build/install/debug y scrcpy para observación/control. No reemplazar `flutter devices`, `flutter run` o DevTools por scrcpy.

## QA visual

Para reproducibilidad:

1. registrar serial/modelo;
2. registrar Android version;
3. registrar build/versionCode de la app;
4. iniciar scrcpy con argumentos declarados;
5. capturar logs por separado;
6. si se graba video, no asumir que reemplaza evidencia técnica.

## Dispositivo real vs emulador

Usa ambos cuando el problema dependa de hardware, OEM, cámara, Bluetooth, sensores, rendimiento o permisos. El emulador es útil para matrices de API/resolución; un dispositivo real sigue siendo importante antes de publicación.
