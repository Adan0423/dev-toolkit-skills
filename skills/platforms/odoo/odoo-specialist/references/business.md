# Configuración y flujos funcionales

Inspecciona apps/roles, compañías y proceso actual. Configura nativo antes de automatizar.
Registra valores previos, dependencias, aceptación y qué estados cambian. No asumir
que un campo visible en otra edición exista aquí. La tabla orienta investigación:

| Área | Revisión funcional y aceptación |
|---|---|
| CRM | Etapas, equipos, leads, actividades, ownership y conversión a cotización |
| Ventas | Pricelist, moneda, descuentos, impuestos, cotización/orden y facturación |
| Compras | Proveedores, UoM, lead time y recepción/factura según políticas |
| Inventario | Ubicaciones, rutas, reservas, lotes/series, UoM y trazabilidad |
| Fabricación | BoM, operaciones, consumo, producción y costes según apps |
| Contabilidad | Localización, diarios, impuestos, moneda y conciliación |
| POS | Configuración sesión, catálogo, pagos y sincronización en alcance |
| Proyecto/Servicio | Etapas, tiempos, permisos, facturabilidad y tareas |
| RRHH | Roles/privacidad, documentos y acceso; nómina según módulos/localización |
| Website/eCommerce | Publicación, catálogo, variantes, carrito y checkout reales |

Para cada flujo identifica registros/modelos disponibles, métodos de transición y
efectos downstream. Usa action/método correcto en vez de escribir state a mano.
No crear inventario por editar quantity sin flujo estándar ni marcar invoice pagada
sin el proceso contable. No confirma pedidos o valida transferencias como prueba visual.

Los cambios de moneda, impuestos, valoración, secuencias, localización, rutas o pagos
pueden afectar documentos existentes: evalúa alcance y prueba copia representativa.
No cambia estos parámetros como consecuencia implícita de mejorar UI. Funciones de
Studio o automatizaciones pueden enviar correo, generar actividades o documentos;
inspecciona disparadores antes de crear/actualizar registros en lote.

Para normativa/fiscalidad investiga localización oficial de versión/país y autoridad
vigente; explica lo que requiere validación funcional/contable. No inventa tipos de
impuesto ni presenta configuración como cumplimiento certificado. No envía documentos
fiscales, pagos o mensajes sin solicitud directa o autorización aplicable.

Entrega instrucciones operativas por rol y ejemplo con datos de prueba que permita
comprobar el proceso completo, distinguiendo configuración de ejecución comercial.
