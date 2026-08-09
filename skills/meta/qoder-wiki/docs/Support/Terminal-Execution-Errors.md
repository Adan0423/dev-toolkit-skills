# Excepción de ejecución de terminal

## Introducción

Cuando se utiliza el modo de agente Qoder, la ejecución del terminal depende en gran medida de su entorno local y de la configuración del shell. Puede encontrar los siguientes problemas:

- No se puede iniciar la terminal
- El comando no se puede ejecutar.
- sin salida

## Métodos comunes de solución de problemas

### Método 1: configurar un shell compatible

Qoder admite múltiples shells. Asegúrese de estar utilizando un shell compatible.

1. Abrir Qoder
2. Presione `Cmd + Shift + P` (macOS) o `Ctrl + Shift + P` (Windows/Linux) para abrir el panel de comandos
3. Ingrese a `Terminal: Seleccionar perfil predeterminado` y selecciónelo
4. Seleccione un shell compatible:
   - Linux/macOS: `bash`, `fish`, `pwsh`, `zsh`
   - Windows: `Git Bash`, `pwsh`
5. Cierre y vuelva a abrir completamente Qoder

### Método 2: instalar manualmente la integración del shell

Agregue las declaraciones correspondientes en el archivo de configuración del shell:

**zsh** (`~/.zshrc`):
```bash
[[ "$TERM_PROGRAM" == "vscode" ]] &&. "$(código --locate-shell-integration-path zsh)"
```

**Bash** (`~/.bashrc`):
```bash
[[ "$TERM_PROGRAM" == "vscode" ]] &&. "$(código --locate-shell-integration-path bash)"
```

**PowerShell**(`$Perfil`):
```powershell
si ($env:TERM_PROGRAM -eq "vscode") { . "$(código --locate-shell-integration-path pwsh)" }
```

## Si el problema persiste

1. Haga clic en el botón **Terminar Terminal** para cerrar la sesión actual del terminal.
2. Vuelva a ejecutar el comando

## Solución de problemas específicos de Windows

### Git Bash

1. Descargue e instale Git para Windows desde https://git-scm.com/downloads/win
2. Salga y vuelva a abrir Qoder
3. Establezca Git Bash como terminal predeterminado

### PowerShell

1. Asegúrate de estar usando PowerShell 7 o superior
2. Ajustar la estrategia de ejecución:
   ```powershell
   Set-ExecutionPolicy RemoteSigned-Scope Usuario actual
   ```

##Salida del terminal de excepción

**Síntomas:** Caracteres confusos, símbolos cuadrados, secuencias de escape

**Posibles motivos:** Configuración personalizada del shell de terceros, como Powerlevel10k, Oh My Zsh

**Solución:** Deshabilite los mensajes o temas complejos para la terminal de ejecución del Agente

```bash
# ~/.zshrc: deshabilita Powerlevel10k cuando se ejecuta el terminal Qoder Agent
si [[ -n "$QODER_AGENT" ]]; entonces
  # Omitir la inicialización del tema para una mejor compatibilidad
demás
  [[ -r ~/.p10k.zsh ]] && fuente ~/.p10k.zsh
fi
```
