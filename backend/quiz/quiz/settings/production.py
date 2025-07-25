import os
from .base import *
from datetime import timedelta

DEBUG = False
SECRET_KEY = os.environ.get("DJANGO_SECRET", "SET_A_SECRET_KEY_NOW")

# Docker uses 172.16.0.0/16
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "172.16.0.0/16"]
CORS_ALLOWED_ORIGINS = []
CORS_ALLOWED_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = []

ALLOWED_HOSTS_ENV = os.environ.get("ALLOWED_HOSTS", "")
if ALLOWED_HOSTS_ENV:
    ALLOWED_LIST = [x for x in ALLOWED_HOSTS_ENV.split(" ")]
    ALLOWED_HOSTS += ALLOWED_LIST
    CORS_ALLOWED_ORIGINS += [("https://" + x) for x in ALLOWED_LIST]
    CSRF_TRUSTED_ORIGINS = [("https://" + x) for x in ALLOWED_LIST]

# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/data/db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = os.environ.get("STATIC_URL", "static/")
STATIC_ROOT = "/data/static/"

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

SIMPLE_JWT.update(
    {
        "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
        "ROTATE_REFRESH_TOKENS": True,
        "SIGNING_KEY": SECRET_KEY,
        "AUTH_COOKIE_DOMAIN": None,
        "AUTH_COOKIE_SECURE": False,
        "AUTH_COOKIE_HTTP_ONLY": True,
        "AUTH_COOKIE_PATH": "/",
        "AUTH_COOKIE_SAMESITE": "Lax",
    }
)

print("=================================")
print("====== PRODUCTION ===============")
print("=================================")
print("[INFO] ALLOWED_HOSTS = ", ALLOWED_HOSTS)
print("[INFO] CSRF TRUSTED ORIGINS = ", CSRF_TRUSTED_ORIGINS)
print("[INFO] CORS ALLOWED ORIGINS = ", CORS_ALLOWED_ORIGINS)
