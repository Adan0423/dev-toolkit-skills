# Artículos, medios y configuración

## Preparar operación

Lee sitio, usuario/capacidades y estado previo; usa APIs WordPress, no SQL directo.
Define alcance, fuente/licencia del contenido, autor real, taxonomías y estado.
Preparar tema no autoriza insertar demos en producción. No borres datos para importar.
Si cargar contenido no especifica publicación, borrador; si pide publicar, esa petición
autoriza publicar el contenido solicitado. No inventes autoría, opiniones o estadísticas.

## Entradas y páginas

1. Mapea título, slug, cuerpo, extracto, tipo, estado, autor, idioma, fecha, categorías,
   tags, featured_media y meta soportada. Usa IDs reales, no nombres en campos de ID.
2. Busca duplicados por origen/slug y conserva mapa origen → ID. Usa contenido en bloques
   válidos si debe editarse en Gutenberg; no páginas enteras como un bloque HTML gigante.
3. Crea/actualiza recurso concreto, no todo el sitio. No cambies slug publicado sin
   estudiar redirect. Fecha futura usa zona horaria del sitio y estado soportado.
4. Recupera ID, status, link y campos guardados; comprueba vista autorizada/pública.
   En lote registra éxito/fallo por elemento y continúa independientes si seguro.

REST core suele usar /wp-json/wp/v2/posts, pages, categories, tags y media; descubre
schema/rutas reales, paginación y CPT. Meta personalizada requiere registro/exposición
y permisos: no asumas que campos de plugins SEO son editables con REST core.
Permisos faltantes no equivalen a colección vacía. No expongas contenido draft en logs.

## Medios

Comprueba derechos, tamaño y formatos; usa biblioteca/API de medios WordPress para
attachment ID y tamaños responsive. Completa alt descriptivo, título y caption cuando
proceda. Subir imagen no la convierte automáticamente en destacada: asigna attachment
ID al post y verifica frontend. No subas duplicados en reintentos; conserva mapa/hash.
No permitas SVG inseguro ni evadas MIME permitidos. Archivos grandes: límite hosting,
optimización y carga controlada. Una carga fallida no debe llevar a publicación rota.

## Reintentos e importación

Tras timeout de escritura, busca resultado antes de repetir: REST no garantiza
idempotencia por sí solo. Respeta 429/Retry-After y acota reintentos; ante 401/403 revisa
autenticación/capabilities en vez de insistir. Guarda manifiesto IDs para recuperación.
WXR sirve para migración WordPress con limitaciones de medios y dependencias; backup
de base/archivos no es lo mismo. CSV/JSON requiere mapear mediante herramienta soportada.
No usar search-replace bruto que corrompa serialización; si hace falta WP-CLI compatible,
dry-run y backup dentro del alcance autorizado.

## Ajustes

Inventaría identidad, idioma/zona, portada/blog, navegación, enlaces permanentes,
comentarios, usuarios, privacidad, SEO, caché y plugins relevantes. Registra valor
anterior → solicitado → persistido. API settings expone solo algunos ajustes y requiere
capacidades; no asumas permisos admin. Lectura y escritura tienen alcances distintos.
Flush rewrite únicamente ante cambios de rutas, no en cada carga. Cambiar dominio,
permalinks, tema activo o extensiones exige compatibilidad, copia/reversión y autorización
aplicable. Formularios, correo y pagos deben usar integraciones reales, no éxito simulado.
Prueba edición de contenido como rol editorial, no solo administrador.
