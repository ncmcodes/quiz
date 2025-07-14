from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
SECRET_KEY = "SUPER_SECRET_KEY"

# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "../db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static/"

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}] {levelname} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "quiz.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {  # "" catch root-level logs
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django": {  # More granular
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
        },
        "__main__": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

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

CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
CORS_ALLOWED_CREDENTIALS = True

print(f"====== DEV: Logs in {BASE_DIR / 'quiz.log'} ===============")
