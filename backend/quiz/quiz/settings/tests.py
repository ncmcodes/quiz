from .base import *

SECRET_KEY = "SUPER_SECRET_KEY"
STATIC_URL = "/static/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

FIXTURE_DIRS = (
    "quiz/quizAUTH/fixtures/",
    "quiz/quizAPI/fixtures/",
)

SIMPLE_JWT.update(
    {
        "ROTATE_REFRESH_TOKENS": False,
        "SIGNING_KEY": SECRET_KEY,
        "AUTH_COOKIE_DOMAIN": None,
        "AUTH_COOKIE_SECURE": False,
        "AUTH_COOKIE_HTTP_ONLY": True,
        "AUTH_COOKIE_PATH": "/",
        "AUTH_COOKIE_SAMESITE": "Lax",
    }
)
