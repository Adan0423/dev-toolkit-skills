# Familias con carga selectiva

Se añadieron seis skills principales y 28 especialidades internas. Cada entrada
elige el modo que corresponde a la tarea y lee solo su guía inicial; carga recursos
adicionales cuando la implementación los necesita. Las 95 fuentes anteriores se
conservan: ahora hay 101 SKILL.md y 55 paquetes.

| Familia | Especialidades | Paquete |
|---|---|---|
| [React](../../skills/frontend/react-engineering/SKILL.md) | Arquitectura, implementación, rendimiento, modernización, rutas | [react-engineering.zip](../../SKILL/react-engineering.zip) |
| [Tailwind](../../skills/frontend/tailwind-engineering/SKILL.md) | Instalación/migración, temas, shadcn, documentación | [tailwind-engineering.zip](../../SKILL/tailwind-engineering.zip) |
| [Diseño web](../../skills/design/web-design-suite/SKILL.md) | Dirección, stack, descubrimiento, auditoría, responsive, composición, tipografía, color, movimiento, acabado, rendimiento, crítica | [web-design-suite.zip](../../SKILL/web-design-suite.zip) |
| [Documentación](../../skills/docs/repository-documentation/SKILL.md) | Auditoría documental, README, cambios | [repository-documentation.zip](../../SKILL/repository-documentation.zip) |
| [WordPress](../../skills/platforms/wordpress/wordpress-suite/SKILL.md) | Código/temas y Elementor/WooCommerce; rutas directas para contenido | [wordpress-suite.zip](../../SKILL/wordpress-suite.zip) |
| [CV](../../skills/docs-cv/cv-suite/SKILL.md) | Formato Harvard y adaptación ATS | [cv-suite.zip](../../SKILL/cv-suite.zip) |

## Instalación y uso

Descomprime el paquete elegido en la carpeta de skills del agente. El ZIP contiene
una carpeta con el nombre de la familia: evita añadir otra envoltura del mismo nombre.
Comprueba que el resultado sea `<carpeta-de-skills>/<familia>/SKILL.md`.
También puedes copiar directamente la carpeta fuente completa de la familia.

Para reducir el catálogo activo, instala la familia en lugar de todas sus skills
individuales. Conservar ambas opciones en este repositorio facilita mantenimiento;
instalarlas todas no reduce el número de entradas que ve el agente.

Ejemplos: «Usa $react-engineering para revisar el rendimiento» o «Usa
$wordpress-suite para preparar un artículo como borrador». Las especialidades son
referencias internas (`guide.md`), no skills anidadas que dependan de descubrimiento
automático. Cada paquete incluye sus guías, recursos y scripts correspondientes.

Las entradas principales tienen entre 30 y 47 líneas. La carga selectiva permite
evitar lecturas innecesarias, pero no se ha medido un porcentaje de ahorro de tokens.
No se instaló ninguna familia globalmente.

## Mantener y mejorar

1. Mejora la skill original indicada en `family-manifest.json`. No edites las copias
   generadas en `references/specialties/`.
2. Para cambiar selección, alcance o instrucciones comunes, edita el SKILL.md principal.
3. Para añadir especialidades o recursos complementarios, edita
   [skill-families.json](../../scripts/skill-families.json).
4. Ejecuta `python scripts/build_skill_families.py` para regenerar guías y ZIPs.
5. Ejecuta `python scripts/build_skill_families.py --check` para comprobar contenido,
   procedencia y correspondencia con los paquetes. Revisa la tarea afectada en un
   proyecto representativo antes de distribuir una mejora de comportamiento.

El generador conserva licencias y hashes de procedencia. Adapta enlaces locales y
dependencias de comandos Impeccable al contexto de la familia. En documentación
respeta la autorización existente para cambios reversibles; conserva límites para
limpieza destructiva. Estas adaptaciones se registran en el manifiesto. No elimina
archivos inesperados: pide revisión para no perder recursos añadidos manualmente.

## Revisión de selección

| Solicitud | Primera especialidad |
|---|---|
| Componentes React lentos | React: performance |
| Loaders de React Router | React: routing |
| Variables de tema claro/oscuro en Tailwind | Tailwind: theming |
| Mejorar solo espaciado | Diseño: layout |
| Ajustar tipografía | Diseño: typography |
| Actualizar README | Documentación: readme |
| Tema WordPress desarrollado en código | WordPress: code |
| Crear una entrada con Elementor instalado | Recurso de contenido del modo builder |
| Formatear CV sin oferta laboral | CV: format |
| Adaptar CV a una oferta | CV: ats |

Se revisaron estructura, enlaces internos y coherencia de estas rutas. Esto no
equivale a una evaluación independiente del agente ni a probar todas las
especialidades, plataformas o integraciones en ejecución.
