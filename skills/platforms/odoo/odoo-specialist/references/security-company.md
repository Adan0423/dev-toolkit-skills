# Permisos y multiempresa

Verifica mecanismos en versión real. En 19.0, ACL otorga CRUD por modelo/grupos de
forma aditiva; sin concesión aplicable no hay acceso. Record rules restringen registros
tras ACL y permiten si ninguna aplica. Globales intersectan; de grupos se unen dentro
del límite global. Una regla no concede acceso de modelo. ACL sin grupo puede abrir
portal/público. Métodos públicos necesitan validar argumentos, permisos y operaciones.
Sudo puede evitar límites: no usarlo como reparación general.

Prueba rol autorizado y no autorizado, usuario interno, portal/público pertinentes y
lectura/escritura/create/unlink reales. Incluye campos sensibles, adjuntos, reportes,
controllers/API y compañía ajena; ocultar menú o botón no protege datos.

Identifica compañía activa y allowed_company_ids. Campos dependientes de compañía
requieren contexto correcto/with_company cuando corresponda. En modelos adecuados
revisa company_id, _check_company_auto y check_company en relaciones; no agregar
check_company al propio company_id. No asumir que datos compartidos sin compañía
equivalen a permiso público. Comprueba dos compañías y registros compartidos permitidos,
con moneda, unidades, impuestos y secuencias correctos.

Documenta matriz rol→operación→alcance→prueba. Tras cambiar permisos prueba usuario
normal, no solo superusuario. No clasifica AccessError como conjunto vacío.
