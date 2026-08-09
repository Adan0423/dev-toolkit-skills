# Selector de modelo

Fuente: https://docs.qoder.com/zh/user-guide/chat/model-tier-selector

## Descripción general

Qoder proporciona dos tipos de métodos de selección de modelos:

- Selección jerárquica: seleccione grupos de modelos por capacidad y costo
- Especificar modelo: seleccione directamente un modelo específico
- Modelo personalizado: acceda a modelos de terceros a través de la clave API; consulte `modelo personalizado.md` para obtener más detalles

## Selección jerárquica

| Nivel | Descripción | Escenarios aplicables | Consumo de créditos |
| --- | --- | --- | --- |
| Automático | Enrutamiento inteligente, equilibrio entre rendimiento y coste | Elección predeterminada para el desarrollo diario | Aproximadamente 1,0x |
| Último | El razonamiento más sólido y el pensamiento profundo | Diseño de sistemas complejos, problemas difíciles | Aproximadamente 1,6x |
| Rendimiento | Salida de alta calidad | Implementación y reconstrucción de funciones centrales | Aproximadamente 1,1x |
| Eficiente | Rendimiento de alto costo | Generación básica, pruebas, preguntas y respuestas generales | Aproximadamente 0,3x |
| Lite | Modo básico gratuito | Verificación rápida, preguntas y respuestas ligeras | Gratis |

## Sugerencias de uso

- Se prefiere `Auto` por defecto
- Las tareas de alto valor se pueden cambiar a "Ultimate" o "Performance"
- Utilice "Eficiente" para tareas sencillas o sensibles al costo
- Pruebas temporales y preguntas y respuestas rápidas disponibles en `Lite`

## Instrucciones comunes

- La lista de modelos podrá actualizarse con estrategias oficiales.
- Puede cambiar de modelo en la misma sesión.
- La selección jerárquica está sesgada hacia "seleccionar por marcha", y el modelo designado está sesgado hacia "seleccionar según modelos específicos"
- Diferentes modelos tienen diferentes coeficientes de consumo de Créditos.

