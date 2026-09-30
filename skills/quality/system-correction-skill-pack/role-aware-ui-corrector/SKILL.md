---
name: role-aware-ui-corrector
description: >
  Corrige UI, formularios, paneles, dashboards, navegación, imágenes y representación
  de datos para que cada usuario vea información correcta según su rol y estado real.
  Valida que la UI esté sincronizada con backend y base de datos sin tratar el
  ocultamiento visual como autorización.
version: 1.0.0
language: es
tags:
  - ui
  - ux
  - dashboard
  - forms
  - uploads
  - role-aware
  - data-binding
---

# Role-Aware UI Corrector

## Objetivo

Asegurar que la interfaz:

1. muestre datos correctos;
2. muestre solo acciones relevantes al rol;
3. represente correctamente permisos;
4. maneje estados reales;
5. se mantenga sincronizada con backend/DB.

---

# 1. No corregir solo apariencia

Antes de cambiar diseño identifica:

- fuente de datos;
- contrato/API;
- estado;
- rol;
- permiso;
- error real;
- resultado esperado.

Si el dashboard muestra `0` por un error de query, no cambies el componente visual:
corrige el flujo de datos.

---

# 2. Mapa de superficies

## Público

- home;
- landing;
- catálogo;
- contenido publicado;
- login/registro;
- páginas legales.

No mostrar:
- datos internos;
- borradores;
- acciones administrativas.

## Usuario autenticado

- perfil;
- recursos propios;
- historial;
- preferencias.

## Dashboard por rol

Cada módulo debe declarar:

- `visible`;
- `readable`;
- `actionable`;
- permiso requerido;
- fuente de datos.

---

# 3. Roles y navegación

La navegación debe:

- evitar links inútiles;
- evitar opciones no permitidas;
- mostrar módulos correspondientes;
- manejar redirecciones;
- cargar permisos antes de renderizar acciones sensibles.

Pero el backend/DB debe volver a validar el permiso.

---

# 4. Estados obligatorios

Cada vista de datos debe contemplar:

- loading;
- success;
- empty;
- partial;
- stale si aplica;
- unauthorized;
- forbidden;
- not found;
- validation error;
- server error;
- network error;
- retry.

No mostrar “No hay datos” cuando realmente hubo error.

---

# 5. Formularios

Auditar:

- campos correctos;
- required;
- tipos;
- rangos;
- formatos;
- validación cliente;
- validación servidor;
- mensajes;
- submit;
- double submit;
- disabled state;
- loading;
- success;
- reset;
- errores por campo;
- errores globales.

El servidor sigue siendo autoridad.

---

# 6. Imágenes y archivos

Verificar:

- selección;
- preview;
- MIME;
- tamaño;
- dimensiones cuando corresponda;
- nombre;
- path;
- upload;
- progreso;
- cancelación;
- URL final;
- permisos;
- cache busting;
- reemplazo;
- borrado;
- fallback visual.

No usar una imagen genérica para ocultar que la carga falló.

Distinguir:

- imagen pública;
- imagen privada;
- signed URL;
- asset empaquetado.

---

# 7. Data binding

Para web/mobile/desktop:

- una fuente de verdad;
- estado observable;
- evitar duplicar datos derivados;
- invalidar/actualizar después de mutaciones;
- evitar carreras;
- evitar datos de usuario anterior;
- limpiar estado al cerrar sesión;
- manejar cambio de rol/sesión.

---

# 8. Dashboard

Verificar cada KPI:

1. definición;
2. query/API;
3. filtro;
4. rango temporal;
5. tenant/usuario;
6. permisos;
7. agregación;
8. formato;
9. actualización.

Nunca asumir que un número visual es correcto solo porque renderiza.

---

# 9. Tablas y listados

Revisar:

- columnas por rol;
- filtros;
- búsqueda;
- orden;
- paginación;
- total;
- loading;
- empty;
- acciones por fila;
- selección;
- bulk actions;
- permisos.

---

# 10. Responsive / mobile / desktop

Mantener diseño existente salvo que cause el problema.

Corregir:

- overflow;
- touch targets;
- teclado;
- safe areas;
- orientación;
- tamaños;
- formularios;
- tablas;
- navegación;
- dialogs;
- estados de error.

---

# 11. Accesibilidad básica

Verificar:

- labels;
- foco;
- navegación por teclado;
- roles semánticos;
- contraste;
- mensajes de error;
- alt text apropiado;
- controles deshabilitados comprensibles.

---

# 12. Prueba por actor

Ejecutar el mismo flujo como:

- visitante;
- usuario;
- propietario;
- rol intermedio;
- admin;
- usuario sin permiso.

Comparar:

- navegación;
- datos;
- acciones;
- errores;
- resultado persistido.

---

# 13. Salida

Para cada corrección indicar:

- pantalla;
- rol;
- síntoma;
- causa raíz;
- fuente de datos;
- cambio UI;
- cambio backend/DB si existió;
- verificación.
