#Habilidades

Skills es un mecanismo en Qoder que empaqueta el conocimiento profesional en funciones reutilizables. Cada habilidad contiene un archivo `SKILL.md` que define la descripción, las instrucciones y los archivos auxiliares opcionales de la habilidad.

## Funciones principales

- **Llamada inteligente**: el modelo decide de forma autónoma cuándo usarlo según la solicitud del usuario y la descripción de la habilidad.
- **Diseño Modular**: Cada Habilidad se enfoca en resolver un tipo específico de tarea
- **Expansión flexible**: admite habilidades personalizadas a nivel de usuario y de proyecto

## Instalar habilidad

### Instalación rápida (recomendado)

Utilice la CLI de habilidades para la instalación con un solo clic:

```bash
# Instalar desde el mercado skills.sh
Las habilidades de npx agregan vercel-labs/agent-browser -a qoder

# Instalar la habilidad especificada desde el repositorio de GitHub
habilidades npx agregan https://github.com/anthropics/skills --skill Skill-creator -a qoder
```

### Instalación manual

Después de copiar manualmente el archivo Skill de destino en la siguiente ruta, reinicie Qoder IDE:

| ubicación | camino | alcance |
| --- | --- | --- |
| Nivel de usuario | `~/.qoder/skills/{nombre-habilidad}/SKILL.md` | Todos los proyectos del usuario actual |
| Nivel de proyecto | `.qoder/skills/{nombre-habilidad}/SKILL.md` | Sólo proyecto actual |

> Cuando tienen el mismo nombre, la Habilidad a nivel de proyecto anula la Habilidad a nivel de usuario.

## Cómo utilizar

### Activar automáticamente

Describa directamente los requisitos y el modelo determinará automáticamente si se utiliza la habilidad adecuada:

```
Analizar errores en este archivo de registro
```

### Gatillo manual

Ingrese `/skill-name` para activar manualmente:

```
/analizador-de-logs
```

## Escenarios de uso

**Escenarios adecuados para usar Skill**:

- **Tareas profesionales complejas**: flujos de trabajo que requieren conocimientos del dominio (revisión de código, procesamiento de PDF, diseño de API)
- **Proceso estandarizado**: Tareas realizadas en pasos fijos (especificaciones de envío, proceso de implementación)
- **Intercambio de conocimientos en equipo**: mejores prácticas de paquetes para uso de equipos
- **Trabajo repetitivo**: Tareas que se realizan con frecuencia y requieren orientación profesional.

## Ejemplo de escenario

- **Análisis de registros**: cree una habilidad de "analizador de registros" para ayudar a identificar errores, problemas de rendimiento y patrones inusuales.
- **Generación de documentación API**: cree la habilidad `api-doc-generator` para identificar automáticamente los puntos finales de API y generar documentación estándar
- **Revisión de código**: cree la habilidad "revisor de código" para revisar el código automáticamente de acuerdo con las especificaciones del equipo.
