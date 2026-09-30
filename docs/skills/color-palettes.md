# Paletas profesionales para agentes de diseño

[Fuente color-palette-studio](../../skills/design/color-palette-studio/SKILL.md) ·
[Paquete independiente](../../SKILL/color-palette-studio.zip) ·
[Familia web-design-suite](../../SKILL/web-design-suite.zip).

La skill selecciona paletas según marca, audiencia y contexto; transforma colores
en roles de interfaz y aplica tokens coherentes. Incluye selección, accesibilidad,
implementación por tecnología y visualización de datos. Puede colaborar con otras
skills de diseño disponibles, cargando solo las guías necesarias.

Úsala con «Usa $color-palette-studio para revisar y aplicar la paleta de este
proyecto». La familia $web-design-suite también carga esta guía al elegir colores
o crear temas. Esto facilita su uso por agentes que tengan instalada la skill;
no instala instrucciones globales ni garantiza que todos los agentes la invoquen.

Descomprime el ZIP en la carpeta de skills de tu agente, conservando una única
carpeta `color-palette-studio` con su SKILL.md y recursos. Alternativamente instala
la familia: ya contiene la especialidad completa, sin depender del paquete individual.

## Qué hace

- Paleta con roles para superficies, texto, acciones, foco, bordes y estados.
- Temas claro, oscuro y sistema cuando el alcance lo requiere; conserva la marca.
- Contraste de texto y controles, señales adicionales al color y revisión de estados.
- Integración con CSS, frameworks, sistemas de tokens, WordPress y otros CMS,
  según la tecnología y el acceso reales. Da instrucciones concretas si no puede actuar.
- Colores para gráficos categóricos, secuenciales y divergentes, con etiquetas y patrones.

El ejemplo parte de [esta paleta de Color Hunt](https://colorhunt.co/palette/222831393e4600adb5eeeeee).
Su turquesa #00ADB5 con blanco ofrece aproximadamente 2.747:1: requiere adaptación
para texto normal según [W3C](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
Los tokens semánticos incluidos son una adaptación propia y pasan sus 32 parejas
declaradas, repartidas entre claro y oscuro. No se promete una auditoría WCAG completa.

## Comprobar y mantener

Desde la carpeta fuente de la skill:

```sh
python scripts/contrast_audit.py check assets/palette-example.json
python scripts/contrast_audit.py css assets/palette-example.json
```

El comprobador no necesita red y admite HEX sRGB opaco. Mide parejas declaradas;
no inspecciona una web ni resuelve transparencias o gradientes. La validación de
la interfaz renderizada sigue siendo necesaria. El CSS generado no incluye por sí
solo un selector de tema ni persistencia.

Actualiza la fuente original, ejecuta las pruebas y regenera ambos paquetes:

```sh
python -B -m unittest discover -s tests -p test_color_contrast.py
python scripts/package_skill.py skills/design/color-palette-studio
python scripts/build_skill_families.py --family web-design-suite
```

[Fuentes consultadas](../../skills/design/color-palette-studio/references/research-sources.md)
incluye Color Hunt, los cuatro catálogos solicitados, W3C y MDN. Se conserva la
skill colorize anterior; no edites la copia generada dentro de la familia.
