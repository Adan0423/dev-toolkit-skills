# Preguntas frecuentes Preguntas frecuentes

Estas preguntas frecuentes cubren preguntas comunes relacionadas con Qoder, incluida la instalación, el inicio de sesión, las plataformas compatibles, la compatibilidad de idiomas, la seguridad de los datos, la facturación, los problemas de red y la solución de problemas.

## Inicio rápido

### ¿Qué debo hacer si Qoder sigue deteniéndose en "Qoder iniciando"?

Intente los siguientes pasos:

1. **Revisa el entorno**
   - Asegúrate de que Qoder esté actualizado a la última versión.
   - Confirmar que el sistema operativo y la arquitectura del sistema son compatibles con Qoder.

2. **Prueba la conexión de red**
   - Ejecute el siguiente comando en la terminal para verificar la conectividad:
   ```
   rizo https://api1.qoder.sh/algo/api/v1/ping
   ```
   - Si se recibe `pong`, significa que la red está conectada

3. **Borrar caché local**
   - Finalizar el proceso Qoder
   - Eliminar el directorio `.Qoder`
   - Reiniciar Qoder

## Inicio de sesión y permisos

### ¿Qué pasa si mi inicio de sesión falla o veo un error de permiso denegado?

- Las sesiones de inicio de sesión caducadas requieren volver a intentarlo
- Asegúrese de que la red permita el acceso a los siguientes nombres de dominio:
  - api1.qoder.sh
  - api2.qoder.sh
  - api3.qoder.sh

## Plataformas compatibles

- macOS: 11.0 y superior
- Ventanas: 10/11

## Lenguajes de programación compatibles

Qoder admite todos los idiomas principales y proporciona una experiencia mejorada en:

- JavaScript, TypeScript, Python, Go, C/C++, C# y Java

## Seguridad de datos

### ¿Qoder almacenará mi código?

No. Qoder no almacena ni comparte su código. El contexto del código se utiliza durante la finalización del código, pero no se almacena.

### ¿Puedo utilizar el código generado por Qoder directamente?

El código generado por Qoder es sólo de referencia y no se garantiza su usabilidad. Los desarrolladores deben revisarlo y decidir si lo adoptan ellos mismos.

## Solución de problemas

### Si encuentro un "Error del sistema" en el modo Quest y Repo Wiki

Actualice a Qoder v0.2.1 o superior.

### El uso de CPU o memoria es demasiado alto

- Los proyectos grandes pueden utilizar muchos recursos al indexar el código.
- Agregue patrones de archivos o directorios que no requieran indexación a `.qoderignore`
- Reinicie Qoder después de editar

## apoyo

Para obtener más ayuda, contáctenos en support@qoder.com.
