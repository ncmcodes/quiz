from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from quizAPI.views import index, health_check, auth_status
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("api/", include("quizAPI.urls")),
    path("auth/", include("quizAUTH.urls")),
    path("auth/status/", auth_status),
    path("health/", health_check),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon/favicon.ico")),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
