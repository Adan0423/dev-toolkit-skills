# Reorganización segura de frontends

## Señales que justifican reorganizar

- archivos de página enormes con responsabilidades mezcladas;
- duplicación de markup/estilos/lógica;
- features distribuidas sin criterio;
- imports circulares o difíciles de seguir;
- componentes genéricos demasiado configurables;
- componentes copiados con pequeñas variantes;
- `utils/helpers/common/misc` sin límites claros;
- tokens visuales repetidos como valores mágicos;
- routing/layout/state mezclados con detalles presentacionales;
- módulos sin ownership claro.

## Procedimiento

1. Mapea rutas y puntos de entrada.
2. Mapea dependencias por feature.
3. Detecta contratos públicos del frontend.
4. Propón internamente límites destino.
5. Mueve una unidad coherente por vez.
6. Actualiza imports y aliases.
7. Ejecuta validaciones.
8. Continúa solo si el cambio anterior quedó estable.

## Eliminación de código

Antes de eliminar confirma ausencia de:

- imports estáticos;
- imports dinámicos;
- referencias en rutas;
- uso desde tests/stories;
- referencias de configuración/build;
- nombres consumidos por plugins;
- uso por templates del servidor;
- referencias CSS por selector/atributo;
- uso en documentación/generadores cuando sea operativo.

Si hay duda material, conserva o depreca; no borres a ciegas.
