# Color para gráficos y datos

Identifica qué codifica el color: categoría, magnitud, dirección, umbral o selección.
Reutiliza identidad semántica en todos los gráficos; no reasigna una categoría a otro
color al ordenar o filtrar. Etiquetas/leyendas accesibles deben mantener correspondencia.

- Categórico: tonos distinguibles y señales redundantes (etiqueta, marcador o patrón).
  La cantidad de series determina si bastan colores; no fuerza un número universal.
- Secuencial: progresión perceptual adecuada a orden/magnitud, sin aparentar categorías.
- Divergente: punto central con significado del dominio, extremos distinguibles y
  escala coherente; no utiliza centro ficticio para datos sin referencia central.
- Estado/umbral: significado coherente, límites explícitos y texto/icono; rojo/verde
  solos no distinguen éxito/error para todos los usuarios.

Comprueba trazos/marcadores necesarios contra fondo y colores adyacentes cuando el
criterio aplique, además de texto de ejes, leyenda y tooltip. Una serie contrastada con
el fondo puede seguir siendo indistinguible de otra; no resuelve todo con el ratio.
Evita interpolación arcoíris si introduce orden aparente o variación engañosa.

En claro/oscuro adapta luminosidad/croma conservando identidad de serie. Revisa colores
inline/SVG de la biblioteca y exportaciones que no hereden tema. No cambia escala,
datos, tipo de gráfico o KPI para solucionar una petición exclusiva de color.

Mantén significado sin color y verifica simulación cromática si hay herramienta. Prueba
legibilidad a tamaño real y alternativas textuales pertinentes; un JSON de contrastes
no certifica la accesibilidad del gráfico interactivo.
