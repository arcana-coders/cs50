# Guía para Crear el Repositorio "resenaya" y Configurar VS Code con Copilot

## Descripción
Esta guía te ayudará a crear un nuevo repositorio llamado "resenaya" y configurar VS Code con GitHub Copilot para trabajar eficientemente con tu proyecto.

## Paso 1: Crear el Repositorio en GitHub

### Opción A: Usando GitHub Web
1. Ve a [GitHub.com](https://github.com) y inicia sesión
2. Haz clic en el botón "+" en la esquina superior derecha
3. Selecciona "New repository"
4. En "Repository name" escribe: `resenaya`
5. Agrega una descripción (opcional): "Proyecto de reseñas"
6. Selecciona si quieres que sea público o privado
7. Marca "Add a README file"
8. Opcionalmente, agrega un .gitignore (selecciona el template apropiado para tu lenguaje)
9. Haz clic en "Create repository"

### Opción B: Usando GitHub CLI
```bash
# Instala GitHub CLI si no lo tienes
# En Windows: winget install GitHub.cli
# En macOS: brew install gh
# En Ubuntu/Debian: sudo apt install gh

# Autentica con GitHub
gh auth login

# Crea el repositorio
gh repo create resenaya --public --add-readme
# O para repositorio privado:
# gh repo create resenaya --private --add-readme
```

## Paso 2: Clonar el Repositorio Localmente

```bash
# Reemplaza 'tu-usuario' con tu nombre de usuario de GitHub
git clone https://github.com/tu-usuario/resenaya.git
cd resenaya
```

## Paso 3: Configurar VS Code

### Instalar Extensiones Necesarias
1. Abre VS Code
2. Ve a Extensions (Ctrl+Shift+X)
3. Instala las siguientes extensiones:
   - **GitHub Copilot** (GitHub.copilot)
   - **GitHub Copilot Chat** (GitHub.copilot-chat)
   - **Git Extension Pack** (donjayamanne.git-extension-pack)
   - **Python** (ms-python.python) - Si trabajas con Python

### Configurar GitHub Copilot
1. Una vez instalado GitHub Copilot, se te pedirá que inicies sesión
2. Haz clic en "Sign in to GitHub"
3. Autoriza VS Code en GitHub
4. Verifica que Copilot esté activo (debería aparecer un icono en la barra de estado)

## Paso 4: Configuración del Workspace de VS Code

Crea el archivo `.vscode/settings.json` en tu proyecto:

```json
{
    "github.copilot.enable": {
        "*": true,
        "yaml": false,
        "plaintext": false,
        "markdown": true
    },
    "editor.inlineSuggest.enabled": true,
    "editor.quickSuggestions": {
        "comments": "on",
        "strings": "on",
        "other": "on"
    },
    "git.autofetch": true,
    "files.autoSave": "afterDelay",
    "editor.formatOnSave": true
}
```

Crea también `.vscode/launch.json` para debugging:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

## Paso 5: Configurar Git

```bash
# Configurar tu información (si no lo has hecho antes)
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"

# Verificar la configuración
git config --global --list
```

## Paso 6: Crear Estructura Inicial del Proyecto

```bash
# Crear directorios básicos
mkdir src docs tests
touch src/main.py
touch README.md
touch .gitignore
touch requirements.txt
```

Ejemplo de `.gitignore` para Python:
```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

## Paso 7: Primer Commit

```bash
# Agregar archivos al staging
git add .

# Hacer commit
git commit -m "Configuración inicial del proyecto resenaya"

# Subir cambios al repositorio remoto
git push origin main
```

## Comandos Útiles para Trabajar con Copilot en VS Code

### Atajos de Teclado
- `Tab`: Aceptar sugerencia de Copilot
- `Ctrl+Enter` (Windows/Linux) o `Cmd+Enter` (macOS): Ver múltiples sugerencias
- `Alt+]`: Siguiente sugerencia
- `Alt+[`: Sugerencia anterior
- `Ctrl+Shift+P` → "GitHub Copilot: Open Chat": Abrir chat de Copilot

### Usar Copilot Chat
1. Abre el chat con `Ctrl+Shift+P` → "GitHub Copilot: Open Chat"
2. Puedes hacer preguntas como:
   - "¿Cómo creo una función para leer archivos CSV?"
   - "Explícame este código"
   - "Refactoriza esta función"
   - "Crea tests para esta función"

## Flujo de Trabajo Recomendado

1. **Planifica tu código**: Escribe comentarios describiendo lo que quieres hacer
2. **Deja que Copilot ayude**: Copilot sugerirá código basado en tus comentarios
3. **Revisa las sugerencias**: No aceptes todo automáticamente, revisa y entiende el código
4. **Haz commits frecuentes**: Guarda tu progreso regularmente
5. **Usa el chat**: Para preguntas específicas o explicaciones

## Comandos Git Útiles

```bash
# Ver estado del repositorio
git status

# Ver historial de commits
git log --oneline

# Crear nueva rama
git checkout -b nueva-funcionalidad

# Cambiar de rama
git checkout main

# Mergear rama
git merge nueva-funcionalidad

# Subir nueva rama
git push -u origin nueva-funcionalidad
```

## Solución de Problemas Comunes

### Copilot no está funcionando
1. Verifica que tienes una suscripción válida de GitHub Copilot
2. Reinicia VS Code
3. Verifica que la extensión esté habilitada
4. Revisa la configuración en `settings.json`

### Problemas con Git
```bash
# Si tienes problemas de autenticación
git config --global credential.helper store

# Para ver la configuración actual
git config --list
```

### Error al hacer push
```bash
# Si hay conflictos, primero hacer pull
git pull origin main

# Resolver conflictos manualmente y luego
git add .
git commit -m "Resolver conflictos"
git push origin main
```

## Recursos Adicionales

- [Documentación de GitHub Copilot](https://docs.github.com/en/copilot)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

¡Ya tienes todo configurado para trabajar en tu repositorio "resenaya" con GitHub Copilot en VS Code!