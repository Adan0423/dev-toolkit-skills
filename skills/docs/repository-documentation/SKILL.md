---
name: repository-documentation
description: >-
  Audita y mantiene documentación de repositorios seleccionando revisión documental,
  creación/mejora de README o actualización desde cambios Git. Úsalo para documentación
  técnica basada en el código real; no para escritura editorial o comunicación general.
---

# Repository Documentation

Analiza el proyecto antes de documentar: instrucciones, manifests, configuración,
comandos, rutas, pruebas y cambios relevantes. Redacta en español salvo elección del
usuario. No inventa stack, features, URLs, despliegues ni comandos ejecutados.

| Solicitud | Guía |
|---|---|
| Auditar, ordenar o reconciliar documentación con implementación | [audit](references/specialties/audit/guide.md) |
| Crear/mejorar README o guía de inicio con evidencia | [readme](references/specialties/readme/guide.md) |
| Actualizar documentación por commits/diff/release existente | [changes](references/specialties/changes/guide.md) |

Lee una guía inicial; no ejecuta auditoría completa para corregir un párrafo. En changes
confirma base/tag/branch real; ausencia de tag no autoriza inventar uno, crear release
ni publicar. Changelog/release notes solo si corresponden al alcance y convenciones.
Las guías son procedimientos locales con sus recursos relativos, no invocaciones
recursivas. Conserva enlaces/rutas y evita borrar documentos sin revisar sus usos.

Verifica links y comandos pertinentes cuando se puedan ejecutar; distingue documentación
confirmada de operación no probada. No publica ni empuja cambios sin autorización.
Coautoría, humanización o comunicaciones son objetivos distintos: usa otras skills
disponibles solo si el usuario solicita ese trabajo, sin cargarlas por defecto.
