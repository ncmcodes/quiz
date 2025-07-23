from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from quizAPI.views import index, health_check, auth_status

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("api/", include("quizAPI.urls")),
    path("auth/", include("quizAUTH.urls")),
    path("auth/status/", auth_status),
    path("health/", health_check),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
