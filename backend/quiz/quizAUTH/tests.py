from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthTests(TestCase):
    fixtures = ["test_auth_data.json"]

    def setUp(self):
        self.client = Client()

    def test_login_success(self):
        url = reverse("token_obtain_pair")
        response = self.client.post(url, {"username": "admin", "password": "admin"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn(settings.SIMPLE_JWT["AUTH_COOKIE"], response.cookies)
        self.assertIn(settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"], response.cookies)

    def test_login_fail(self):
        url = reverse("token_obtain_pair")
        response = self.client.post(
            url, {"username": "admin", "password": "wrongpassword"}, format="json"
        )
        self.assertEqual(response.status_code, 401)

    def test_refresh(self):
        admin = User.objects.get(username="admin")
        self.client.force_login(admin)

        login_url = reverse("token_obtain_pair")
        login_response = self.client.post(
            login_url, {"username": "admin", "password": "admin"}, format="json"
        )
        self.assertEqual(login_response.status_code, 200)

        refresh_url = reverse("token_refresh")
        refresh_response = self.client.post(refresh_url, content_type="application/json")
        self.assertEqual(refresh_response.status_code, 200)
        self.assertIn(settings.SIMPLE_JWT["AUTH_COOKIE"], refresh_response.cookies)

    def test_logout(self):
        admin = User.objects.get(username="admin")
        self.client.force_login(admin)

        login_url = reverse("token_obtain_pair")
        login_response = self.client.post(
            login_url, {"username": "admin", "password": "admin"}, format="json"
        )
        self.assertEqual(login_response.status_code, 200)

        logout_url = reverse("logout")
        logout_response = self.client.post(logout_url)
        self.assertEqual(logout_response.status_code, 200)
        self.assertEqual(logout_response.cookies[settings.SIMPLE_JWT["AUTH_COOKIE"]].value, "")
        self.assertEqual(
            logout_response.cookies[settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"]].value,
            "",
        )
