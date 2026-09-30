---
name: react-engineering
description: >-
  Implementa, revisa y moderniza aplicaciones React/TypeScript seleccionando solo la
  especialidad necesaria de arquitectura, componentes/datos, rendimiento o React Router.
  Úsalo para desarrollo funcional React; el diseño visual tiene una familia independiente.
---

# React Engineering

Entrada de la familia React. Inspecciona dependencias, router, renderizado, patrones y
pruebas del proyecto antes de proponer cambios. Conserva stack y contratos salvo que
el alcance requiera cambiarlos. No instala React nuevo ni migra framework por rutina.

## Selección de especialidad

| Necesidad principal | Guía que debes leer |
|---|---|
| Estructura, límites de componentes, hooks y estrategia de pruebas | [architecture](references/specialties/architecture/guide.md) |
| Implementar pantalla, formulario, hooks o carga/estados de datos | [implementation](references/specialties/implementation/guide.md) |
| Lentitud, renders, bundles, waterfalls o revisión de performance | [performance](references/specialties/performance/guide.md) |
| Modernizar arquitectura o evaluar capacidades de versiones actuales | [modernization](references/specialties/modernization/guide.md) |
| React Router en modo framework: loaders/actions, SSR, sesión y errores | [routing](references/specialties/routing/guide.md) |

Lee una guía inicial y solo sus recursos pertinentes. Añade otra únicamente si aparece
una necesidad independiente real; no recorrer toda la tabla ni inferir migración de
una petición de formulario. Next.js/Nuxt u otro router no debe convertirse a React Router.
Un bug local suele necesitar implementation; una auditoría de rendimiento performance.

## Contrato común

Las guías son procedimientos internos, no skills a registrar ni comandos que deban
invocarse recursivamente. Rutas relativas de cada guía se resuelven desde su carpeta.
No cargar otras familias por palabras citadas incidentalmente. Si una recomendación
es de otra versión, verificar código/documentación oficial antes de usarla.
Fuentes históricas no convierten React 2026 en versión obligatoria.

Confirma estados loading/empty/error/denied y permisos reales. Preserva rutas, APIs,
accesibilidad y comportamiento. Valida con build/checks relevantes y escenario afectado;
no añade tests que solo replican el código. No publica/despliega como efecto implícito.
Entrega cambios, pruebas, límites y guía elegida. Para identidad visual usa una skill
disponible apropiada, o criterios propios, sin dependencia de instalación obligatoria.
