"""
URL configuration for quiz project.
"""

from django.contrib import admin
from django.urls import path, include
from quizAPI.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("quizAPI.urls")),
    path("", index),
]
