# Biblioteca de prompts profesionales

**68 prompts:** 64 nuevos de imagen, edición y web, más los cuatro de trabajo
con repositorios que ya existían. Los 64 nuevos están organizados en 15 categorías.

[Catálogo creativo completo](creative/README.md) · [Guía de adaptación](creative/guia-de-uso.md)
· [Fuentes investigadas](creative/fuentes.md) · [Índice para agentes](creative/catalog.json).

## Elegir por tarea

| Necesidad | Biblioteca |
|---|---|
| Retoque, fondos, restauración, ampliación | [Edición de fotos](creative/edicion-fotos.md) |
| Fotografía de personas | [Retrato fotográfico](creative/retrato-fotografico.md) |
| Avatares para perfiles y comunidades | [Retrato y avatar](creative/retrato-avatar.md) |
| Identidad, packaging y sistema visual | [Diseño de marca](creative/diseno-marca.md) |
| Símbolos, wordmarks e iconos | [Logotipos](creative/logotipos.md) |
| Campañas y fotografía de producto | [Producto comercial](creative/producto-comercial.md) |
| Catálogo, fichas y recursos para tienda | [E-commerce](creative/ecommerce.md) |
| Escenas dibujadas y renders conceptuales | [Ilustración y 3D](creative/ilustracion-3d.md) |
| Mascotas, personajes y continuidad | [Personajes](creative/personajes.md) |
| Manga, chibi y caricatura | [Anime y caricaturas](creative/anime-caricaturas.md) |
| Técnicas pictóricas y gráficas | [Estilo artístico](creative/estilo-artistico.md) |
| Espacios, decoración y escenificación | [Interiores](creative/interiores.md) |
| Relighting, partículas y atmósfera | [Efectos visuales](creative/efectos-visuales.md) |
| Publicidad conceptual y composiciones | [Visuales creativos](creative/visuales-creativos.md) |
| Platos, bebidas y gastronomía | [Comida](creative/comida.md) |
| Landing, tienda, portfolio, SaaS, CMS y rediseño | [Páginas web](web/paginas-web.md) |

Las categorías fotográficas se agrupan en un mismo archivo de retrato: el catálogo
tiene 14 archivos de imagen y uno de web, sin duplicar prompts entre perfiles y fotografía.

## Prompts de repositorio existentes

- [Crear una skill](meta/prompt-skill-creator.md).
- [Organizar skills de proyectos](meta/prompt-organizar-skills-repo.md).
- [Auditoría de sistema](audit/prompt-auditoria.md).
- [Mejorar README](docs/prompt-mejorar-readme.md).

## Uso rápido

Abre una categoría, elige un ID y copia su bloque completo. Sustituye las variables
`{{...}}` y adjunta las referencias que solicite. Para un agente: «Lee prompts/creative/
ecommerce.md y usa el prompt ECO-01 con esta foto de producto». El índice JSON
permite localizar un prompt sin cargar toda la biblioteca.

No requieren instalación como skill. La disponibilidad de edición, máscaras, tamaño,
transparencia o generación depende de la herramienta. Los prompts no garantizan
resultados idénticos ni certifican compatibilidad con todos los modelos.
