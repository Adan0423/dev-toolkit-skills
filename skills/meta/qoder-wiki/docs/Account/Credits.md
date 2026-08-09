# Créditos

Los usuarios no pueden utilizar modelos de lenguaje grandes de alto nivel sin restricciones, por lo que adoptamos un mecanismo de cuota basado en Créditos. Los créditos representan cuotas de recursos consumidas por la IA mientras realiza tareas.

## Función para consumir Créditos

En Qoder, las siguientes solicitudes de usuarios consumen Créditos:

- Chat en línea
- modo preguntar
- Modo agente
- Modo de búsqueda
- Repositorio Wiki

La cantidad exacta de créditos consumidos variará según la complejidad de la tarea y el modelo avanzado específico utilizado.

## Cómo deducir créditos

Los créditos adquiridos en diferentes momentos tienen diferentes tiempos de vencimiento. El sistema dará prioridad al uso de los Créditos que caduquen primero para ayudarle a maximizar el valor de sus Créditos.

Incluso si el usuario ha agotado la cuota del modelo avanzado (es decir, los créditos se han agotado), seguiremos proporcionando una cuota de llamadas diaria limitada para el modelo básico.

## error

Los créditos no se deducen por solicitudes fallidas del modelo Qoder. Los créditos se deducen solo si la llamada a la API del modelo se realiza correctamente.

## Guía de Consumo de Tareas y Créditos

|  | Mediana (ventana de contexto de 50K) | Mediana (ventana de contexto de 200K) |
| --- | --- | --- |
| Preguntar | ~ 3 Créditos / Solicitud de Usuario | ~ 4 Créditos / Solicitud de Usuario |
| Agente | ~ 7 Créditos / Solicitud de Usuario | ~ 12 Créditos / Solicitud de Usuario |
| Búsqueda | / | ~ 100 créditos / tarea de misión |
| Repositorio Wiki | / | ~ 50 Créditos / Repositorio |

**Nota:** A medida que se lancen nuevas funciones en el futuro, es posible que actualicemos la tasa de consumo de Créditos según sus requisitos de recursos.

## Ver uso de créditos

Inicie sesión en el sitio web oficial de Qoder. Haz clic en el avatar en la esquina superior derecha y ve a Configuración > Uso.

Aquí puede ver el Plan actual, así como la información de Créditos disponibles y utilizados en el paquete de recursos.

- **Prioridad de uso de créditos**: los créditos que caduquen primero se consumirán primero
- **Vencimiento de los créditos**: Pérdida de diferentes tipos de créditos tienen sus propios tiempos de vencimiento.

Los créditos obtenidos a través del plan son válidos para el período de suscripción actual.
