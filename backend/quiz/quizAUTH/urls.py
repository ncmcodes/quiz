from django.urls import path
from . import views

urlpatterns = [
    path("token/", views.CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", views.CookieTokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
