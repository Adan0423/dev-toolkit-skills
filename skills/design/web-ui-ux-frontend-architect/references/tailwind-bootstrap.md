# Tailwind CSS y Bootstrap

## Tailwind

- Mantén theme/tokens centralizados.
- Extrae componentes reales; no conviertas cada combinación de utilities en abstracción.
- Usa responsive variants y container queries cuando la adaptación dependa del contenedor.
- Evita clases dinámicas imposibles de detectar por el build cuando el mecanismo de Tailwind no las soporte.

## Bootstrap

- Usa grid/utilities/componentes existentes antes de crear overrides innecesarios.
- Personaliza mediante CSS variables/Sass/utilities de forma centralizada.
- Evita una cascada de `!important` manual fuera del sistema.
- No mezcles múltiples frameworks CSS de componentes sin una razón fuerte.

## Migraciones

No migres Bootstrap↔Tailwind solo por preferencia. Justifica por mantenibilidad, producto, compatibilidad y costo.
