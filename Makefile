style:
	flake8 .
	isort .

types:
	mypy .

tests:
	pytest

check:
	make -j3 style types tests

migrate:
	python manage.py migrate --noinput

static:
	python manage.py collectstatic --noinput

run:
	python -m gunicorn --bind 0.0.0.0:8000 --workers 3 cleanhub.wsgi:application

install:
	python -m pip install --no-cache-dir uv==0.7.8 && \
    python -m uv export --frozen --no-hashes --no-dev -o requirements.txt && \
    python -m pip install --no-cache-dir -r requirements.txt && \
    python -m pip uninstall -y uv

install-all:
	python -m pip install --no-cache-dir uv==0.7.8 && \
    python -m uv export --frozen --no-hashes --all-groups -o requirements.txt && \
    python -m pip install --no-cache-dir -r requirements.txt && \
    python -m pip uninstall -y uv
