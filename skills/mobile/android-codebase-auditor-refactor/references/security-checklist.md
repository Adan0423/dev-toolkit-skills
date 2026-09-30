# Android Security Checklist

## Principio

No etiquetar un patrón como vulnerabilidad explotable sin contexto. Distinguir señal, riesgo y vulnerabilidad confirmada.

## Almacenamiento local

Buscar:

- `SharedPreferences`, `PreferenceManager`, `getSharedPreferences`;
- tokens, refresh tokens, session IDs, passwords, API secrets o PII almacenada sin protección;
- bases de datos o archivos con contenido sensible sin controles adecuados;
- backups que puedan incluir secretos.

Para información sensible, evaluar una estrategia basada en Android Keystore y cifrado del payload. DataStore no cifra automáticamente: si se usa para secretos, requiere una capa de cifrado adecuada.

No introducir dependencias criptográficas obsoletas sin comprobar su estado actual y compatibilidad.

## Secretos hardcodeados

Buscar valores reales asociados a términos como:

- `API_KEY`
- `SECRET`
- `CLIENT_SECRET`
- `PASSWORD`
- `TOKEN`
- `PRIVATE_KEY`
- `Authorization`
- `Bearer`

Evitar falsos positivos: nombres de variables o placeholders no equivalen a secretos reales.

Tratar cualquier credencial incluida en el APK como potencialmente recuperable. `BuildConfig`, resources y constantes no son bóvedas de secretos.

## Red y TLS

Buscar:

- `http://` fuera de localhost/emulador/dev;
- `android:usesCleartextTraffic="true"`;
- configuraciones permisivas de `networkSecurityConfig`;
- TrustManagers que aceptan todos los certificados;
- `HostnameVerifier` que siempre retorna `true`;
- `SSLContext` personalizado sin validación robusta;
- certificate pinning roto o bypass intencional.

Un bypass TLS en producción normalmente es `CRITICAL`.

## Logging

Buscar `Log.*`, Timber, `println`, `printStackTrace` e interceptores HTTP.

Escalar cuando se registren:

- Authorization/Bearer;
- cookies;
- access/refresh tokens;
- passwords;
- datos personales;
- request/response bodies sensibles;
- session IDs.

`HttpLoggingInterceptor.Level.BODY` debe estar limitado a builds apropiados y no exponer secretos.

## AndroidManifest y componentes

Revisar:

- `android:exported`;
- `allowBackup`;
- `debuggable`;
- `usesCleartextTraffic`;
- custom permissions;
- Activities/Services/Receivers/Providers exportados;
- intent filters y deep links;
- FileProvider paths;
- permisos de alto riesgo.

Todo componente exportado necesita una justificación funcional y controles coherentes.

## WebView

Revisar:

- `javaScriptEnabled`;
- `addJavascriptInterface`;
- `allowFileAccess`;
- `allowContentAccess`;
- `mixedContentMode`;
- WebView debugging;
- navegación a orígenes no confiables;
- validación de URLs/deep links.

## Sesión y autenticación

Comprobar:

- centralización de refresh token;
- borrado seguro al logout;
- evitar tokens en logs/analytics/exceptions;
- manejo de 401 concurrentes;
- no persistir credentials innecesariamente;
- no duplicar lógica de sesión por pantalla.

## Migración de almacenamiento sensible

Plan recomendado:

1. identificar formato y ubicación legacy;
2. seleccionar mecanismo seguro compatible;
3. leer dato antiguo;
4. cifrar/persistir en destino;
5. verificar lectura del nuevo formato;
6. eliminar el valor inseguro;
7. manejar rollback/errores sin destruir sesión;
8. añadir tests de migración cuando sea viable.
