install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 page_analyzer

dev:
	python manage.py runserver

start:
	gunicorn task_manager:application