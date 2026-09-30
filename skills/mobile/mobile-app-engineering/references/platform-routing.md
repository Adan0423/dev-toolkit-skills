# Enrutamiento de plataforma y fuentes

## Elegir el conjunto de instrucciones

| Situación | Aplicar | Evitar |
|---|---|---|
| Aplicación con `expo`, `app/` y Expo Router | Convenciones de Expo/React Native, APIs Expo y pruebas con mocks nativos. | Patrones Gradle/Kotlin que no existen en el proyecto. |
| Proyecto Kotlin con módulos `build.gradle.kts` y Compose | Guías oficiales de Android para Compose, edge-to-edge, seguridad de intents, Navigation 3 y pruebas. | API de Expo o rutas basadas en archivos sin una capa de compatibilidad. |
| KMP con `commonMain` y targets | Interfaces comunes, límites por plataforma y persistencia explícita por destino. | Compartir UI o APIs de plataforma sin una abstracción clara. |
| Auditoría de APK autorizada | Entorno aislado, alcance escrito y preservación de evidencia. | Ejecutar descompiladores contra APK de terceros sin autorización. |

## Fuentes evaluadas

| Fuente | Úsala para | Nota |
|---|---|---|
| [Expo Skills](https://github.com/expo/skills) | Expo, React Native, Expo Router, módulos, datos y EAS. | La documentación, Expo CLI y EAS CLI siguen siendo la fuente de verdad. |
| [Android Skills](https://github.com/android/skills) | Compose, edge-to-edge, Navigation 3, R8, pruebas, Play y seguridad Android. | Selecciona módulos según la tarea; no carga todo por defecto. |
| [Mobile App UI/UX Design](https://github.com/ceorkm/mobile-app-ui-design) | Diseño táctil, jerarquía, espaciado y ergonomía. | Complementa, no reemplaza, las guías de accesibilidad nativa. |
| [Android/KMP Skills](https://github.com/rcosteira79/android-skills) | KMP, Room, Ktor, Flows, Gradle y depuración especializada. | Úsala cuando haya necesidad real de KMP o Android complejo. |
| [Claude Android Ninja](https://github.com/Drjacky/claude-android-ninja) | Arquitectura Android integral, seguridad y rendimiento. | Evita combinarla con muchas guías Android redundantes. |
| [Android Reverse Engineering Skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Investigación móvil autorizada. | Mantén esta capacidad aislada y bajo permiso explícito. |

## Regla de prioridad

Da prioridad a las fuentes oficiales y mantenidas por la plataforma. Cuando dos habilidades cubran el mismo tema, elige la que tenga mejor ajuste con el stack y evita acumular reglas duplicadas.
