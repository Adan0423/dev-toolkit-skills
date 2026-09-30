# Incremental Android Refactor Playbook

## Objetivo

Reducir monolitos sin romper comportamiento ni acumular una cadena larga de cambios no verificados.

## Secuencia para archivos >1000 líneas

1. Identificar responsabilidades concretas.
2. Mapear dependencias entrantes/salientes.
3. Identificar estado mutable, side effects y lifecycle.
4. Seleccionar una responsabilidad con boundary claro.
5. Extraerla con el mínimo cambio de firma necesario.
6. Compilar el módulo afectado.
7. Ejecutar tests relevantes.
8. Revisar diff y comportamiento.
9. Repetir con la siguiente responsabilidad.

No empezar moviendo todo a carpetas nuevas. El valor está en separar responsabilidades y dependencias, no en reorganizar nombres.

## Patrón objetivo pragmático

```text
presentation
  ├─ route/screen/components
  ├─ viewmodel
  └─ ui-state/events
        ↓
domain
  ├─ models
  ├─ use-cases
  └─ repository contracts
        ↑
data
  ├─ repository implementations
  ├─ remote
  ├─ local
  └─ mappers
```

No imponer esta estructura cuando un feature simple no la necesita.

## Compose

Extraer primero piezas con alta cohesión visual:

- header;
- form;
- list/content;
- dialogs/sheets;
- reusable cells/cards;
- stateful Route separado de Screen stateless cuando convenga.

Evitar un archivo genérico `Components.kt` que vuelva a convertirse en un monolito.

## ViewModel

Si es demasiado grande, identificar qué ocupa espacio:

- reglas de negocio → UseCase/domain service;
- transformación de modelos → mapper;
- persistencia/remoto → Repository/data source;
- reducción compleja de estado → reducer/state handler;
- validación reutilizable → validator/domain rule.

No resolver un ViewModel gigante creando varios ViewModels igualmente gigantes.

## UseCases

Crear un UseCase cuando represente una intención de negocio coherente o encapsule política/reglas. Evitar UseCases que solo renombren un getter/setter sin aportar boundary, testabilidad o semántica.

## Repositories

Separar interfaz/implementación cuando exista una frontera real entre dominio e infraestructura, múltiples fuentes de datos, testabilidad relevante o posibilidad razonable de sustitución.

## Validación por lote pequeño

Tras cada extracción:

- verificar package/imports;
- verificar visibilidad y DI;
- buscar todas las referencias de firmas modificadas;
- compilar el task más pequeño útil;
- ejecutar tests del componente/módulo;
- inspeccionar el diff;
- continuar solo con base verde.

## Git safety

Antes de escribir, inspeccionar `git status` cuando Git esté disponible. No sobrescribir cambios no relacionados del usuario. No usar comandos destructivos para “limpiar” el repositorio.

## Fin de refactor

Entregar:

- arquitectura antes/después;
- lista de archivos creados/modificados/eliminados;
- métricas de archivos >300 y >1000 antes/después;
- seguridad corregida/pendiente;
- comandos ejecutados;
- resultados de compilación/tests/lint;
- riesgos o deuda restante.
