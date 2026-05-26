"""
Script para generar documentación HTML automáticamente
utilizando Pydoc y Django.
"""

import os
import shutil
import django
import pydoc

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

# Crear carpeta docs
os.makedirs("docs", exist_ok=True)

# Lista de módulos
modules = [
    "manage",
    "blog.models",
    "blog.views",
    "blog.urls",
    "blog.apps",
    "blog.admin",
]

# CSS personalizado
custom_css = """
<style>

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 20px;
    color: #111827;
}

table {
    width: 100%;
    border-collapse: collapse;
    background-color: white;
}

td, th {
    padding: 10px;
    border: 1px solid #d1d5db;
}

.heading {
    background-color: #1f2937 !important;
    color: white !important;
}

a {
    color: #2563eb;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

</style>
"""

# Generar documentación
for module in modules:
    pydoc.writedoc(module)

# Modificar HTML y moverlos a docs
for file in os.listdir():
    if file.endswith(".html"):

        # Leer contenido
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # Insertar CSS antes de </head>
        content = content.replace("</head>", f"{custom_css}</head>")

        # Guardar cambios
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

        # Mover archivo a docs
        shutil.move(file, f"docs/{file}")

# Crear página principal personalizada
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write("""
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentación Django</title>

    <style>

        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #1f2937;
            color: white;
            padding: 30px;
            text-align: center;
        }

        .container {
            width: 80%;
            margin: auto;
            padding: 30px;
        }

        .card {
            background-color: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            border: 1px solid #d1d5db;
        }

        .card a {
            text-decoration: none;
            color: #111827;
            font-size: 20px;
            font-weight: bold;
        }

        .card:hover {
            background-color: #e5e7eb;
        }

        footer {
            text-align: center;
            padding: 20px;
            background-color: #1f2937;
            color: white;
            margin-top: 40px;
        }

    </style>

</head>

<body>

    <header>
        <h1>Documentación Django</h1>
        <p>Proyecto documentado automáticamente con Pydoc</p>
    </header>

    <div class="container">

        <div class="card">
            <a href="manage.html">manage.py</a>
        </div>

        <div class="card">
            <a href="blog.models.html">blog.models</a>
        </div>

        <div class="card">
            <a href="blog.views.html">blog.views</a>
        </div>

        <div class="card">
            <a href="blog.urls.html">blog.urls</a>
        </div>

        <div class="card">
            <a href="blog.apps.html">blog.apps</a>
        </div>

        <div class="card">
            <a href="blog.admin.html">blog.admin</a>
        </div>

    </div>

    <footer>
        Proyecto Django - Pydoc
    </footer>

</body>

</html>
""")

print("Documentación generada correctamente.")