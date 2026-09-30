# Guía Rápida de Instalación

> **Diferenciación clave**
> 
> - **`SKILL/`** → Paquetes **listos para usar** (`.skill` o `.zip`). Descomprime/copia directamente en tu agente. No requieren compilación.
> - **`skills/`** → Código fuente para **desarrollo, pruebas y mejora** de skills. Úsalos para modificar, iterar o entender su implementación.

## 1. Opción A: Copiar un paquete `.skill` (recomendada)

Los archivos `.skill` son el formato nativo para muchos agentes (OpenCode, Claude Skills, etc.). Son portables y autocontenidos.

```bash
# Clonar repositorio
git clone https://github.com/Adan0423/dev-toolkit-skills.git

# Copiar una skill específica a tu proyecto
cp -r dev-toolkit-skills/SKILL/skill-creator.skill /tu-proyecto/.agents/skills/skill-creator.skill
```

Ruta típica recomendada: `.agents/skills/`

## 2. Opción B: Extraer un `.zip`

```bash
# Extraer
unzip dev-toolkit-skills/SKILL/pdf.zip -d /tu-proyecto/.agents/skills/pdf
```

## 3. Opción C: Usar el repositorio como fuente global

En configuración de tu agente (OpenCode), añade la ruta de `skills/` o `SKILL/` como fuente.

```json
{
  "skillsPath": [
    "C:/Users/TRINIDAD/Downloads/proyectos/dev-toolkit-skills/SKILL",
    "C:/Users/TRINIDAD/Downloads/proyectos/dev-toolkit-skills/skills"
  ]
}
```

> **Recomendación:** Usa **`SKILL/`** para producción/uso diario. Usa **`skills/`** solo si vas a editar o contribuir mejoras.

## 4. Verificación

El agente debería detectar la skill automáticamente al invocarla por su `name` (kebab-case). Si no aparece, reinicia el agente o vuelve a escanear skills.

## 5. Uso

Una vez instalada, actívala **por descripción o nombre**. Ejemplo: *"Usa skill-creator para crear una nueva skill para X"*. La mayoría se activan por **triggers** definidos en su `description`.