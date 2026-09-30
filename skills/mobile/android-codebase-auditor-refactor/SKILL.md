---
name: android-codebase-auditor-refactor
description: Audita repositorios Android/Kotlin de forma autónoma para detectar deuda técnica, archivos monolíticos, violaciones de arquitectura, problemas de estabilidad y vulnerabilidades de seguridad. Úsalo cuando el usuario pida revisar, modernizar o refactorizar una app Android, especialmente con archivos >300 líneas, God Classes, Compose/ViewModels sobredimensionados, almacenamiento sensible inseguro o acoplamiento UI-data.
compatibility: Diseñado para agentes de código con acceso de lectura al repositorio Android; la fase de refactorización requiere capacidad de editar archivos y ejecutar Gradle. Python 3 es opcional para scripts/audit_android_repo.py.
metadata:
  version: "1.0.0"
  tags: "android,kotlin,clean-architecture,security,refactoring"
---

# Android Codebase Auditor & Refactor

## Objetivo

Auditar primero y refactorizar después, de forma incremental, aplicaciones Android monolíticas o frágiles. Prioriza seguridad, estabilidad, conservación del comportamiento, compilación continua y separación clara de responsabilidades.

## Regla principal

Empieza siempre en modo **AUDIT / read-only**. No crees, edites, muevas, renombres ni elimines archivos durante el diagnóstico. Solo entra en modo **REFACTOR** después de que el usuario confirme explícitamente el plan de cambios presentado tras la auditoría.

## Cuándo activar este Skill

Actívalo cuando ocurra al menos una de estas condiciones:

- El usuario pide auditar, refactorizar, modernizar, modularizar, estabilizar o securizar una aplicación Android.
- Hay archivos Kotlin de más de 300 líneas o clases/composables/viewmodels con múltiples responsabilidades.
- Existe cualquier archivo Kotlin de más de 1000 líneas.
- La UI accede directamente a Retrofit, OkHttp, Room, SQLite, SharedPreferences, DataStore, Firebase u otra infraestructura.
- Se detectan posibles secretos hardcodeados, tráfico HTTP inseguro, TLS debilitado o logs sensibles.
- El usuario pide aplicar MVVM, MVI, Clean Architecture, separar ViewModels, extraer UseCases/Repositories o dividir Composables.
- Una modificación solicitada aumentaría claramente la deuda técnica de un componente ya monolítico.

## Entradas esperadas

Acepta uno o más de estos insumos:

- repositorio Android completo;
- carpeta o módulo Android;
- diff/PR;
- archivos Kotlin/XML/Gradle específicos;
- reporte de crashes o problemas de estabilidad;
- instrucciones del usuario sobre el alcance.

Si el repositorio está disponible, inspecciona el código real antes de inferir arquitectura, contratos, dependencias o comportamiento.

## Fase 0 — Descubrimiento

1. Identifica módulos y configuración desde `settings.gradle[.kts]`, `build.gradle[.kts]`, `gradle.properties`, `libs.versions.toml` y manifests.
2. Detecta Kotlin, Compose, Views/XML, Hilt/Dagger/Koin, Room, Retrofit/OkHttp, DataStore, Firebase, Navigation, WorkManager, Paging, Coroutines/Flow y frameworks de test.
3. Construye un mapa de módulos y dependencias sin modificar archivos.
4. Localiza `src/main`, `src/test` y `src/androidTest`.

## Fase 1 — Auditoría pasiva obligatoria

### 1. Inventario de tamaño

- Cuenta líneas de todos los `.kt`.
- Marca >300 líneas como deuda técnica relevante.
- Marca >1000 líneas como monolítico crítico.
- Ordena los hallazgos de mayor a menor tamaño.
- No uses tamaño como único criterio: evalúa responsabilidades, acoplamiento y riesgo.

Puedes ejecutar `python3 scripts/audit_android_repo.py <repo>` si el entorno lo permite. El script es read-only y solo produce diagnóstico.

### 2. Arquitectura y responsabilidades

Detecta:

- Activities/Fragments con lógica de negocio;
- Composables con networking, persistencia, validación o navegación excesiva;
- ViewModels que mezclen estado, dominio, infraestructura, permisos, analytics o sesión;
- acceso directo UI → DAO/API/storage;
- repositorios que mezclen demasiadas responsabilidades;
- modelos reutilizados indiscriminadamente entre API, DB, dominio y UI;
- dependencias circulares o capas que apunten en dirección incorrecta.

Mapea la arquitectura real y compárala con una separación pragmática `presentation → domain ← data`.

### 3. Seguridad estricta

Busca como mínimo:

- `SharedPreferences`, `PreferenceManager` y `getSharedPreferences` usados para datos sensibles;
- API keys, client secrets, passwords, tokens, private keys o credenciales hardcodeadas;
- URLs `http://` de producción;
- `usesCleartextTraffic`, `networkSecurityConfig`, TrustManagers/HostnameVerifiers inseguros;
- `HttpLoggingInterceptor.Level.BODY` en producción;
- logs que expongan tokens, Authorization, cookies, passwords, sesiones o PII;
- componentes `android:exported`, WebView insegura, backups/debuggable y permisos sensibles.

Lee [references/security-checklist.md](references/security-checklist.md) cuando aparezca cualquiera de estas señales.

### 4. Estabilidad

Busca:

- abuso de `!!`, casts inseguros, `lateinit`, `first()`/`single()` sin garantías;
- `GlobalScope`, `runBlocking`, jobs fuera del lifecycle y errores de coroutines no gestionados;
- side effects durante composición, recomposiciones evitables y operaciones costosas en UI;
- observers/listeners con riesgo de fuga;
- excepciones silenciadas o convertidas indiscriminadamente en `null`;
- ausencia de timeout, retry controlado o estado de error en flujos críticos.

### 5. Informe inicial

Antes de cualquier cambio entrega:

- resumen ejecutivo;
- arquitectura actual;
- número de `.kt`;
- archivos >300 y >1000 líneas;
- hallazgos de seguridad;
- riesgos de estabilidad;
- deuda arquitectónica;
- cobertura/pruebas observables;
- tabla de impacto con ID, archivo, evidencia, severidad, prioridad y acción recomendada;
- arquitectura objetivo y orden incremental de refactorización;
- archivos que probablemente se crearían/modificarían/eliminarían;
- comandos de compilación/test que usarías para validar.

Usa las severidades `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO` y prioridades `P0` a `P3` descritas en [references/audit-checklist.md](references/audit-checklist.md).

## Gate obligatorio de autorización

Tras el diagnóstico:

1. Declara explícitamente que no se modificó ningún archivo.
2. Presenta el plan incremental y su alcance.
3. Solicita confirmación explícita del usuario para ejecutar la refactorización.
4. Si no hay confirmación inequívoca, detente en modo AUDIT.

Una autorización limitada a un módulo o conjunto de archivos no autoriza cambios globales.

## Fase 2 — Refactorización incremental

Solo después de autorización explícita.

### Reglas de tamaño

- Objetivo normal: 50–150 líneas por archivo nuevo o extraído.
- Máximo recomendado: 200 líneas.
- Si un archivo nuevo/refactorizado supera 200 líneas, vuelve a evaluar responsabilidades antes de continuar.
- No fragmentes artificialmente una unidad cohesionada solo para cumplir una métrica.

### Orden preferido

Adapta el orden a las dependencias reales, pero prefiere:

1. modelos/contratos;
2. data sources;
3. repositorios;
4. UseCases/reglas de dominio;
5. ViewModels y UiState/UiEvent;
6. UI/Composables;
7. navegación/integración;
8. eliminación del legacy ya reemplazado.

Para archivos >1000 líneas aplica estrategia strangler: extrae una responsabilidad independiente, compila/prueba y continúa. Nunca hagas una reescritura masiva de una sola vez salvo que el usuario lo pida expresamente y exista una razón técnica clara.

### Compose

- Extrae componentes por responsabilidad visual.
- Haz stateless los Composables reutilizables siempre que sea razonable: `state in, events out`.
- Separa Route/Screen/Content/Sections/Components/Dialogs cuando aporte claridad.
- No permitas que componentes reutilizables conozcan DAO, Retrofit, repositorios o almacenamiento.

### ViewModels y estado

- Mantén el ViewModel como coordinador de UI y dominio.
- Extrae reglas de negocio a UseCases cuando representen operaciones coherentes.
- Usa `UiState` explícito; puede ser `sealed interface` o `data class` según el caso.
- Usa eventos explícitos cuando reduzcan ambigüedad; no introduzcas jerarquías ceremoniales para pantallas simples.

### Repositories y data

- Evita UI → infraestructura directa.
- Mantén contratos de repositorio en dominio cuando Clean Architecture sea apropiada.
- Mantén implementaciones y detalles de Retrofit/Room/DataStore/Firebase en data.
- Introduce DTO/Entity/Domain/UI models y mappers solo cuando sus responsabilidades difieran realmente.

### Seguridad

Si hay datos sensibles en SharedPreferences estándar, incluye su migración en el plan aprobado. Prefiere una solución actual y soportada para el proyecto, por ejemplo:

- DataStore con cifrado del payload y claves gestionadas por Android Keystore; o
- una solución de almacenamiento cifrado compatible con la versión/stack existentes.

No asumas que `androidx.security:security-crypto` es la mejor opción sin comprobar compatibilidad, mantenimiento y dependencias del proyecto. Si el código existente ya usa `EncryptedSharedPreferences`, evalúa su estado y una migración segura antes de reemplazarlo.

La migración debe preservar datos/sesiones cuando sea razonable: leer formato antiguo → persistir de forma segura → verificar → retirar dato inseguro.

## Validación continua

Después de cada cambio estructural significativo:

1. corrige imports, visibilidad, packages, DI y referencias;
2. ejecuta el task Gradle más pequeño que valide el módulo, por ejemplo `./gradlew :app:compileDebugKotlin` o equivalente;
3. si falla por tu cambio, detente, corrige y vuelve a ejecutar;
4. ejecuta tests relevantes (`test`, tests del módulo y, si el entorno lo permite, instrumentación);
5. no continúes acumulando cambios sobre una base rota.

Lee [references/refactor-playbook.md](references/refactor-playbook.md) antes de una refactorización amplia.

## Guardrails obligatorios

- **Read-only primero:** ningún cambio antes del diagnóstico.
- **Confirmación humana:** ningún cambio de código sin aprobación explícita posterior al diagnóstico.
- **Sin placeholders:** no introduzcas comentarios de implementación pendiente, funciones vacías para “hacer compilar”, fragmentos sustituidos por texto genérico ni marcadores de posición.
- **Sin código inventado:** no inventes endpoints, DTOs, claves, tablas, rutas de navegación, interfaces ni contratos que no existan o no estén autorizados.
- **Cambios pequeños y reversibles:** conserva comportamiento salvo bug/vulnerabilidad demostrada o instrucción explícita.
- **No big-bang:** evita reescrituras masivas de legacy cuando pueda migrarse incrementalmente.
- **Scope control:** no amplíes silenciosamente el alcance aprobado.
- **Git safety:** no ejecutes `git reset --hard`, `git clean -fd`, `git checkout .` ni comandos equivalentes destructivos.
- **No mezclar refactor y feature:** separa mantenimiento de nueva funcionalidad salvo autorización.
- **No segundo framework DI:** conserva Hilt/Dagger/Koin existente salvo decisión explícita y justificada.
- **No upgrades masivos incidentales:** separa actualización de dependencias de la refactorización cuando sea posible.
- **Seguridad no negociable:** nunca debilites TLS, autenticación, permisos o almacenamiento para simplificar código o tests.

## Formato de salida del diagnóstico

Usa [assets/diagnostic-report-template.md](assets/diagnostic-report-template.md) como plantilla. Cada hallazgo debe estar respaldado por evidencia concreta del repositorio (archivo, símbolo, línea/rango cuando esté disponible).

## Criterios de finalización

Una refactorización se considera terminada únicamente cuando:

- el alcance aprobado está implementado;
- compila el proyecto o los módulos afectados;
- los tests relevantes pasan, o se documentan fallos preexistentes/no relacionados;
- no quedan imports/referencias rotas;
- no quedaron placeholders ni código deliberadamente incompleto;
- los archivos nuevos/refactorizados respetan el objetivo de tamaño o documentan una excepción cohesionada;
- los riesgos de seguridad incluidos en el alcance fueron corregidos o quedaron explícitamente documentados;
- se entrega un informe final con antes/después, archivos tocados y resultados de validación.

## Prioridad global

Aplica esta jerarquía al tomar decisiones técnicas:

`seguridad → estabilidad → comportamiento correcto → arquitectura → mantenibilidad → optimización`
