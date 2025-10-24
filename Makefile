style:
	flake8 .
	isort .

types:
	mypy .

tests:
	pytest --ls --vv

check:
	make -j3 style types tests

migrate:
	python manage.py migrate --noinput

static:
	python manage.py collectstatic --noinput

run:
	python -m gunicorn --bind 0.0.0.0:8000 --workers 3 cleanhub.wsgi:application
