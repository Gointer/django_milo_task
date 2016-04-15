APP_LIST ?= django_milo_task accounts

install:
	pip install -r requirements/dev.txt

ci: test
	@coverage report

run:
	python manage.py runserver

collectstatics:
	./manage.py collectstatic --noinput

test:
	@coverage run --source=. manage.py test -v2 $(APP_LIST)