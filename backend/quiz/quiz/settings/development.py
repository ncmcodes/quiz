from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
SECRET_KEY = "django-insecure-far#mq=j5)4m$wxtlmpj*j1#4=_sq)m0%m)#^y+wm%sr3imp(k"

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

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
