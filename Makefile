MANAGE := poetry run python manage.py
HOST ?= 127.0.0.1
PORT ?= 8000

.PHONY: prod

dev:
	$(MANAGE) runserver

shell:
	$(MANAGE) shell

setup_migration:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

prod:
	poetry run gunicorn -b $(HOST):$(PORT) task_manager.wsgi:application

install:
	poetry install

build: install

lint:
	poetry run flake8 page_analyzer

selfcheck:
	poetry check

check: selfcheck lint

new_locales:
	django-admin makemessages -l ru --ignore=venv/* --ignore=static/* --ignore=/task_manager/labels/* --ignore=/task_manager/statuses/* --ignore=/task_manager/tasks/* --ignore=/task_manager/users/* --ignore=/task_manager/asgi.py --ignore=/task_manager/settings.py --ignore=/task_manager/urls.py --ignore=/task_manager/views.py --ignore=/task_manager/wsgi.py
