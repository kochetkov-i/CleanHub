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
RUN make install

# Copy application code
COPY . /app/

RUN ls -a
RUN ls ./cleanhub -a

RUN make migrate
RUN make static

EXPOSE 8000

RUN make run
