# Modelado NoSQL por patrón de acceso

NoSQL incluye modelos distintos; no transforma cada tabla SQL en una colección ni
asume falta de esquema/validación. Mantén invariantes, consistencia requerida, cardinalidad
y límites de crecimiento explícitos. Revalida capacidades por producto/edición.

## Documentos: MongoDB

Elige embedding para datos acotados que se leen y cambian como agregado; referencias para
entidades independientes o crecimiento abierto. Registra fan-out, tamaño y lecturas/escrituras
dominantes. Evita arrays que crecen sin límite o documentos gigantes; revisa límites BSON.
Desnormalización necesita fuente y proceso de reparación, no promesa de sincronización.

Valida tipos, campos obligatorios y rangos con validator/JSON Schema soportado. Define
validationLevel/action y qué pasará con documentos antiguos; un cambio de validator no
certifica que todo el histórico cumple. Constraints de colección e índices únicos son
distintos de validación de campos; revisar null/missing, partial/sparse y sharding.

Índices desde filtro/orden, con pruebas explain y coste de escritura. Evita índice para
todo campo y considera multikey y índices compuestos. IDs de tenant deben limitar consultas,
lookup y escritura; projection no es autorización de campos. Transacción multi-documento
solo cuando el despliegue la soporte y el invariante lo requiera. No usa transacciones
como sustituto de un agregado bien definido.

[Validator de ejemplo](../assets/mongodb-order-validator.json) es configuración ilustrativa
de una colección de órdenes, no código SQL. `maxItems:100` representa una regla del
ejemplo, no recomendación universal. No comprueba existencia de clientes/productos ni
aislamiento; esa integridad y autorización deben implementarse y probarse aparte.

## DynamoDB y clave-valor

Lista access patterns antes de PK/SK e índices: clave de partición, orden, consulta,
consistencia, tenant, frecuencia, cardinalidad y hot keys. Diseña claves desde acceso,
no desde entidades solamente. Query eficiente, scan y filtro posterior no son equivalentes.
Cada GSI implica duplicación, coste y consistencia propios; no añade un índice sin una
consulta justificada. Single-table es una opción con tradeoffs, no una obligación.

Usa condiciones/transacciones e idempotencia cuando la regla lo necesite. Distingue
consistencia del índice/operación elegidos. TTL no garantiza borrado instantáneo ni
revoca acceso a datos aún existentes. Revisa IAM por recurso/operación y claves permitidas;
acceso vía backend privilegiado exige autorización propia, incluidos índices y scans.

## Firestore

Diseña documentos/colecciones desde consultas, índices, tamaño y contención. Un documento
no debe convertirse en contador global caliente sin analizar concurrencia. Seguridad
cliente necesita Rules; servidor/Admin SDK usa IAM y autorización de backend.
Las reglas no filtran una consulta amplia a los documentos permitidos: la consulta debe
ser demostrablemente autorizada. Separa campos secretos en documentos con acceso distinto
si no pueden revelarse junto al documento permitido. Prueba reglas con emulador cuando
disponible; no confunde validación de escritura de campos con ocultación de lectura.

## Redis, grafo y otros

Redis: formato de key/namespace, TTL, atomicidad, concurrencia, persistencia y memoria
son parte del modelo. ACL por comandos/keys no equivale a permisos por campo JSON.
Una cache tiene invalidación y fuente; no almacena credenciales en keys/logs.

Grafo: modela nodos/edges y constraints del motor real desde recorridos. Documenta
coste, direccionalidad, fan-out, pertenencia y autorización en cada traversal; usa
parámetros y límites. Series temporales: tiempo de evento/ingestión, cardinalidad,
retención y consultas. Vectorial: metadatos de pertenencia, filtros verificados,
procedencia y borrado de embeddings asociados. No filtra tenant solo después de devolver
documentos sensibles al cliente. No simula soporte en un motor sin comprobarlo.

## Evolución

Versiona documentos, valida coexistencia de lectores/escritores y backfill idempotente.
Comprueba divergencia entre copia desnormalizada y fuente. Para cambios usa
[migraciones](migrations.md) y [seguridad](security.md), según tarea.
