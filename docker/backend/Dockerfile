FROM python:slim

ENV DJANGO_SETTINGS_MODULE=quiz.settings.production

# Install dependencies
WORKDIR /app
COPY backend/.python-version backend/pyproject.toml backend/uv.lock /app
RUN pip install uv && uv run sync

# Need curl for healthchecks
RUN apt update && apt install curl -y

# Now copy code; allows docker to cache the installation of dependencies
COPY docker/backend/docker-entrypoint /app
COPY backend/quiz /app/quiz

RUN uv run /app/quiz/manage.py collectstatic --no-input
ENTRYPOINT ["/app/docker-entrypoint"]
