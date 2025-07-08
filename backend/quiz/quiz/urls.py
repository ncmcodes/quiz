"""
URL configuration for quiz project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from quizAPI.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("quizAPI.urls")),
    path("", index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
