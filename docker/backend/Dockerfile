FROM python:slim

ENV DJANGO_SETTINGS_MODULE quiz.settings.production

# Install dependencies
RUN mkdir -p /app/quiz
COPY docker/backend/docker-entrypoint /app
COPY backend/.python-version backend/pyproject.toml backend/uv.lock /app
WORKDIR /app
RUN pip install uv && uv run sync

# Now copy code; allows docker to cache the installation of dependencies
COPY backend/quiz /app/quiz

RUN uv run /app/quiz/manage.py collectstatic --no-input
ENTRYPOINT ["/app/docker-entrypoint"]
