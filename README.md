# TADREEBI

Backend Django App of TADREEBI

You may find full app documantation on [Introductory Repo](https://github.com/Tadreebi/app)

Deployed App (Soon...)

## [Minor Fixes to Do](https://github.com/Tadreebi/be/projects/2)

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

## How to start development

- python manage.py runserver

## Adding New Module Instructions

Soon...

## Testing Steps

- Switch to dev branch with following CLI command

        git checkout dev
- Fetch latest version of dev branch

        git Fetch
- Delete SQLite3 database file.
- Do following CLI command

        python manage.py makemigrations
- Do following CLI command

        python manage.py migrate
- Do following CLI command

        python manage.py cretesuperuser
- Start by testing the CRUD of each endpoint of own models'...
  - Admin panel form
  - URL links
- If possible, it's recommended to test others' work as well.
- When an error found, branch out of dev to fix the error with following CLI command

        git checkout -b new_branch_name dev
- Remember to create a to-do card for the fix to be done, so no one try to do what you're doing n have double works.
- There is probably an error that will occur, which is resulted by not adding permissions to models' views, so you might wanna start with that fix.

## Technical Features

- Landing page of API documentation.
- Data CRUD through admin panel or API calls.

## Future Techincal Features to Add

Soon...

## Libraries Used
- Django
