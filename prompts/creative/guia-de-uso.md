# Cómo adaptar y ejecutar los prompts

Los bloques son prompts completos en español. Carga uno por tarea; usa los campos
del propio bloque como brief. No necesitas leer todas las categorías.

## Completar el brief

Sustituye cada `{{variable}}` por información concreta. Especifica sujeto o producto,
objetivo, público, soporte final, formato, colores, elementos que deben conservarse
y cambios autorizados. Si una variable no aplica, indica «no aplica» o elimina su
frase; no envíes marcadores vacíos a un generador. Para explorar, permite supuestos
explícitos sobre estilo; para editar identidad, producto o geometría, usa referencias.

Ejemplo: `{{producto}}` → «frasco de café de 250 g, foto adjunta A»;
`{{paleta}}` → «crema #F4E9DA, café #452D24 y verde #40644A»;
`{{formato}}` → «imagen cuadrada para ficha de tienda, producto entero con margen».
Son datos de ejemplo, no una recomendación universal de paleta o proporción.

Si un agente prepara el prompt, pide solo los datos que bloquean el trabajo. Si el
prompt ya está completo y hay herramientas, ejecuta la tarea. Si solo hay chat,
entrega el prompt adaptado e indica qué debe adjuntar el usuario; no afirma haber
generado o editado un archivo.

## Referencias y preservación

Identifica archivos: A = sujeto/producto, B = estilo, C = composición. No mezcla
identidades o etiquetas por usar varias referencias. En edición, define región
editable y elementos protegidos. Las máscaras, si existen, delimitan la zona;
comprueba sus convenciones en la herramienta. Mantén el original y entrega una copia.
Para series, reutiliza la misma referencia y ficha de rasgos; revisa cada salida.

## Formato y capacidades reales

Relación de aspecto, tamaño y cantidad deben configurarse en los controles de la
herramienta cuando existan. El prompt describe el objetivo: escribir «8K» no produce
automáticamente un archivo 8K. No presupone seed, negative prompt o máscaras.
Describe exclusiones en lenguaje natural; usa campos específicos solo si se admiten.
Transparencia requiere salida con canal alpha; una cuadrícula dibujada no es transparencia.
JPEG no conserva alpha. Un render 3D es una imagen, no un modelo editable ni un STL.

Para logos, una apariencia vectorial no es SVG editable. Usa el prompt LOG-04 para
construir un SVG sencillo real con código y validar el archivo. Para fotografía o
conceptos detallados, entrega raster y explica cualquier vectorización pendiente.
Las cifras de lente, apertura e iluminación describen intención fotográfica; no
son metadatos verificados de una foto generada.

## Texto, producto y revisión

Usa nombres y frases exactos entre comillas. Comprueba ortografía, etiquetas y precios.
Si el texto se deforma, genera el arte sin letras y compón texto editable después.
Para catálogo, utiliza los assets reales de producto/etiqueta y no inventes atributos,
certificaciones ni accesorios. Para impresión verifica medidas, sangrado, resolución
y perfil con el proveedor; no declara CMYK por escribirlo en el prompt.

Evalúa identidad, anatomía, bordes, reflejos, sombras, perspectiva, materiales,
continuidad y legibilidad. Para corregir una salida, describe un cambio localizado
y lo que debe quedar fijo: «Corrige únicamente [problema] en [región], conserva
[rasgos y composición], entrega una copia en [formato]». Es una pauta de iteración,
no una promesa de conservación perfecta de píxeles.

En web, distingue prototipo visual de sitio funcional. Revisa navegación, formularios,
datos, errores y permisos; prueba tema claro/oscuro, teclado y anchos intermedios.
No simula pagos o envíos exitosos. Usa las skills pertinentes si están disponibles,
sin instalar otras ni cambiar la tecnología solo para seguir una plantilla.
