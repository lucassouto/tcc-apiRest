APP = app

runserver:
	python manage.py runserver

test:
	python manage.py test $(APP)

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations $(APP)
