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

# Mover archivos HTML a docs
for file in os.listdir():
    if file.endswith(".html"):
        os.rename(file, f"docs/{file}")

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

        h1 {
            margin: 0;
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
            color: #1f2937;
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