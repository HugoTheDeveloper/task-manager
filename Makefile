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

