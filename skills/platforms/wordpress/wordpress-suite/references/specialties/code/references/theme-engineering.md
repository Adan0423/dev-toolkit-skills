# Ingeniería de temas

## Elegir arquitectura

Bloques: preferible para edición nativa de plantillas/patrones cuando instalación y
objetivo lo permiten. Clásico: compatible con integraciones PHP existentes o control
de templates requerido. Híbrido: clásico con theme.json y editor de bloques. Tema hijo:
extiende un padre existente sin perder cambios con actualización. No migres por moda.

Estructuras orientativas (no todos los archivos son obligatorios):

```text
mi-tema/                        # bloques
  style.css                     # cabecera Theme Name/Text Domain/versiones
  theme.json                    # esquema compatible con WP objetivo
  functions.php                 # hooks, assets y soporte necesario
  templates/index.html          # fallback; markup válido de bloques
  templates/{front-page,home,single,page,archive,search,404}.html
  parts/{header,footer}.html
  patterns/                     # composiciones insertables/editables
  assets/{css,js,images}/

mi-tema/                        # clásico
  style.css
  index.php                     # fallback de la jerarquía
  functions.php
  header.php / footer.php
  front-page.php / home.php / single.php / page.php
  archive.php / search.php / 404.php
  template-parts/ / assets/ / inc/
```

Respeta jerarquía: front-page y home no son intercambiables. Bloques usan comentarios
serializados y atributos reconocidos, no un HTML completo pegado en template. Un
tema hijo declara Template con slug real y su carga de estilos según el padre.
Theme.json es opcional para reconocimiento del tema de bloques, pero útil para tokens
y editor; elige schema/version según WordPress instalado, no trunk automáticamente.

## Datos y extensibilidad

Conserva Loop, the_content y bloques del post; no sustituyas artículo por fixtures.
Usa WP_Query solo donde corresponde, paginación y wp_reset_postdata tras loops propios.
Evita consultas N+1 y límites arbitrarios que hagan desaparecer artículos. Carga datos
dinámicos al renderizar cuando proceda, mantén enlaces/IDs WordPress reales.
Usa plantillas/partes reutilizables, hooks y prefijo único de funciones/handles.
En clásico conserva wp_head, wp_footer, wp_body_open, body_class y language_attributes;
soportes y menús en hooks apropiados. Usa title-tag y thumbnails cuando corresponda.
Internacionaliza cadenas con dominio del tema y escape contextual; RTL con propiedades
lógicas. Incluye licencias de recursos y no uses URLs de assets locales fijas.

CPT, taxonomías de negocio, formularios procesados, REST personalizado y tareas que
deban sobrevivir al tema: plugin separado. Registra schema/capabilities de meta;
no expongas datos privados al REST. Nonce mitiga CSRF, no sustituye current_user_can.
Sanitiza entrada, valida dominio/tipos y escapa tarde según HTML/atributo/URL/JS.
Consultas propias inevitables: prepare; nunca concatenar datos del usuario.

## Assets/editor

Usa wp_enqueue_style/script y APIs de bloques para dependencias/carga; no pegues
scripts en plantillas. Versiona caché, carga condicionalmente y usa API de estrategia
compatible. No impongas librería pesada a una interacción simple. theme.json y estilos
del editor deben reflejar tipografía, anchos, paleta y espaciado del frontend.
Variables semánticas claro/oscuro necesitan CSS adicional cuando theme.json emita
valores estáticos: prueba estilos de bloques, inline y overrides del usuario.
Los templates/estilos guardados en base de datos por Site Editor pueden prevalecer
sobre archivos: inventaría/exporta overrides y no los borres sin autorización.

## Integraciones

WooCommerce, formularios, miembros y multilingual: detecta versión y compatibilidad,
usa hooks y evita copiar templates del plugin sin necesidad. Si copias un override,
registra versión/origen y comprueba cambios futuros. Verifica carrito/checkout y estados
si entran en alcance. Preserva SEO de plugin; no generar head duplicado desde el tema.

Empaqueta una raíz con slug y archivos requeridos, excluyendo .git, secretos,
node_modules, tests/fixtures y caches; incluye assets compilados y licencias necesarias.
No confundas ZIP del skill con ZIP del tema que producirás en una ejecución futura.
