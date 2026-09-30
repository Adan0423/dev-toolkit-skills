# Android Audit Checklist

## Severidad

- `CRITICAL`: secreto real expuesto, TLS deliberadamente inseguro, pérdida de datos, vulnerabilidad explotable o crash recurrente en flujo principal.
- `HIGH`: almacenamiento sensible sin protección, God Class severa, archivo >1000 líneas, acoplamiento arquitectónico fuerte o alta probabilidad de fallo.
- `MEDIUM`: archivo >300 líneas, duplicación importante, responsabilidades mezcladas o testabilidad deficiente.
- `LOW`: deuda localizada, inconsistencias menores o mantenibilidad limitada sin impacto inmediato.
- `INFO`: observación útil sin defecto confirmado.

## Prioridad

- `P0`: atender inmediatamente.
- `P1`: corregir antes de ampliar funcionalidad relacionada.
- `P2`: siguiente ciclo de mantenimiento/refactor.
- `P3`: mejora opcional.

La prioridad depende de impacto, exposición, frecuencia y blast radius, no solo del tamaño del archivo.

## Inventario mínimo

Inspeccionar:

- `settings.gradle`, `settings.gradle.kts`
- `build.gradle`, `build.gradle.kts`
- `gradle.properties`
- `libs.versions.toml`
- `AndroidManifest.xml`
- `proguard-rules.pro`, `consumer-rules.pro`
- `src/main`, `src/test`, `src/androidTest`

Ignorar por defecto artefactos generados como `build/`, `.gradle/`, `.idea/` y equivalentes, salvo que una evidencia apunte allí.

## Tamaño y complejidad

Clasificación orientativa:

| Líneas | Estado |
|---:|---|
| 0–150 | saludable |
| 151–200 | aceptable; revisar cohesión |
| 201–300 | advertencia |
| 301–500 | deuda técnica |
| 501–1000 | alta complejidad |
| >1000 | monolítico crítico |

Además del LOC, revisar métodos largos, demasiadas dependencias constructoras, múltiples estados mutables, nesting, callbacks encadenados, lógica heterogénea y responsabilidades incompatibles.

## Arquitectura

Determinar si el proyecto se aproxima a MVC, MVP, MVVM, MVI, Clean Architecture, híbrida o sin patrón consistente.

Registrar dependencias problemáticas como:

- UI → Retrofit/OkHttp
- UI → Room/DAO
- UI → SharedPreferences/DataStore
- ViewModel → DAO/API sin abstracción cuando hay lógica de dominio relevante
- domain → Android framework/data implementation
- dependencias circulares entre módulos

No imponer capas sin beneficio. Interfaces de una sola implementación pueden ser válidas si aportan boundary, testabilidad o inversión de dependencias; no crearlas por ceremonial.

## Compose

Revisar:

- Composables demasiado grandes;
- state hoisting;
- side effects;
- `LaunchedEffect`/`DisposableEffect` mal delimitados;
- acceso directo a ViewModel en componentes reutilizables;
- operaciones costosas durante composición;
- llamadas a infraestructura desde UI;
- recomposición por estado demasiado amplio.

## ViewModels

Buscar mezcla de:

- networking;
- persistencia;
- validación;
- navegación;
- reglas de negocio;
- permisos;
- analytics;
- sesión/autenticación;
- transformación pesada de datos.

Preferir extraer operaciones de negocio coherentes, no wrappers triviales.

## Estabilidad Kotlin/Coroutines

Revisar:

- `!!` con inputs opcionales;
- casts inseguros `as`;
- `lateinit` con lifecycle incierto;
- `first()`/`single()` sin garantías;
- `GlobalScope`;
- `runBlocking` en caminos UI;
- collectors duplicados;
- jobs sin lifecycle;
- excepciones no gestionadas;
- carreras en refresh/session/cache;
- `catch (Exception)` vacío o pérdida de error.

## Pruebas

Registrar:

- unit tests disponibles;
- tests de ViewModel/domain/data;
- instrumented/UI tests;
- tasks Gradle ejecutables;
- cobertura observable si existe reporte;
- áreas críticas sin tests que eleven el riesgo de refactor.

## Evidencia y reporte

Cada hallazgo debe incluir:

- ID estable (`SEC-001`, `ARCH-001`, `STAB-001`, etc.);
- archivo y símbolo;
- línea/rango si está disponible;
- evidencia breve;
- impacto técnico;
- severidad;
- prioridad;
- acción concreta;
- dependencias o riesgos del cambio.
