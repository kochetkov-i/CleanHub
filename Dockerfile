FROM python:3.11-slim

WORKDIR /app

# Install make
RUN apt-get update && \
    apt-get install -y --no-install-recommends make && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy dependency files
COPY Makefile uv.lock pyproject.toml /app/

# Install dependencies using uv
RUN python3 -m pip install --no-cache-dir uv==0.7.8 && \
    python3 -m uv export --frozen --no-hashes --no-dev -o requirements.txt && \
    python3 -m pip install --no-cache-dir -r requirements.txt && \
    python3 -m pip uninstall -y uv

# Copy application code
COPY cleanhub /app/

RUN make build

EXPOSE 8000

RUN python -m gunicorn --bind 0.0.0.0:8000 --workers 3 cleanhub.wsgi:application
