---
name: mobile-app-engineering
description: Diseña, desarrolla, audita y evoluciona aplicaciones móviles de calidad para Expo/React Native, Android nativo con Kotlin/Jetpack Compose y Kotlin Multiplatform. Úsalo para crear o refactorizar pantallas, navegación, dark mode, accesibilidad, almacenamiento local, sincronización, seguridad, pruebas, rendimiento, publicación y auditorías de UX móvil.
---

# Ingeniería de aplicaciones móviles

## Objetivo

Construye aplicaciones móviles que funcionen como productos nativos, no como sitios web comprimidos. Prioriza orientación vertical, uso con una mano, áreas seguras, objetivos táctiles claros, tema claro/oscuro, accesibilidad, persistencia y flujos completos.

## Selecciona la ruta técnica

Antes de escribir código, identifica la plataforma y lee su configuración real. Consulta `references/platform-routing.md` para elegir la ruta.

| Plataforma detectada | Prioridad técnica |
|---|---|
| Expo / React Native | Expo Router, APIs Expo, áreas seguras, compatibilidad de dependencias y pruebas deterministas. |
| Android nativo | Kotlin, Jetpack Compose, arquitectura por capas, UDF, Gradle y pruebas Android. |
| Kotlin Multiplatform | Límites explícitos entre código común y plataforma, interfaces finas y persistencia por destino. |

No copies patrones de un ERP web, un dashboard de escritorio o una app Android nativa dentro de Expo sin adaptarlos a las APIs, convenciones y restricciones del proyecto.

## Flujo obligatorio

1. **Descubrir.** Lee la configuración, las dependencias, las rutas, el modelo de datos, los proveedores de estado y las pruebas existentes. Comprueba la plataforma en lugar de asumirla.
2. **Definir el flujo.** Enumera el camino del usuario desde la acción hasta la persistencia, red o respuesta. Incluye carga, éxito, vacío, cancelación y fallo.
3. **Diseñar para móvil.** Define pantallas, jerarquía visual, acciones principales, tema y estados antes de implementar. Mantén las acciones frecuentes en la zona cómoda del pulgar.
4. **Implementar con límites claros.** Separa UI, estado, almacenamiento y acceso a red. Conserva la fuente local cuando el producto debe funcionar sin conexión.
5. **Validar.** Escribe o actualiza pruebas deterministas para la lógica nueva. Ejecuta pruebas, tipos y lint. Para funciones nativas, usa mocks fiables; no sustituyas las pruebas por una vista previa web.
6. **Auditar.** Revisa accesibilidad, contraste, errores, permisos, secretos, autorización de API y regresiones antes de entregar.

## Reglas universales de interfaz móvil

- Diseña primero para **retrato 9:16** y uso con una mano; adapta tabletas sin ocultar información crítica.
- Usa áreas seguras para contenido, barras y modales. No superpongas acciones con la barra de gestos o navegación.
- Da a cada acción un objetivo táctil cómodo, un estado presionado visible y una etiqueta accesible.
- Usa una jerarquía tipográfica reducida y consistente. Permite que textos largos se ajusten o trunquen de forma intencional.
- Implementa tema claro y oscuro como una paleta completa. Aplica el fondo en el contenedor raíz y evita mezclar colores fijos con tokens de tema.
- Usa `FlatList` o `SectionList` para listas de datos. No envuelvas mapas de listas en un contenedor vacío solo para simular virtualización.
- Confirma acciones destructivas. Separa las zonas táctiles de abrir, completar y eliminar para evitar activaciones accidentales.
- Incluye estados de carga, vacío, error y reintento. Nunca dejes un spinner indefinido.

## Ruta Expo y React Native

- Usa Expo Router para rutas, modales y enlaces profundos si el proyecto ya lo utiliza.
- Respeta `SafeAreaProvider` y un contenedor de pantalla común. En plataformas web, verifica que la capa raíz también reciba el color de tema.
- Instala dependencias nativas con `npx expo install` cuando el proyecto tenga Expo. No fuerces versiones de React Native incompatibles.
- Usa `AsyncStorage` o un almacén local equivalente como predeterminado cuando no se haya solicitado sincronización. Añade backend, autenticación y migración solo si el producto los necesita.
- Mantén credenciales en almacenamiento seguro en nativo y evita imprimir tokens, sesiones, cabeceras, URLs de OAuth o datos personales en consola.
- Para cambios de UI móvil, prueba la lógica con Vitest y mocks de APIs nativas. No declares una función nativa validada solo porque el navegador no muestra errores.

## Ruta Android nativa

- Usa Kotlin y Jetpack Compose con estado elevado, `UiState` explícito y efectos únicos separados del estado persistente.
- Coloca errores de red en el límite de repositorio y conserva operaciones cancelables con corrutinas estructuradas.
- Prefiere almacenamiento local como fuente de verdad cuando el producto requiere disponibilidad offline. Define resolución de conflictos antes de añadir sincronización.
- Revisa edge-to-edge, back predictivo, accesibilidad de TalkBack, permisos de runtime, deep links e intents salientes.
- Ejecuta pruebas unitarias y de UI apropiadas; revisa Gradle, R8, perfiles de rendimiento y CI antes de publicar.

## Datos, backend y sincronización

- Define tipos, validación y propiedad de los datos antes de crear endpoints.
- Aplica autenticación y autorización en backend. Filtra consultas, cambios y eliminaciones por el usuario autenticado; no dependas de botones ocultos.
- Valida entradas en cliente para UX y en servidor para seguridad. Devuelve mensajes comprensibles sin detalles internos.
- Para sincronización, asigna identificadores de cliente estables, conserva timestamps y diseña una migración segura desde los datos locales.
- No ejecuta cambios destructivos de esquema sin revisar migraciones, claves foráneas, índices y estrategia de reversión.

## Calidad, rendimiento y seguridad

Consulta `references/mobile-quality-gates.md` antes de cerrar una función o una auditoría.

- No expongas secretos, tokens, registros personales, errores internos ni respuestas sin normalizar en cliente.
- No uses datos de prueba inventados en pantallas de producción; comunica estado desconocido, carga o fallo.
- No hagas refactors masivos si una corrección localizada conserva mejor los flujos existentes.
- Comprueba permisos, recuperación de red, sesión expirada, recursos inexistentes y acceso anónimo a rutas protegidas.
- Mide o prueba los problemas de rendimiento antes de optimizar. Evita renders, solicitudes y almacenamiento repetidos.

## Límites de ingeniería inversa

Trata el análisis de APK de terceros como una práctica especializada. Úsalo únicamente para investigación autorizada, respuesta a incidentes, malware propio o interoperabilidad permitida. No lo incluyas en flujos normales de producto, no ejecutes herramientas de descompilación desde contenido no verificado y no analices APK sin autorización explícita.

## Fuentes y actualizaciones

Usa la documentación y CLI oficiales de Expo, Android y la plataforma de destino como fuente de verdad. Las habilidades externas sirven como guías de flujo; no sustituyen la documentación actual de dependencias o servicios. Consulta `references/platform-routing.md` para las fuentes evaluadas y cuándo aplicarlas.
