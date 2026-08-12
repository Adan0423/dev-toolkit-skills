# Guía de solución de problemas

Este artículo describe cómo utilizar el script de diagnóstico de Qoder para solucionar problemas de inicio y conexión de Qoder.

## Requisitos previos

Antes de ejecutar el script de diagnóstico, confirme lo siguiente:

- **Sistema operativo**: Windows
- **Permisos**: ejecuta el script con privilegios de administrador
- **Ruta de instalación**: Confirme que Qoder esté instalado en el directorio predeterminado `C:\Users\<Su nombre de usuario>\.qoder`

## Ejecutar script de diagnóstico

### Paso 1: ejecutar el script

1. Busque el archivo `.bat` guardado (como `qoder_Debug.bat`)
2. Haga doble clic en el archivo para ejecutar el script.
3. El script se ejecutará automáticamente para recopilar datos del sistema y de la aplicación.

⚠️ Espere a que el script se ejecute por completo. No cierre la ventana de comandos prematuramente.

### Paso 2: Ver los registros generados

Después de ejecutar el script, se generará un paquete comprimido ZIP, incluidos los archivos de registro recopilados y los archivos de configuración clave.

## Preguntas frecuentes

| Tipo de problema | Problema | Solución |
| --- | --- | --- |
| Red | Verifique la configuración del proxy | Compruebe si el proxy está habilitado. Si está utilizando un proxy, configure manualmente el proxy de red en la configuración |
| Estado del servidor Qoder | Si Qoder.exe existe | Verifique la ruta de instalación, elimine el directorio .qoder y reinicie el IDE para regenerar |
| Compatibilidad del sistema | Información del sistema y del hardware | Verifique que el sistema cumpla con los requisitos: Windows 10 o superior (64 bits), CPU compatible con x86_64 |

## Problemas que uno mismo no puede resolver

Si el problema aún no se puede resolver, comuníquese con support@qoder.com y adjunte el archivo de registro generado.
