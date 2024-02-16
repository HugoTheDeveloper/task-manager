dev:
	python3 manage.py runserver

install:
	poetry install

init_postgres:
	psql -a -d $(DATABASE_URL) -f database.sql

build: install init_postgres

lint:
	poetry run flake8 page_analyzer

selfcheck:
	poetry check

check: selfcheck lint

new_locales:
	django-admin makemessages -l ru --ignore=venv/* --ignore=static/* --ignore=/task_manager/labels/* --ignore=/task_manager/statuses/* --ignore=/task_manager/tasks/* --ignore=/task_manager/users/* --ignore=/task_manager/asgi.py --ignore=/task_manager/settings.py --ignore=/task_manager/urls.py --ignore=/task_manager/views.py --ignore=/task_manager/wsgi.py
