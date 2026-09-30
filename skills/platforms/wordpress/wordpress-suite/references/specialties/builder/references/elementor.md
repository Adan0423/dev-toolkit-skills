# Diseño editable con Elementor

## Inspección y arquitectura

Identifica versión/editor real: Atomic/V4 y widgets/estructuras anteriores tienen
capacidades diferentes. Inventaría documentos, kit activo, breakpoints, tokens,
condiciones Theme Builder y widgets de addons. No convierte documentos de versión
automáticamente ni instala experimentos para hacer funcionar una herramienta.

Mapa de páginas: portada, servicios/landing, blog, single, archivos/categorías,
búsqueda, 404, contacto y tienda cuando proceda. Determina qué controla tema,
Elementor, Theme Builder o bloques. Evita headers/footers y breadcrumbs duplicados.
Usa Theme Builder y contenido dinámico solo cuando disponibles en plan/versiones;
sin esa capacidad conserva plantillas del tema o propone alternativa compatible.
Las condiciones de visualización son parte del diseño: no aplicar una plantilla
nueva globalmente sin comprobar exclusiones, idiomas y páginas comerciales.

## Dirección visual y skills

Si usuario nombra skill, localízalo y lee sus instrucciones. Si no, consulta catálogo
disponible y elige por necesidad: frontend-design, design-system, Figma, accessibility
o polish son ejemplos, no dependencias. Acepta cualquier skill relevante y disponible.
Define audiencia, jerarquía, identidad, densidad y objetivo antes de ejecutar cambios.
Traduce componentes de React/Figma/otro entorno a contenedores, elementos y controles
compatibles; no incrustar una SPA para imitar la referencia. Si skill falta, informa
y continúa con principios de diseño, sin inventar una invocación realizada.

Centraliza paleta semántica, tipos, tamaños, espaciado, radios, sombras y anchos en el
sistema global soportado; evita valores locales contradictorios. No sobrescribas kit
existente completo para corregir una sección. Diseño moderno: jerarquía, legibilidad,
espacio y componentes consistentes; efectos según función, reduced-motion y coste.
Usa imágenes con derechos y contenido real; no inventes reseñas o números comerciales.

## Implementación

Prefiere estructuras nativas y reutilizables soportadas, con anidamiento razonable.
Evita posicionamiento absoluto para layouts principales, tamaños rígidos y secciones
enteras duplicadas por dispositivo. Controles responsive nativos antes de overrides
CSS; usa clases semánticas propias cuando CSS adicional sea necesario.
Widgets/plugins requeridos deben existir antes de importar; no simules widget con
un nombre no registrado. No asumir controles Pro, Custom CSS, forms o widgets Woo
disponibles solo por existir Elementor instalado.

Artículos: plantilla dinámica para título, cuerpo, imagen, autor/fecha, taxonomías y
navegación, manteniendo origen WordPress. Productos: widgets/datos Woo reales, no
precio/botón estáticos. Contacto: integración real y errores/confirmación; no formulario
decorativo con éxito falso. Menús/búsqueda/paginación y vacíos deben funcionar.

## Datos y exportación

Usa API/editor/MCP y formatos de importación/exportación compatibles con la versión.
Un JSON sintácticamente válido no garantiza plantilla importable. Descubre esquema
y IDs reales antes de generar documentos; conserva vínculos globales y referencias
de medios. No modificar _elementor_data o SQL a ciegas: métodos internos requieren
compatibilidad verificada, backup, validación y procedimiento soportado.
No sobrescribir datos serializados ni eliminar revisiones para ocultar fallos.

Después de editar, guarda documento, ábrelo en editor y verifica elementos editables;
revisa frontend. Regenera archivos/CSS o invalida caché mediante mecanismo oficial
de versión cuando haga falta, sin purgas globales arbitrarias. Exporta plantilla/kit
autorizado y documenta dependencias, IDs y condiciones. Un export no acredita que
artículos, pedidos o ajustes externos viajen incluidos.
