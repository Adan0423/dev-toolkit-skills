# Reglas ATS (Applicant Tracking System)

Un ATS es un software que filtra CVs automáticamente antes de que un humano los vea. Más del 75% de empresas medianas/grandes lo usan. Si el CV no es "legible" para el ATS, puede ser rechazado aunque el candidato sea ideal.

## Checklist de compatibilidad técnica (obligatorio, cualquier rubro)

- [ ] **Formato de archivo**: PDF generado desde Word/Google Docs/similar con texto extraíble (seleccionable). Nunca imagen escaneada ni PDF de solo-imagen.
- [ ] **Una sola columna.** Los diseños de dos columnas (común en plantillas "bonitas" de Canva) confunden a muchos parsers ATS, que leen de izquierda a derecha línea por línea y mezclan el contenido de ambas columnas.
- [ ] **Sin tablas, cuadros de texto ni gráficos** para estructurar contenido. Usar texto plano con bullets.
- [ ] **Headers de sección estándar**: "Experiencia" / "Experiencia laboral", "Educación", "Habilidades", "Certificaciones" — no headers creativos como "Mi trayectoria" o "Lo que sé hacer", que el ATS puede no reconocer como sección estándar.
- [ ] **Fechas en formato consistente y explícito**: "Enero 2020 – Diciembre 2022" o "01/2020 – 12/2022", igual en todo el documento.
- [ ] **Fuente estándar**: Arial, Calibri, Times New Roman, Helvetica, Georgia. Evitar fuentes decorativas.
- [ ] **Datos de contacto detectables**: email y teléfono en texto plano (no como imagen), en la parte superior del documento.
- [ ] **Sin encabezados/pies de página** con información crítica (nombre, contacto) — algunos parsers no los leen.
- [ ] **Nombre de archivo profesional**: "Nombre_Apellido_CV.pdf", no "CV final v3 (2).pdf".

## Optimización de keywords (lo que más mueve el score de "match" con una vacante)

1. Si el usuario tiene una vacante objetivo, pide el texto de la descripción del puesto y extrae:
   - Herramientas/tecnologías/software nombrados explícitamente.
   - Certificaciones o metodologías mencionadas (ej. Scrum, Six Sigma, ISO, GAAP, HIPAA — según el rubro).
   - Soft skills que la vacante repite (ej. "gestión de equipos", "atención al cliente", "análisis de datos").
2. Usa el término **exacto** de la vacante, no solo el sinónimo. Si la vacante dice "Cloud computing" y el CV solo dice "AWS", agregar ambos si es cierto — el ATS busca la palabra literal.
3. Sin vacante específica: usa `adaptacion_por_industria.md` para las keywords típicas del rubro del usuario.
4. **No hagas keyword stuffing invisible** (texto blanco, tamaño 1pt, palabras repetidas sin sentido). Los ATS modernos y ciertamente cualquier reclutador humano lo detectan y penalizan; es la única técnica de esta lista que puede jugar en contra.
5. Evita repetir la misma palabra 5+ veces de forma forzada (ej. "seguridad" repetida sin variar vocabulario) — varía con sinónimos reales del campo cuando sea natural.

## Elementos indispensables que cualquier diagnosticador de CV revisa

Correo electrónico · Nombre completo · Teléfono · LinkedIn (o portafolio relevante) · Ubicación (ciudad, país basta — no la dirección exacta) · sección Educación · sección Experiencia laboral · sección Habilidades.

Si falta cualquiera de estos, es la primera corrección a hacer, antes de trabajar el contenido fino.
