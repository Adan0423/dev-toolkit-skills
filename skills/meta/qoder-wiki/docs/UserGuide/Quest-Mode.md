#ModoMisión

## Descripción general

Quest Mode es la función de programación autónoma de Qoder, que permite al Agente completar tareas de desarrollo de un extremo a otro. Sólo necesita describir sus objetivos y Quest aclarará los requisitos, planificará la solución, ejecutará el código y verificará los resultados, sin intervención humana continua.

**Concepto central**: Definir el objetivo. Revisa el resultado.

## Funciones principales

### Programación independiente

El agente completa de forma independiente resultados entregables de alta calidad, de extremo a extremo:

- **Soporte de modelo superior**: utilice el modelo de IA líder en el mundo
- **Mecanismo de alineación de requisitos**: identificación de intenciones, aclaración de requisitos, especificación de cocreación
- **Capacidad de misión de larga distancia**: mejora enormemente las capacidades de ejecución continua a largo plazo
- **Garantía de calidad independiente**: capacidades integradas de verificación de resultados, verificación independiente y reparación de la calidad entregable

### Escenarios de aplicaciones compatibles

- **Desarrollo impulsado por especificaciones**: primero alinear requisitos y restricciones, luego ejecutar y aceptar
- **Idea a producto**: soporte 0-1 para la creación de sitios web y prototipos

## Empezar

### Cambiar al modo Misión

Qoder proporciona dos modos de trabajo:

- **Modo editor**: programación colaborativa en tiempo real, una pregunta y una respuesta
- **Modo Misión**: delegación de tareas, ejecución autónoma, entrega sin intervención

**Método de cambio**: haz clic en el botón de cambio **Editor/Misión** en la esquina superior izquierda

## Crear tarea

### Seleccionar escena

| Escenario | Aplicabilidad | Comportamiento de búsqueda |
| --- | --- | --- |
| **Controlador de especificaciones** | Desarrollo y reconstrucción de funciones complejas | Primero alinear el alcance de los requisitos, diseñar los planes de implementación y los criterios de aceptación |
| **Crear un sitio web** | 0-1 creación de sitios web y creación rápida de prototipos | Describa el sitio web que desea crear y Quest creará las páginas y la estructura general |
| **Exploración de prototipos** | Validar rápidamente ideas y experimentos creativos | Comience con una idea y Quest la convertirá en un prototipo funcional |

## Entorno de ejecución

Quest admite tres entornos de ejecución:

### Local

- Modificar directamente en el espacio de trabajo principal, costo inicial cero
- Adecuado para tareas sencillas y verificación rápida

### Árbol de trabajo (paralelo)

- Cree un espacio de trabajo oculto en segundo plano y mantenga limpia la rama principal
- Adecuado para tareas moderadamente complejas y paralelismo multitarea

### Remoto (Nube)

- Ejecución remota de contenedores, apagado local y desconexión de red.
- Adecuado para tareas complejas de larga distancia y operaciones que requieren muchos recursos

## Mejores prácticas

### Escribe una buena descripción de la tarea.

```
❌ "Optimizar código"
✅ "Refactorice UserService, divídalo en múltiples funciones pequeñas y agregue pruebas unitarias"

❌ "Crear un sitio web"
✅ "Cree un blog de viajes, que incluya una página de inicio, una lista de artículos y una página de detalles, utilizando Next.js"
```

### Elige la escena adecuada

- **Controlador de especificaciones**: funciones complejas, documentación requerida → implementación estricta
- **Crea un sitio web**: crea rápidamente → Lo que ves es lo que obtienes
- **Exploración de prototipos**: validar ideas → iterar rápidamente
