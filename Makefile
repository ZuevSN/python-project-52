install:
	poetry install
	make static

test:
	python manage.py test

lint:
	poetry run flake8 task_manager

dev:
	python manage.py runserver

PORT ?= 8000
devstart:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

start:
	poetry run gunicorn task_manager.wsgi

static:
	python manage.py collectstatic

inter_ru:
	python manage.py makemessages -l ru

migr:
	python manage.py makemigrations
	python manage.py migrate