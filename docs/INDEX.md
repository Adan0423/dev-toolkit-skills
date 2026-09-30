# 📚 Documentación del Toolkit de Skills


[Paletas profesionales: nueva skill y guía de uso](skills/color-palettes.md).

> Guía completa de uso, instalación y referencia de todas las skills y prompts disponibles.

## 🚀 Inicio Rápido

- [Guía de Instalación](install/quickstart.md) — Cómo instalar skills (`.skill`, `.zip`) y cuándo usar `SKILL/` vs `skills/`

## 🧠 Skills

- [Bases de datos: modelado y seguridad](skills/database-engineering.md) — SQL/NoSQL, migraciones, permisos y MCP compatible.

- [Marketing profesional](skills/marketing-skills.md) — Estrategia, contenido, Meta Ads, Google Ads, TikTok Ads y medición.

- [Familias con carga selectiva](skills/family-skills.md) — Siete skills principales y 34 especialidades internas.

- [Skills Listadas (`SKILL/` — Listas para Usar)](skills/skill-packages.md) — 64 paquetes (57 nombres de skill). Formato listo para producción, sin compilación.
- [Skills Fuente (`skills/` — Desarrollo/Pruebas)](skills/source-skills.md) — 110 skills únicas, incluyendo especialistas anidados. Úsalas para desarrollo, pruebas y mejora.

- [Auditoría y propuesta de agrupación](skills/organization-review.md) — Fuentes recuperadas, variantes y mejoras para las 95 skills.

## 💬 Prompts

- [Prompts Disponibles](prompts/README.md) — 68 prompts: imagen, edición, web y repositorio.

## 🗂️ Archivos de Referencia

- [README Principal](../README.md) — Vista general del repositorio
- [docs_structure.json](../docs_structure.json) — Índice documental para carga en otros proyectos
- [skills-lock.json](../skills-lock.json) — Lockfile de skills

## Diferenciación Clave

| Directorio | Propósito | Estado | Cuándo usar |
|---|---|---|---|
| **`SKILL/`** | Paquetes autocontenidos (`.skill`, `.zip`) | **Listos para usar** | Instalación directa en agentes. Sin compilación/rebuild. |
| **`skills/`** | Código fuente + `SKILL.md` + referencias/scripts | **Desarrollo/Pruebas** | Para modificar, mejorar, debuggear o entender implementación. |
| **`prompts/`** | Plantillas Markdown reutilizables | **Listos para usar** | Invocar como prompts base en tareas recurrentes. |
