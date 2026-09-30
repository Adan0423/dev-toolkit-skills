# Diseño, integración de skills y modo oscuro

## Orquestar skills de diseño

Si usuario nombra un skill, localiza y lee su SKILL.md. Si no, descubre catálogo real
y elige por tarea: frontend-design para dirección visual, design-system para tokens,
accessibility-review para auditoría, Figma para diseño aportado, polish para acabado.
También admite cualquier skill relevante no listado: importa principios/componentes,
no supone una API universal entre skills ni invoca nombres inexistentes.
Explica cuál aplicas. Usa las instrucciones que aporten valor en este alcance; adapta
React/Tailwind u otro output a PHP/bloques/HTML y CSS del tema. No incrustes una app
React completa solo porque el skill de diseño la produjo. No crees subagentes ni
mensajes externos por el mero hecho de combinar skills.
Si skill ausente, declara limitación y continúa diseño propio con criterios aquí.

## Dirección visual y contenido

Define audiencia, identidad, referencias, densidad editorial y conversión. Diseña
tokens semánticos de color/superficies/texto/bordes/estados, escala tipográfica,
espaciado, radios y contenedores. Reutiliza en theme.json/CSS/editor sin duplicar
fuentes de verdad. La estética debe convivir con artículos largos, títulos multilínea,
sin imagen, listas, tablas, embeds, comentarios y mensajes vacíos.
Composiciones editables mediante patrones/bloques; no incrustar todo en una imagen.

## Responsive como aceptación

Mobile first con flujo continuo, minmax, clamp y límites de lectura; breakpoints
según contenido, no marcas de dispositivos. Viewport correcto, sin bloquear zoom.
Min-width:0 en flex/grid cuando haga falta; imágenes fluidas con dimensiones y srcset
nativos, vídeo/embeds con relación de aspecto. Tablas/código pueden tener scroll local
etiquetado; no fuerces scroll horizontal global ni ocultes overflow para encubrir errores.
No recortes artículos ni controles para lograr la maqueta. Prueba orientación, teclado
virtual, zonas seguras y sticky header con admin bar WordPress visible.
Navegación móvil operable con botón real, aria-expanded, cierre Escape y foco coherente;
solo aplica trap de foco si funciona como diálogo modal. No depende de hover.

## Claro / oscuro / sistema

Ofrece tres opciones con control accesible: Sistema, Claro y Oscuro. Preferencia explícita
manda sobre prefers-color-scheme; sistema sigue cambios del dispositivo. Persistencia
local con try/catch ante almacenamiento bloqueado; sin JS sigue preferencia de sistema.
Aplica data-theme o clase en raíz mediante bootstrap mínimo temprano para minimizar
destello. Integrar por hooks/API compatible y revisar CSP, no debilitarla.
No genera HTML cacheado dependiente de usuario para la preferencia de tema.

Define tokens en :root y selectores oscuro; ajusta color-scheme para controles nativos.
No uses filter:invert global. Revisa logos, imágenes transparentes, iconos, formularios,
menús, foco, links, code, tablas y mensajes. Los colores personalizados guardados en
bloques o plugins pueden anular tokens: prueba y corrige selectores sin romper edición.
Las variaciones de estilo Site Editor no equivalen a un selector para visitantes.
Editor: paridad tipográfica/espacial y contraste; no oscurezcas el administrador entero
sin alcance. Respeta prefers-reduced-motion, forced-colors y zoom.

## Accesibilidad

Objetivo WCAG 2.2 AA: contraste 4,5:1 para texto normal, 3:1 grande; controles/indicadores
pertinentes con contraste; foco visible, skip link, landmarks y headings coherentes.
Objetivos táctiles cómodos (preferible 44×44 CSS px), teclado, nombres accesibles,
labels y errores asociados. No apliques ARIA que contradiga HTML nativo. Automatización
no sustituye pruebas de teclado, lectura y zoom.
