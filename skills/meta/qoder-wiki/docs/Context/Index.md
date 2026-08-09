# índice base de código

Cuando abre un proyecto, Qoder indexa automáticamente la base del código generando vectores de incrustación de archivos. Esto permite la comprensión del código basada en IA, recomendaciones inteligentes y búsqueda semántica. La indexación se produce de forma incremental, por lo que los archivos nuevos o modificados se procesan en tiempo real, sin intervención manual.

## Configurar índice

1. En la esquina superior derecha de Qoder IDE, haga clic en el icono de usuario y seleccione **Configuración de Qoder**
2. En la barra de navegación izquierda, haga clic en **Índice base de código**
3. Seleccione uno de los siguientes:
   - Para habilitar la indexación manualmente, haga clic en **Crear** junto a **Índice base de código**
   - Para habilitar la indexación en segundo plano persistente, cambie **Actualizaciones automáticas** a Activado

> **Nota:** Admite bases de código de hasta 100 000 archivos. Para bases de código con menos de 10.000 archivos, las actualizaciones automáticas están activadas de forma predeterminada. Para bases de código más grandes, la indexación debe habilitarse manualmente.

## ignorar archivo

De forma predeterminada, Qoder indexa todos los archivos del proyecto con las siguientes excepciones:

- Archivos y directorios especificados en `.gitignore`
- Archivos listados en `.qoderignore`

### Especificar archivos ignorados personalizados

Puede definir archivos o directorios adicionales que deben excluirse del índice.

1. En la esquina superior derecha de Qoder IDE, haga clic en el icono de usuario y seleccione **Configuración de Qoder**
2. En la barra de navegación izquierda, haga clic en **Índice base de código**
3. Haga clic en **Administrar** junto a **Ignorar archivos**
4. Agregue un patrón coincidente personalizado

### Ejemplo de patrón

| Formato | describir |
| --- | --- |
| configuración.json | Ignorar archivos específicos |
| dist/ | ignorar todo el directorio |
| *.registro | Ignorar todos los archivos con extensión .log |
| **/registros | Ignorar directorios de registros en cualquier nivel de anidamiento |
| !aplicación/ | Excluir una ruta de las reglas de ignorar (negar) |

## Preguntas frecuentes

### ¿Dónde puedo ver bases de códigos indexados?

Actualmente no existe una lista de índice centralizada. Puede ver los repositorios indexados en la configuración de indexación de cada proyecto.

### ¿Mi código fuente estará alojado en los servidores de Qoder?

No. Qoder no almacena su código fuente.
