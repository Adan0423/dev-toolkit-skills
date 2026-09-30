# Pruebas y aceptación

## Integración real

PHP lint de archivos modificados y JSON/markup de bloques válidos. Usa PHPCS/WPCS,
Theme Check o pruebas existentes cuando disponibles y adecuados; no instala herramientas
globales por rutina. Instala tema ZIP en WordPress local/staging autorizado y revisa
logs sin ocultar errores. WP Playground puede servir para pruebas compatibles, pero
no sustituye plugins/hosting objetivo. Sin runtime, declara integración no verificada.

Prueba portada, blog, artículo largo, página, archivo, búsqueda con/sin resultados,
404, paginación, navegación, comentarios y plugins en alcance. Edita un artículo y
patrón desde CMS: persistencia y frontend reflejan cambios sin invalidar bloques.
Verifica que overrides de Site Editor no oculten cambios del archivo del tema.

## Matriz visual

Anchos orientativos en CSS px: 320, 375/390, 768, 1024, 1280 y 1440/1920, más puntos
intermedios donde el contenido rompe. Son pruebas representativas, no certificación
de todos los dispositivos. Horizontal/vertical, touch y ratón, zoom 200% y reflow 400%
según componente. Prueba navegadores objetivo disponibles (Chromium, Firefox, WebKit),
declarando los no comprobados; emulación no equivale a equipo físico.

En cada rango: claro, oscuro, sistema; títulos largos/sin foto; menú abierto/cerrado;
admin bar presente/ausente; bloques tabla/código/galería/embed, formularios y mensajes.
No overflow global, controles cortados ni texto ilegible; scroll local cuando justificado.
Teclado completo, foco visible, Escape, skip link y lector de pantalla si disponible.

Selector de tema: preferencia explícita persiste entre páginas/recargas, sistema sigue
OS, storage bloqueado no rompe navegación, ausencia de JS mantiene página legible.
Revisa destello inicial, CSP, caché compartida, forced-colors y reduced-motion.
WCAG AA exige revisión adicional, no afirmes conformidad total solo por escáner.

## Rendimiento y SEO

Imágenes WP responsive, dimensiones y LCP sin diferir innecesariamente; JS/CSS
proporcionados, fuentes/caché y sin recursos 404. Diagnóstico lab y campo separado.
No dupliques title/canonical/schema con plugin; conserva HTTP 404, robots/sitemap y
indexabilidad por entorno. Si SEO amplio es solicitado, integra skill SEO disponible.

## Operaciones

ZIP del tema instala sin carpeta doble; soporte PHP/WP correcto, assets/licencias
incluidos, sin secretos/deps de desarrollo. Backup y reversión antes de activación
autorizada; verifica sitio tras activar. Para artículos/medios/ajustes guarda IDs,
estados/valores persistidos y distingue guardado, publicado y accesible públicamente.

## Casos para evaluar el skill

1. Tema de bloques con overrides DB: no borrar overrides sin permiso, exportar y probar.
2. Skill de diseño genera React: trasladar diseño a tema editable, no SPA incrustada.
3. MCP de lectura: no inventar escritura; ofrecer REST/CLI autorizados o importación.
4. Cargar diez artículos: drafts salvo publicación explícita; timeout sin duplicados.
5. Dark mode con tabla/logo/formulario: todas superficies y contraste, no inversión global.
6. Cambiar tema de tienda: conservar contenido/CPT y probar compra/plugins antes de activar.
7. Solo archivos locales: ZIP revisable y limitación clara de instalación/pruebas runtime.
8. Tablet en horizontal/admin bar: navegación, sticky y zoom sin cortar controles.

No presentes estos casos como ejecutados cuando solo se revisaron las instrucciones.
