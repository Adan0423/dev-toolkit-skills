# Predicción de sugerencias entre líneas (SIGUIENTE)

La predicción de sugerencias entre líneas (NEXT) puede predecir dinámicamente cambios de código según el contexto del código completo actual, combinado con modificaciones de código y la posición del cursor, lo que permite a los desarrolladores completar cambios de código de manera eficiente con una sola pestaña.

## Características

Con Qoder NEXT podrás:

- Edite varias líneas a la vez cerca del cursor
- Obtenga recomendaciones basadas en cambios recientes y ediciones aceptadas previamente
- Salta sin problemas a la siguiente sugerencia en un archivo
- Importar dependencias automáticamente.
- Obtenga sugerencias de modificación entre archivos sin tener que buscar manualmente cambios relevantes

## Principio de funcionamiento

Qoder mostrará automáticamente sugerencias en línea o una al lado de la otra según el ancho del código modificado y el mensaje SIGUIENTE:

- Si el ancho total de los dos excede el ancho del editor, se recomienda mostrarlo en forma en línea
- De lo contrario, muestre lado a lado para facilitar la comparación.

**Aceptar o rechazar sugerencias:**

- Coloca el cursor sobre **Aceptar**/**Rechazar**, o
- Presione `Tab` para aceptar, `Esc` para rechazar

**Vista previa de cambios sugeridos:**

- Mantenga presionada la tecla `⌥` (Mac) / `Alt` (Windows) para obtener una vista previa de los cambios.
- Liberación para restaurar el código original.

## configuración

### Habilitar SIGUIENTE

1. En la esquina superior derecha de Qoder IDE, haga clic en el icono de usuario y seleccione **Configuración de Qoder**
2. En el panel emergente, haga clic en **Sugerencias entre líneas**
3. Activa **SIGUIENTE**

### Importación automática

Cuando esté activado, NEXT importará automáticamente los módulos necesarios para TypeScript

### Configuración rápida

Haga clic en el ícono SIGUIENTE en la esquina inferior derecha para abrir configuraciones rápidas donde puede:

1. Activa o desactiva NEXT globalmente
2. Habilite o deshabilite SIGUIENTE para extensiones de archivo específicas

## Escenarios de uso

- **Predicción multipunto en un solo archivo**: al modificar el nombre de una variable o función, NEXT identificará automáticamente todas las ubicaciones de uso relacionadas en el mismo archivo
- **Importación automática de dependencias**: al escribir código que haga referencia a bibliotecas o módulos externos, NEXT detectará y agregará automáticamente las declaraciones de importación requeridas.
- **Completado automático a nivel de función**: NEXT predecirá toda la implementación de la función según el contexto
- **Predicción de edición entre archivos**: cuando se realizan modificaciones en un archivo, NEXT analizará la base del código y hará proactivamente sugerencias de modificaciones relevantes en otros archivos.
