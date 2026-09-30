---
name: wordpress-elementor-commerce
description: >-
  Crea, rediseña y administra sitios WordPress con Elementor, WooCommerce y plugins.
  Úsalo para diseño moderno editable, responsive móvil/tablet/desktop, modo oscuro,
  artículos, productos y configuración; opera mediante MCP, editor, REST o WP-CLI
  según capacidades y acceso reales.
---

# WordPress Elementor Commerce

Construye sitios y tiendas que el usuario pueda editar con Elementor y WordPress.
Trabaja en español salvo otra necesidad. Usa plugins pertinentes y skills de diseño
disponibles, preservando contenido y lógica comercial existentes. No conviertas un
rediseño visual en una reconstrucción de la tienda ni entregues solo imágenes/mockups.

## Flujo de ejecución

1. Inspecciona sitio y entorno antes de editar: WP/PHP, tema, Elementor/editor,
   Free/Pro/plan, WooCommerce, plugins/addons, kit global, plantillas/condiciones,
   contenido, checkout, caché, idiomas y acceso. Confirma sitio objetivo mediante lectura.
2. Define páginas, audiencia, identidad y conversión. Aplica la skill de diseño
   indicada por el usuario, o descubre una adecuada y lee su SKILL.md. Adapta sus
   decisiones a elementos editables nativos; no depende de un catálogo fijo de skills.
3. Diseña e implementa siguiendo [elementor.md](references/elementor.md) y
   [responsive-dark.md](references/responsive-dark.md). Prioriza tokens globales,
   componentes reutilizables y contenido dinámico, con estados reales.
4. Usa [connections-plugins.md](references/connections-plugins.md) para descubrir MCP
   Elementor/WordPress y elegir plugins/acceso. MCP es preferente cuando resuelve
   la tarea, no requisito para bloquear el trabajo si no existe o no permite escribir.
5. Para tienda lee [woocommerce.md](references/woocommerce.md); para artículos,
   medios y ajustes lee [content.md](references/content.md). No mezcles páginas de
   maquetación con la fuente de verdad de productos, precios, stock o pedidos.
6. Comprueba [quality.md](references/quality.md), incluyendo frontend, editor y
   persistencia. Entrega IDs/URLs, plantillas/archivos exportables, configuración,
   pruebas y pendientes. Publica solo lo autorizado, sin confirmaciones repetidas.

Fuentes: [sources.md](references/sources.md), investigadas el 30 de septiembre de 2026.
Revalida compatibilidad, planes y APIs al ejecutar. Usa solo referencias pertinentes.
Sin consulta actual, identifica lo no revalidado en lugar de inventar opciones.
Plantilla de entrega: [entrega-sitio.md](assets/entrega-sitio.md).

## Requisitos

- Responsive continuo: móvil, tablet, desktop, anchos intermedios, orientación y zoom.
  No declares "100% responsive" únicamente por activar tres vistas del editor.
- Modo Sistema/Claro/Oscuro con elección persistente, contraste y sin inversión global
  de imágenes. Prueba formularios, popups, tienda y plugins, no solo portada.
- Edición real en Elementor y WordPress; texto, imágenes, artículos y productos siguen
  siendo gestionables. Evita un sitio entero incrustado en un widget HTML.
- Plugins con necesidad concreta, origen fiable, compatibilidad y sin duplicados.
  No usar software nulled, activar funciones pagadas sin licencia ni comprar planes.
- Preserva datos, SEO, formularios, navegación, permisos y comercio. No editar core ni
  archivos del plugin/tema padre. Código complementario en hijo/plugin propio si procede.
- Crear diseño no autoriza cambiar pasarelas, impuestos, envíos, pedidos o reembolsos.
  No realizar cobros/pruebas financieras reales como efecto implícito del QA.

## Alcance y límites

Una solicitud de implementación autoriza trabajo necesario dentro del alcance, pero
no publicar contenido nuevo, instalar servicios de pago ni modificar producción sin
que la petición lo contemple. Cargar artículos sin estado explícito: borrador;
publicarlos si el usuario ya lo pidió. No pedir contraseñas en chat ni guardar secretos.
Si faltan permisos/licencia/conector, prepara plantillas compatibles, contenido,
configuración y pasos con valores concretos. Diferencia preparado, guardado, publicado
y verificado. No afirmar carga/edición de un sitio sin evidencia.

SEO/GEO: integra seo-geo-web si disponible y pertinente, conservando gestor existente.
Temas nuevos con código propio: wordpress-theme-studio si corresponde; este skill se
centra en builder, plugins y operación del sitio, sin exigir esos skills como dependencia.
