# Puertas de calidad móvil

## Antes de implementar

| Área | Verificación |
|---|---|
| Flujo | Define inicio, éxito, vacío, error, cancelación y reintento. |
| Datos | Identifica propiedad, validación, almacenamiento y sincronización. |
| Diseño | Define orientación, área segura, zona del pulgar, jerarquía y dark mode. |
| Seguridad | Identifica permisos, credenciales, datos sensibles y autorización de API. |

## Antes de entregar

| Área | Verificación |
|---|---|
| Función | Todos los botones finalizan en una acción controlada; no hay rutas muertas. |
| Accesibilidad | Etiquetas, roles, estados, contraste, foco y objetivos táctiles son adecuados. |
| Tema | Claro y oscuro aplican fondo, superficies, texto, bordes y estado de sistema. |
| Resiliencia | Carga, errores, red, sesión expirada y datos dañados no dejan la app bloqueada. |
| Seguridad | No hay secretos ni tokens en consola; backend protege propiedad de recursos. |
| Rendimiento | Las listas se virtualizan y las operaciones repetidas se eliminan o justifican. |
| Validación | Ejecuta pruebas, tipos y lint; usa pruebas nativas deterministas cuando aplique. |
