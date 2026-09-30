# Contraste y accesibilidad del sistema de color

## Requisitos y alcance

Comprueba criterios vigentes y el componente real. Referencia WCAG 2.2 AA: texto normal
4.5:1; texto grande 3:1; información visual necesaria para componentes/gráficos 3:1
contra colores adyacentes aplicables. Grande depende del tamaño/peso real (18pt normal
o 14pt bold), no de llamar «heading» a un componente. No redondea ratios para aprobar.

Logotipos, decoración e interfaces inactivas tienen excepciones específicas; no convierte
texto secundario, placeholders o contenido importante en «decorativo» para evadir contraste.
Una excepción no implica que convenga hacerlo ilegible. AAA, si se solicita, usa otros
umbrales de texto; no afirma AA/AAA de la página por aprobar unas parejas.

Los bordes decorativos no requieren ser 3:1 por existir; los que son necesarios para
identificar un control/estado sí deben examinarse según el criterio. No aplica «todo
borde a 3:1» ni «todos los botones necesitan un contorno» como reglas universales.

## Pares y estados

Revisa texto/placeholder/icono necesario sobre cada superficie realmente usada, texto
de CTA sobre su relleno y estados hover/active/focus/selected/error/loading. Para focus
comprueba color adyacente y visibilidad/obscuración/geometría: un ratio no valida todo
el criterio de foco. Un outline del mismo color que el botón puede necesitar gap/capas.

Comprueba overlays, sticky areas, menús, inputs, modales, chips y gráficos, incluidos
estilos inline/SVG que ignoren tokens. Los colores pueden cambiar por opacity, blending,
sombras, imágenes o tema; evaluar el token fuente no prueba el resultado compuesto.
Con gradiente/imagen identifica fondos relevantes y su peor combinación; si es variable
usa superficie/overlay adecuado y revisa el resultado. No usa un único color medio como
evidencia de todo el fondo.

## Más que contraste

No transmite selección/error/disponibilidad solo por color. Usa texto/icono/underline,
patrón o forma pertinentes. En enlaces dentro de texto conserva una señal que permita
identificarlos sin confundirlos con contenido; revisa contexto y estados de interacción.

Evita depender de rojo/verde y comprueba categorías con simulación de deficiencias de
visión cromática cuando exista tooling. Simulación no sustituye redundancia de señal
ni pruebas de usuario. En forced-colors respeta colores del sistema y foco; no bloquea
ese modo globalmente para conservar una paleta de marca.

## Herramienta incluida

Usa [contrato](tool-contract.md) para `scripts/contrast_audit.py`. Solo calcula sRGB
opaco HEX #RGB/#RRGGBB. No acepta alpha, rgb(), OKLCH, P3, gradients o CSS variables:
resuelve colores finales con tooling apropiado antes de medir. No inventa conversiones.
Validar el fallback sRGB no prueba que el valor de gamut amplio renderizado sea equivalente.

El helper informa parejas declaradas. Para web usa estilos computados y revisión
browser/axe/u otra herramienta disponible por rutas, temas y estados pertinentes;
una captura anti-aliased o cálculo JSON por sí solo no acredita accesibilidad completa.
Si no hay acceso, entrega cálculo estático y lista precisa de checks pendientes.

Registra tema, componente/estado, foreground/background, tipo, umbral, ratio sin redondeo
para decisión, resultado y corrección. Mantén evidencia de fallos y aprobación posterior.
