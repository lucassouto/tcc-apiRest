APP = app

install:
	pip install pipenv
	pipenv install
	pipenv install --dev --three

runserver:
	python manage.py runserver

test:
	python manage.py test $(APP)

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations $(APP)
