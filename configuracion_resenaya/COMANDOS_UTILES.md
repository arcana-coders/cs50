# Comandos Útiles para el Repositorio "resenaya"

## Comandos Git Esenciales

### Configuración Inicial
```bash
# Configurar tu identidad (solo la primera vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"

# Verificar configuración
git config --list
```

### Trabajar con el Repositorio
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/resenaya.git
cd resenaya

# Ver estado actual
git status

# Ver diferencias
git diff

# Agregar archivos al staging
git add archivo.py          # Agregar archivo específico
git add .                   # Agregar todos los archivos
git add src/                # Agregar directorio completo

# Hacer commit
git commit -m "Descripción del cambio"

# Subir cambios
git push origin main
git push                    # Si ya está configurado upstream

# Obtener cambios del repositorio remoto
git pull origin main
git pull                    # Si ya está configurado upstream
```

### Trabajar con Ramas
```bash
# Ver ramas
git branch                  # Ver ramas locales
git branch -a              # Ver todas las ramas

# Crear nueva rama
git checkout -b nueva-funcionalidad
git switch -c nueva-funcionalidad    # Comando moderno

# Cambiar de rama
git checkout main
git switch main             # Comando moderno

# Mergear rama
git checkout main
git merge nueva-funcionalidad

# Eliminar rama
git branch -d nueva-funcionalidad    # Eliminar rama local
git push origin --delete nueva-funcionalidad  # Eliminar rama remota
```

### Historial y Logs
```bash
# Ver historial
git log
git log --oneline          # Versión compacta
git log --graph --oneline  # Con gráfico de ramas

# Ver cambios específicos
git show commit-hash
git show HEAD              # Último commit
git show HEAD~1            # Penúltimo commit
```

## Comandos de Python y Entorno Virtual

### Crear y Usar Entorno Virtual
```bash
# Crear entorno virtual
python -m venv venv
python3 -m venv venv       # En Linux/macOS

# Activar entorno virtual
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/macOS

# Desactivar entorno virtual
deactivate

# Instalar dependencias
pip install -r requirements.txt

# Generar requirements.txt
pip freeze > requirements.txt

# Instalar paquete individual
pip install requests
pip install pytest --dev  # Para desarrollo
```

### Ejecutar el Proyecto
```bash
# Ejecutar archivo principal
python src/main.py

# Ejecutar con argumentos
python src/main.py --input data/file.txt

# Ejecutar tests
python -m pytest
python -m pytest tests/
python -m pytest -v       # Verbose
python -m pytest --cov    # Con coverage
```

## Comandos de VS Code desde Terminal

```bash
# Abrir VS Code en el directorio actual
code .

# Abrir archivo específico
code src/main.py

# Instalar extensión
code --install-extension ms-python.python
code --install-extension GitHub.copilot

# Ver extensiones instaladas
code --list-extensions
```

## Comandos de GitHub CLI (gh)

```bash
# Autenticarse
gh auth login

# Crear repositorio
gh repo create resenaya --public --clone

# Ver información del repositorio
gh repo view

# Crear issue
gh issue create --title "Bug en main.py" --body "Descripción del problema"

# Ver issues
gh issue list

# Crear pull request
gh pr create --title "Nueva funcionalidad" --body "Descripción"

# Ver pull requests
gh pr list
```

## Atajos de VS Code con Copilot

### Atajos de Teclado
- `Tab`: Aceptar sugerencia de Copilot
- `Esc`: Rechazar sugerencia
- `Ctrl+Enter` (Windows/Linux) / `Cmd+Enter` (macOS): Ver múltiples sugerencias
- `Alt+]`: Siguiente sugerencia
- `Alt+[`: Sugerencia anterior
- `Ctrl+Shift+P`: Paleta de comandos
- `Ctrl+`` ` ``: Abrir/cerrar terminal
- `Ctrl+Shift+`` ` ``: Crear nueva terminal

### Comandos de Copilot
- `Ctrl+Shift+P` → "GitHub Copilot: Open Chat"
- `Ctrl+Shift+P` → "GitHub Copilot: Enable/Disable"
- `Ctrl+Shift+P` → "GitHub Copilot: Generate Tests"

## Tips para Usar Copilot Efectivamente

### 1. Escribir Comentarios Descriptivos
```python
# Función para leer archivo CSV y convertirlo a lista de diccionarios
def read_csv_file(filename):
    # Copilot sugerirá el código aquí
```

### 2. Usar Nombres de Variables Descriptivos
```python
# Mejor
user_reviews = []
average_rating = 0.0

# Peor
data = []
x = 0.0
```

### 3. Crear Funciones con Docstrings
```python
def analyze_sentiment(text):
    """
    Analiza el sentimiento de un texto y retorna un score.
    
    Args:
        text (str): El texto a analizar
        
    Returns:
        float: Score de sentimiento (-1 a 1)
    """
    # Copilot sugerirá la implementación
```

### 4. Usar el Chat de Copilot
- "Explica esta función"
- "¿Cómo puedo optimizar este código?"
- "Crea tests para esta función"
- "Refactoriza este código para mejor legibilidad"

## Flujo de Trabajo Recomendado

### 1. Desarrollo Diario
```bash
# Inicio del día
git pull origin main
git status

# Durante el desarrollo
git add .
git commit -m "Descripción clara del cambio"
git push origin main

# Fin del día
git status  # Verificar que todo está committed
```

### 2. Nueva Funcionalidad
```bash
# Crear nueva rama
git checkout -b feature/nueva-funcionalidad

# Desarrollar y hacer commits
git add .
git commit -m "Implementar nueva funcionalidad"

# Subir rama
git push -u origin feature/nueva-funcionalidad

# Crear PR (si usas GitHub)
gh pr create --title "Nueva funcionalidad"

# Después de merge, limpiar
git checkout main
git pull origin main
git branch -d feature/nueva-funcionalidad
```

### 3. Corrección de Bugs
```bash
# Crear rama para el fix
git checkout -b fix/bug-descripcion

# Hacer el fix y commit
git add .
git commit -m "Fix: descripción del problema resuelto"

# Subir y crear PR
git push -u origin fix/bug-descripcion
gh pr create --title "Fix: descripción del bug"
```

## Comandos de Troubleshooting

### Problemas Comunes
```bash
# Descartar cambios locales
git checkout -- archivo.py
git restore archivo.py     # Comando moderno

# Volver al último commit
git reset --hard HEAD

# Ver qué cambió en un archivo
git diff HEAD archivo.py

# Buscar en el código
grep -r "función" src/     # Linux/macOS
findstr /s "función" src\* # Windows

# Ver archivos grandes
find . -type f -size +10M  # Linux/macOS

# Limpiar archivos no trackeados
git clean -fd
```

### Problemas de Merge
```bash
# Si hay conflictos después de pull
git status                 # Ver archivos en conflicto
# Editar archivos manualmente para resolver conflictos
git add .
git commit -m "Resolver conflictos"
```

## Recursos Útiles

- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [VS Code Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [GitHub CLI Manual](https://cli.github.com/manual/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)