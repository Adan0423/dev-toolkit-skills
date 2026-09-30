# Comprobador y contrato de datos

Ejecuta desde la carpeta de esta skill, o desde su especialidad color dentro de la
familia. Requiere Python 3; usa solo la biblioteca estándar, sin red ni instalación.

```sh
python scripts/contrast_audit.py pair --foreground '#FFFFFF' --background '#00ADB5' --kind text
python scripts/contrast_audit.py check assets/palette-example.json
python scripts/contrast_audit.py css assets/palette-example.json
```

`pair` y `check` imprimen JSON: salida 0 significa que pasan las parejas declaradas,
1 significa contraste insuficiente, 2 indica entrada inválida. `css` imprime CSS;
generar tokens no comprueba su accesibilidad. No escribe archivos por sí mismo.

El JSON propio contiene `themes` con `light` y/o `dark`, cada uno con tokens de
nombre semántico y valores HEX sRGB opacos. `checks` declara objetos con `id`,
`theme`, `foreground`, `background` y `kind` (`text`, `large` o `ui`). Foreground y
background son nombres de tokens. Consulta el ejemplo completo para el formato.
No es una declaración de compatibilidad con un estándar de intercambio de tokens.

Se rechazan claves JSON duplicadas, referencias inexistentes, identificadores
repetidos y listas de comprobación vacías. `unchecked_themes` señala temas sin
parejas declaradas: un resultado positivo no acredita esos temas.

Acepta solo #RGB y #RRGGBB. Para transparencia, gradientes, imágenes, OKLCH o P3,
resuelve primero el color efectivamente renderizado y el fondo real con herramientas
apropiadas. No elimina alpha ni supone un fondo blanco. Compara ratios sin redondear.
El autor declara el tipo de pareja; el programa no mide tamaño de fuente ni decide
qué criterio WCAG corresponde. No inspecciona DOM, estados, foco o daltonismo.

El CSS usa roles `--color-*`, tema explícito con `data-theme` y preferencia del
sistema cuando no hay selección light/dark. No implementa selector ni persistencia.
Adapta el contrato al sistema real antes de integrarlo. Actualiza primero el JSON,
regenera el CSS y comprueba las parejas y la interfaz renderizada.
