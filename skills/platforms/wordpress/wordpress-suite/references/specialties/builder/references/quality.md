# Validación y entrega

## Matriz de aceptación

| Área | Evidencia |
|---|---|
| Elementor | Documento guardado y reabierto editable, widgets sin errores |
| Plantillas | Condiciones correctas; header/footer y contenido dinámico únicos |
| Responsive | 320, 375/390, 768, 1024, 1280, 1440/1920 CSS px e intermedios |
| Orientación/zoom | Horizontal/vertical, 200% zoom y reflow pertinente a 400% |
| Modo | Claro/oscuro/sistema, persistencia, cambio OS, storage bloqueado y sin JS |
| Accesibilidad | Teclado/foco, menú/Escape, labels, contraste y reduced-motion |
| Contenido | Largo, vacío, sin imagen, tabla, código, galería, embed y errores |
| Woo | Simple/variable, stock, cantidad, notices, carrito y checkout en entorno seguro |
| Persistencia | IDs/status/valores recuperados; publicado separado de guardado |
| Performance | Recursos sin 404, imágenes responsive, layout estable, JS proporcional |

Prueba página pública además de previews Elementor; purga/regenera por mecanismo
oficial solo si necesario. Admin bar, banners, formularios, popups y widgets de addons
en ambos modos. Chromium/Firefox/WebKit cuando disponibles; emulación no equivale
a dispositivos reales. Registra evidencia y navegadores/tamaños no comprobados.
No declara compatibilidad con todos los dispositivos sin pruebas representativas.

Revisa CSS calculado y herencia antes de acumular overrides. No tocar CSP/cache/WAF
global por un fallo de estilo. No asumir publicación si tool devuelve success: leer
status/documento y comprobar frontend. Sin runtime/acceso declara validación pendiente.
Accesibilidad automatizada no certifica WCAG ni reemplaza revisión manual.

## Entrega

Resume páginas/templates, skills de diseño, plugins y dependencias/licencia, IDs/URLs,
exportables y cambios de configuración. Incluye pruebas, límites y reversión según
riesgo. Separa preparado, draft guardado, publicado y visible. No afirma activación de
MCP/plugin sin persistencia comprobada. No publica borradores ni hace compras como cierre.

## Casos de evaluación de decisiones

1. Elementor Free sin Theme Builder: alternativa editable, no promete función Pro.
2. MCP Atomic y página legacy: verifica soporte sin sobrescribir layout incompatible.
3. Plugin dark mode existente: reutiliza/prueba Woo; no añade otro ni invierte imágenes.
4. Producto variable: preserva variaciones/precios/stock y botón real de compra.
5. Diez artículos con timeout: deduplica/recupera IDs y drafts, sin publicación implícita.
6. Cambiar diseño checkout: mantiene validaciones/pasarela y QA sandbox, sin cobro real.
7. Tablet intermedia: menú/títulos/tabla no desbordan; no ocultar contenido como solución.
8. Sin acceso/licencia: export compatible y guía concreta, sin afirmar edición del sitio.

Son casos para evaluar futuras ejecuciones, no pruebas realizadas por escribir el skill.
