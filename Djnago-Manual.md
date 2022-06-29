# How to build a Django App From Scratch


## Pre-reuiqrments

Soon...


## Steps

1. To initiate, run following CLI commands
    - poetry new [django-app]
    - cd [django-app]
    - poetry install
    - poetry shell
    - poetry add django django-filter djangorestframework Markdown
    - django-admin startproject [project]
    - cd [project]
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py startapp [app]
    - Add [app] to INSTALLED_APPS list in [project]/settings.py

2. Create your models
    - Add models construction in [app]/models.py
    - Register model in [app]/admin.py

3. Run following CLI commands
    - python manage.py makemigrations
    - python manage.py migrate

4. Do REST API configs
    - Add "rest_framework" to INSTALLED_APPS list in [project]/settings.py
    - Add default rest configs in tail of [project]/settings.py
            REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}
    - Create [app]/api/serializers.py & link models
    - Create [app]/api/viewset.py & link models & serializers
    - Create urls.py in [app] directory
    - Link created urls.py to [project]/urls.py
    - Add API URLs to [app]/urls.py

5. Add Permissions
    - Adjust REST_FRAMEWORK list of [project]/settings.py to...
            rest_framework.permissions.IsAuthenticated
    - Create [app]/api/permissions.py
    - Link created permissions to views of [app]/api/viewset.py
    - Build permission tests in [app]/tests.py
    - Run CLI command of "python manage.py test" to test permissions functionality

6. Build Docker initial files of "docker-compose.yml" & "Dockerfile" & "requirements.txt"

7. Replace SQLite3 with PG database
    - Build a Docker container for database
    - Run CLI command of "poetry add psycopg2-binary" to add PG package
    - Update DATABASES list in [project]/settings.py


## How to start

- python manage.py runserver

## How to test

- python manage.py test

## APIs

- "/" | Landing Page
- "/admin" | Admin Panel Page
