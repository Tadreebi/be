# TADREEBI

Backend Django App of TADREEBI

You may find full app documantation on [Introductory Repo](https://github.com/Tadreebi/app)

## Pre Development Steps

- Complete the setup process of pg database
- Split given feature into tasks n populate tasks of github [Project Mgmt Page](https://github.com/Tadreebi/be/projects/1)

## Development Instructions & Notes

- Clone repo to local machine
- Do the first-time setup steps of...

        poetry install

        poetry shell
        
        python manage.py migrate
        
        python manage.py createsuperuser
- To make a new branch for each task of the to-do list
- Branch is to be made out of the dev branch using the command
        git checkout -b branch_name dev

## Django API App Building Steps

1. Run following CLI commands
    - poetry new [tadreebi]
    - cd [tadreebi]
    - poetry install
    - poetry shell
    - poetry add django django-filter djangorestframework Markdown
    - django-admin startproject [tadreebi]
    - cd [tadreebi]
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py startapp [app]
    - Add [app] to INSTALLED_APPS list in [tadreebi]/settings.py

2. Create your models
    - Add models construction in [app]/models.py
    - Register model in [app]/admin.py

3. Run following CLI commands
    - python manage.py makemigrations
    - python manage.py migrate

4. Do REST API configs
    - Add "rest_framework" to INSTALLED_APPS list in [tadreebi]/settings.py
    - Add default rest configs in tail of [tadreebi]/settings.py
            REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"]}
    - Create [app]/api/serializers.py & link models
    - Create [app]/api/viewset.py & link models & serializers
    - Create urls.py in [app] directory
    - Add API URLs to [app]/urls.py
    - Link created urls.py to [tadreebi]/urls.py

5. Add Permissions
    - Adjust REST_FRAMEWORK list of [tadreebi]/settings.py to...
            rest_framework.permissions.IsAuthenticated
    - Create [app]/api/permissions.py
    - Link created permissions to views of [app]/api/viewset.py
    - Build permission tests in [app]/tests.py
    - Run CLI command of "python manage.py test" to test permissions functionality

6. Build Docker initial files of "docker-compose.yml" & "Dockerfile" & "requirements.txt"

7. Replace SQLite3 with PG database
    - Build a Docker container for database
    - Run CLI command of "poetry add psycopg2-binary" to add PG package
    - Update DATABASES list in [tadreebi]/settings.py
