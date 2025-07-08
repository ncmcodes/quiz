import os
from django.core.management.utils import get_random_secret_key
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.1.20", "quiz-front"]
SECRET_KEY = os.environ.get("DJANGO_SECRET", f"{get_random_secret_key()}")

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
STATIC_ROOT = "/app/quiz/static"

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

print("=================================")
print("====== PRODUCTION ===============")
print("=================================")
