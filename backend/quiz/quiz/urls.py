"""
URL configuration for quiz project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from quizAPI.views import index, health_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("quizAPI.urls")),
    path("", index),
    path("health/", health_check),
    # https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints
    re_path(r"^auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.jwt")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
