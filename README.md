# Blog Django

## Introducció

Aquest projecte és una aplicació web desenvolupada amb Django dins del mòdul de Programació.

L’aplicació consisteix en un blog on es poden visualitzar diferents publicacions, consultar informació dels autors i navegar entre etiquetes relacionades amb els posts.

L’objectiu principal del projecte ha estat practicar el funcionament bàsic de Django treballant amb:

- Models
- Vistes
- URLs
- Plantilles HTML
- Relacions entre taules
- Bootstrap i CSS

També s’ha treballat amb GitHub i documentació automàtica amb Pydoc.

---

# Documentació Pydoc

## Enllaç de la documentació

https://khaled22-del.github.io/Django/

## Mòduls documentats

- manage.py
- blog.models
- blog.views
- blog.urls
- blog.apps
- blog.admin

---

# Instal·lació ràpida

## Clonar el repositori

```bash
git clone https://github.com/khaled22-del/Django.git

Entrar a la carpeta del projecte
cd Django
Crear un entorn virtual
Windows
python -m venv venv
Linux o Mac
python3 -m venv venv
Activar l’entorn virtual
Windows
venv\Scripts\activate
Linux o Mac
source venv/bin/activate
Instal·lar dependències
pip install django
Executar migracions
python manage.py migrate
Execució del projecte

Per executar el servidor localment:

python manage.py runserver

Després es podrà accedir al projecte des del navegador amb la següent URL:

http://127.0.0.1:8000/
Estructura del projecte
Django/
│
├── blog/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── my_site/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── docs/
├── .github/
│   └── workflows/
│       └── docs.yml
│
├── generate_docs.py
├── manage.py
└── README.md
Funcionalitats principals
Creació i visualització de posts
Relació entre autors i publicacions
Sistema d’etiquetes
Panell d’administració de Django
Navegació entre pàgines
Documentació automàtica amb Pydoc
Publicació automàtica amb GitHub Pages
Tecnologies utilitzades
Python
Django
HTML
CSS
Bootstrap
GitHub Actions
GitHub Pages
Pydoc
Autor

Projecte desenvolupat per Khaled.
