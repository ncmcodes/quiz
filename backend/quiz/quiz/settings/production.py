import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "10.0.0.0/8", "192.168.0.0/16", "localhost", "quizbackend"]
SECRET_KEY = os.environ.get("DJANGO_SECRET", "")

# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/data/db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
# TODO: Fix static files not being served
STATIC_URL = "static/"
STATIC_ROOT = "/app/quiz/static/"

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
#         "LOCATION": "127.0.0.1:11211",
#     }
# }

# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# https://docs.djangoproject.com/en/5.2/howto/logging/
# LOGS
if not os.path.isdir("/data/logs/"):
    os.makedirs("/data/logs")

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
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/data/logs/quiz.log",
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 5,  # 5MB
            "backupCount": 5,  # keep 5 old logs
        },
    },
    "loggers": {
        "": {  # "" catch root-level logs
            "handlers": ["file"],
            "level": "INFO",
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

print("=================================")
print("====== PRODUCTION ===============")
print("=================================")
