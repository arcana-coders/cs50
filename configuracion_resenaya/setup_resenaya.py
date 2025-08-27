#!/usr/bin/env python3
"""
Script de configuración automática para el repositorio 'resenaya'
Automatiza los pasos básicos de configuración del proyecto
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def run_command(command, check=True):
    """Ejecuta un comando y maneja errores"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=check)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando comando: {command}")
        print(f"Error: {e.stderr}")
        return None


def create_directory_structure():
    """Crea la estructura básica de directorios"""
    directories = [
        'src',
        'tests',
        'docs',
        'data',
        '.vscode'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ Directorio creado: {directory}")


def create_basic_files():
    """Crea archivos básicos del proyecto"""
    
    # README.md
    readme_content = """# Reseñas

Proyecto para gestión y análisis de reseñas.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python src/main.py
```

## Estructura del Proyecto

- `src/`: Código fuente principal
- `tests/`: Pruebas unitarias
- `docs/`: Documentación
- `data/`: Archivos de datos

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✓ README.md creado")
    
    # src/main.py
    main_content = '''"""
Archivo principal del proyecto de reseñas
"""

def main():
    print("¡Bienvenido al sistema de reseñas!")
    # TODO: Implementar funcionalidad principal


if __name__ == "__main__":
    main()
'''
    
    with open('src/main.py', 'w', encoding='utf-8') as f:
        f.write(main_content)
    print("✓ src/main.py creado")
    
    # tests/test_main.py
    test_content = '''"""
Tests para el módulo main
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from main import main


def test_main():
    """Test básico para la función main"""
    # TODO: Implementar tests reales
    assert True
'''
    
    with open('tests/test_main.py', 'w', encoding='utf-8') as f:
        f.write(test_content)
    print("✓ tests/test_main.py creado")


def copy_config_files():
    """Copia los archivos de configuración de ejemplo"""
    config_source = Path(__file__).parent / "configuracion_resenaya"
    
    if not config_source.exists():
        print("⚠️  Directorio de configuración no encontrado")
        return
    
    # Copiar settings.json
    if (config_source / "vscode-settings.json").exists():
        shutil.copy(config_source / "vscode-settings.json", ".vscode/settings.json")
        print("✓ .vscode/settings.json copiado")
    
    # Copiar launch.json
    if (config_source / "vscode-launch.json").exists():
        shutil.copy(config_source / "vscode-launch.json", ".vscode/launch.json")
        print("✓ .vscode/launch.json copiado")
    
    # Copiar .gitignore
    if (config_source / "gitignore-python").exists():
        shutil.copy(config_source / "gitignore-python", ".gitignore")
        print("✓ .gitignore copiado")
    
    # Copiar requirements.txt
    if (config_source / "requirements-example.txt").exists():
        shutil.copy(config_source / "requirements-example.txt", "requirements.txt")
        print("✓ requirements.txt copiado")


def initialize_git():
    """Inicializa el repositorio Git"""
    if not Path('.git').exists():
        run_command('git init')
        print("✓ Repositorio Git inicializado")
    else:
        print("✓ Repositorio Git ya existe")


def main():
    """Función principal del script"""
    print("🚀 Configurando proyecto 'resenaya'...")
    print()
    
    # Verificar que estamos en el directorio correcto
    current_dir = Path.cwd().name
    if current_dir != 'resenaya':
        print("⚠️  Advertencia: No pareces estar en el directorio 'resenaya'")
        response = input("¿Continuar de todos modos? (y/n): ")
        if response.lower() != 'y':
            print("Configuración cancelada")
            return
    
    # Crear estructura
    create_directory_structure()
    print()
    
    # Crear archivos básicos
    create_basic_files()
    print()
    
    # Copiar configuraciones
    copy_config_files()
    print()
    
    # Inicializar Git
    initialize_git()
    print()
    
    # Comandos finales recomendados
    print("🎉 Configuración completada!")
    print()
    print("Próximos pasos recomendados:")
    print("1. git add .")
    print("2. git commit -m 'Configuración inicial del proyecto'")
    print("3. git remote add origin https://github.com/tu-usuario/resenaya.git")
    print("4. git push -u origin main")
    print("5. Abre el proyecto en VS Code")
    print()
    print("¡Ya puedes empezar a desarrollar con GitHub Copilot! 🤖")


if __name__ == "__main__":
    main()