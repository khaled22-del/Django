"""
Script para generar documentación HTML automáticamente
utilizando Pydoc y Django.
"""

import os
import django
import pydoc

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

# Crear carpeta docs
os.makedirs("docs", exist_ok=True)

# Generar documentación
modules = [
    "manage",
    "blog.models",
    "blog.views",
    "blog.urls",
    "blog.apps",
    "blog.admin",
]

for module in modules:
    pydoc.writedoc(module)

# Mover index principal
if os.path.exists("manage.html"):
    os.rename("manage.html", "docs/index.html")

# Mover el resto de html a docs
for file in os.listdir():
    if file.endswith(".html") and file != "docs":
        os.rename(file, f"docs/{file}")

print("Documentació generada correctament.")