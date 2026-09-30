# Tokens e implementación por contexto

## Reutilizar antes de añadir

Inspecciona variables, design system, theme y overrides existentes. Diferencia valores
primitivos de roles semánticos y aliases de componentes. Conserva nombres públicos de
tokens o documenta migración compatible; no agrega un segundo sistema paralelo.

Tokens orientativos: background, surface, text, text-muted, border-control, action,
on-action, action-hover/active, link, focus, success/error/warning/info y sus superficies.
No necesita exactamente ese catálogo si el proyecto ya tiene uno apropiado.
No distribuye HEX repetidos por componentes; usa el punto global del sistema existente.

## Código web y otras interfaces

- HTML/CSS y frameworks: usa variables/tokens y estilo de componentes en el sistema
  real, incluidos SVG y portales. JSX/TSX/Blade/etc. no cambian la necesidad de contraste.
- Tailwind: adapta versión/configuración/theme existente; no migra a v4 ni instala
  shadcn por pedir una paleta. Un cambio de token puede afectar muchas rutas: revisa alcance.
- WordPress, Elementor, Wix u otro CMS: usa estilos globales/tema y controles nativos
  disponibles; evita valores distintos por elemento que rompan edición y mantenimiento.
  Identifica plugins, estilos inline, formularios y checkout afectados.
- Apps nativas: usa recursos/tema del stack; no entrega solo CSS si el usuario pide
  Compose, SwiftUI, Flutter o un escritorio nativo. Respeta semántica de estados.
- Diseño/marketing: adapta roles a fondo, texto y CTA del formato/placement. Un póster
  oscuro no equivale a implementar dark mode interactivo. Revisa lectura al tamaño final.

Si necesita una exportación DTCG/Figma/Style Dictionary, verifica formato/versión y
capacidad de herramienta concreta. El JSON incluido es un contrato propio del helper,
no un archivo universal compatible con todos los sistemas de tokens.

## Claro, oscuro y sistema

Usa roles equivalentes con valores por tema; no invierte RGB ni reutiliza texto oscuro
en superficies oscuras. Controla inputs, placeholders, autofill, selects, iconos, charts,
modales y estados. `color-scheme` ayuda a UI del navegador; no recolorea todo el producto.

Cuando hay selector distingue elección explícita y sistema. Reutiliza persistencia/
bootstrap/SSR existentes; evita flash y divergencia de hidratación. Un selector de tema
debe ser accesible y reflejar estado real. No añade esa lógica fuera del alcance.
El CSS ejemplo admite atributo `data-theme` en la raíz: light/dark explícitos y ausencia
o system para preferencia del sistema; no incluye selector ni persistencia JS.

El [CSS ejemplo](../assets/tokens-example.css) se genera desde
[JSON](../assets/palette-example.json) con el helper; valores son demostrativos y deben
adaptarse a marca y usos. Color responsivo significa conservar función y lectura en
variantes de UI, no cambiar colores arbitrariamente por ancho de pantalla.

## Verificación y entrega

Prueba rutas/componentes afectados en móvil/tablet/escritorio, temas y estados. No
infere éxito visual por build solamente. Si cambia solo un botón, verifica ese alcance
y dependencias; no exige rehacer toda la web. En forced-colors verifica sistema/foco.

Entrega diff o configuración editable, tabla rol/valor/uso, parejas y estados comprobados,
procedencia y límites. Para MCP/browser externo confirma sitio y permiso de mutación;
preparar CSS no autoriza publicar. No modifica lógica, accesos o backend por elegir colores.
