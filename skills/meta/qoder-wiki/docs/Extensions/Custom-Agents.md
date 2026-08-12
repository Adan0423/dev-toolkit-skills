#agentepersonalizado

Agentes personalizados en IA y en Qoders, todas las cosas que son diferentes en manejos y especificaciones.

## Crear un agente personalizado

Cree un archivo `.md` en la siguiente ubicación:

| Ubicación | camino | Alcance |
| --- | --- | --- |
| nivel de usuario | `~/.qoder/agents/<nombreAgente>.md` | Todos los artículos |
| nivel de proyecto | `${proyecto}/.qoder/agents/<nombreAgente>.md` | Sólo proyecto actual |

El archivo debe contener la información básica de la definición del bloque inicial y el contenido de la palabra de aviso del sistema:

```yaml
---
nombre: revisión de código
Descripción: Experto en revisión de código, comprobando la calidad y seguridad del código.
herramientas: Leer, Grep, Glob, Bash
---

Usted es un revisor de código senior responsable de garantizar la calidad del código.

Lista de verificación de revisión:
1. Legibilidad del código
2. Convención de nomenclatura
3. Manejo de errores
4. Control de seguridad
5. Cobertura de prueba
```

| Campo | Requerido | ilustrar |
| --- | --- | --- |
| `nombre` | Sí |
| `descripción` | Sí |
| `herramientas` | No | Lista de herramientas permitidas, separadas por comas |

## Lista de herramientas compatibles

| Nombre de la herramienta | ilustrar |
| --- | --- |
| `Concha` |
| `Editar` |
| `Escribir` | Crear o sobrescribir archivos |
| `Globo` | Recuperar archivos |
| `grep` | Recuperar el contenido del archivo |
| `Leer` | Lea el contenido de un archivo. |
| `WebFetch` | URL especificada |
| `Búsqueda Web` | Realizar una búsqueda web con filtrado de dominio |

## Uso en IDE

En la sala de chat, use el lenguaje natural para describir la tarea y el modelo seleccionará automáticamente el agente personalizado apropiado según la descripción:

```
Ayúdame a revisar la implementación de esta interfaz.
```
