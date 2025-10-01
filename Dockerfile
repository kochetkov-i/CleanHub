FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . .

RUN uv sync --locked

# Expose the application port
EXPOSE 8000

RUN chmod +x  /app/runserver.sh
CMD ["/app/runserver.sh"]
