# Responsive y accesibilidad

## Responsive

Prueba por contenido y espacio, no por nombres de dispositivos.

Casos mínimos sugeridos:
- ~320-375 px;
- ~390-430 px;
- ~768 px;
- ~1024 px;
- ~1280-1440 px;
- >1600 px si el producto lo justifica.

No conviertas estos valores en dogma. Ajusta breakpoints a puntos donde el layout realmente falla.

Usa:
- CSS Grid/Flexbox;
- tamaños fluidos;
- `min()`, `max()`, `clamp()` cuando ayuden;
- container queries cuando un componente dependa de su contenedor;
- `overflow` deliberado;
- tablas adaptativas sin ocultar datos críticos.

## Accesibilidad

Referencia WCAG 2.2 cuando corresponda. Comprueba teclado, focus, labels, contraste, targets, headings, landmarks, errores y reduced motion.
