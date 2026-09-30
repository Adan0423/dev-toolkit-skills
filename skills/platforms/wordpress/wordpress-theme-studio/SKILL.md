---
name: wordpress-theme-studio
description: >-
  Crea y personaliza temas WordPress con código propio, clásicos o de bloques,
  diseño responsive y modo oscuro. Úsalo para desarrollar temas, integrar skills
  de diseño, cargar artículos y medios, configurar sitios y operar mediante
  WordPress MCP, REST API, WP-CLI o el administrador según acceso disponible.
---

# WordPress Theme Studio

Desarrolla temas utilizables y contenido editable en WordPress, con PHP, HTML, CSS,
JavaScript y APIs nativas. Trabaja en español salvo otra necesidad del usuario.
Código propio no excluye Gutenberg/theme.json: evita exigir builders comerciales.
No entregues una maqueta HTML desconectada del CMS como si fuera un tema terminado.

## Flujo

1. Inspecciona instalación/repositorio: WordPress/PHP, modalidad .org/.com, tema activo,
   plugins, multisite, editor, hosting, despliegue, contenido, SEO y permisos reales.
   Confirma sitio/entorno antes de mutar. No asumas acceso al servidor por tener MCP.
2. Identifica objetivo, audiencia y páginas. Elige tema de bloques, clásico, híbrido
   o tema hijo según compatibilidad y edición requerida. Conserva datos y negocio.
   Para modificar un tema ajeno actualizable usa hijo o extensión, no tema padre.
3. Aplica diseño: lee [design.md](references/design.md), descubre skills disponibles,
   usa la indicada por el usuario o la adecuada. Traduce diseño a WordPress sin
   perder contenido editable, hooks o accesibilidad. No requiere otra skill instalada.
4. Implementa siguiendo [theme-engineering.md](references/theme-engineering.md).
   Integra contenido real, archivos, búsqueda, vacíos y errores, no solo portada.
5. Gestiona artículos, medios y ajustes con [content-operations.md](references/content-operations.md).
   Si necesitas acceso externo lee [connections.md](references/connections.md):
   descubre capacidades reales de MCP, REST o CLI y conserva autorización de publicación.
6. Valida [quality.md](references/quality.md): instalación WordPress, edición, responsive,
   claro/oscuro, teclado, funcionalidad y salida pública. Empaqueta el tema y entrega
   código/configuración reproducibles; declara qué falta probar o publicar.

Fuentes oficiales: [sources.md](references/sources.md). Revalida APIs/políticas para
la versión encontrada; investigación inicial 30 de septiembre de 2026. Sin navegación,
explica lo no revalidado, sin inventar funciones de plugins o del plan.

## Requisitos de aceptación

- Responsive continuo en móviles, tablets, desktop, orientación y zoom; comprobar
  rangos y anchos de quality.md, no prometer compatibilidad solo por añadir media queries.
- Claro, oscuro y preferencia del sistema, elección persistente y sin destello evitable.
  Usabilidad/contraste de todas las superficies y contenido del editor.
- Contenido gestionable desde WordPress: entradas, páginas, medios, taxonomías,
  navegación y ajustes pertinentes; evitar textos principales incrustados en código.
- Theme ZIP instalable con slug/estructura correctos, dependencias y versión PHP/WP
  documentadas para el proyecto. No incluir secretos ni directorios de desarrollo.
- La lógica que debe sobrevivir al cambio de tema vive en plugin, no en el tema.
- Nunca editar core, bypass de capacidades, publicación accidental, credenciales en
  código, SQL directo como sustituto de APIs ni borrar contenido para mostrar demos.

## Alcance y bloqueos

Crear un tema no autoriza activar en producción, instalar plugins externos o publicar
artículos. Ejecuta esas acciones cuando la petición ya las autorice y el acceso lo
permita, sin confirmaciones repetidas. Si piden cargar contenido sin estado explícito,
crea borradores y reporta; si piden publicar, verifica y publica lo autorizado.
No contactes terceros ni compres servicios como parte implícita de una configuración.
Si no puedes acceder, prepara ZIP/parches, contenido importable y guía exacta con
valores y verificación; no afirmes instalación, carga o publicación sin evidencia.

## Entregables

Entrega resultado, arquitectura/skills usadas, pruebas, ZIP/ruta, estado de activación
y URLs/IDs de contenido cuando existan, con pendientes concretos. Usa
[entrega-wordpress.md](assets/entrega-wordpress.md) para proyectos amplios.
Si SEO/GEO entra en alcance, usa seo-geo-web si está disponible; conserva el gestor
SEO existente y no dupliques canonical/schema.
