MANAGE := poetry run python manage.py

.PHONY: prod shell

dev:
	$(MANAGE) runserver

shell:
	$(MANAGE) shell_plus --ipython

setup_migration:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

collect_static:
	$(MANAGE) collectstatic --no-input

prod:
	poetry run gunicorn task_manager.wsgi:application

install:
	poetry install

build: install collect_static migrate

lint:
	poetry run flake8 task_manager

selfcheck:
	poetry check

test:
	$(MANAGE) test

check: selfcheck lint test

new_locales:
	django-admin makemessages -l ru --ignore=venv/* --ignore=static/* --ignore=/task_manager/labels/* --ignore=/task_manager/statuses/* --ignore=/task_manager/tasks/* --ignore=/task_manager/users/* --ignore=/task_manager/asgi.py --ignore=/task_manager/settings.py --ignore=/task_manager/urls.py --ignore=/task_manager/views.py --ignore=/task_manager/wsgi.py

compile-locales:
	$(MANAGE) compilemessages

create_superuser:
	$(MANAGE) createsuperuser

test-coverage:
	poetry run coverage run --source='.' manage.py test task_manager
	poetry run coverage xml
	poetry run coverage report