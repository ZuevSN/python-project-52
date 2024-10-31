install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 task_manager

dev:
	python manage.py runserver

PORT ?= 8000
devstart:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

start:
	poetry run gunicorn task_manager.wsgi