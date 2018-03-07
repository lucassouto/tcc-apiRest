install:
	pip install pipenv
	pipenv install
	pipenv install --dev

runserver:
	python manage.py runserver

test:
	python manage.py test

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations
