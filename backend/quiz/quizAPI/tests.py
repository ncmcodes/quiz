from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Card, Quiz


class CardViewTests(TestCase):
    fixtures = ["test_api_data.json", "test_auth_data.json"]

    def setUp(self):
        self.client.login(username="admin", password="admin")

    def test_get_cards(self):
        url = reverse("cards")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_card(self):
        url = reverse("cards")
        data = {"front": "New Card", "back": "New Card Back", "card_type": "Flashcard"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Card.objects.count(), 3)


class SingleCardViewTests(TestCase):
    fixtures = ["test_api_data.json", "test_auth_data.json"]

    def setUp(self):
        self.client.login(username="admin", password="admin")

    def test_get_single_card(self):
        url = reverse("card", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["front"], "Test Card 1")

    def test_update_single_card(self):
        url = reverse("card", kwargs={"pk": 1})
        data = {"front": "Updated Card", "back": "Updated Card Back", "card_type": "Flashcard"}
        response = self.client.put(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Card.objects.get(pk=1).front, "Updated Card")

    def test_delete_single_card(self):
        Quiz.objects.get(pk=1).delete()
        url = reverse("card", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Card.objects.count(), 1)


class QuizViewTests(TestCase):
    fixtures = ["test_api_data.json"]

    def test_get_quizzes(self):
        url = reverse("quiz-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class SingleQuizViewTests(TestCase):
    fixtures = ["test_api_data.json"]

    def test_get_single_quiz(self):
        url = reverse("quiz-single", kwargs={"quiz": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class CardsCategorizeViewTests(TestCase):
    fixtures = ["test_api_data.json"]

    def test_get_categorized_cards(self):
        url = reverse("cards-categorize")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class SingleCardsCategorizeViewTests(TestCase):
    fixtures = ["test_api_data.json", "test_auth_data.json"]

    def setUp(self):
        self.client.login(username="admin", password="admin")

    def test_categorize_card(self):
        url = reverse("cards-categorize-single", kwargs={"pk": 1})
        data = {"quizzes": [2]}
        response = self.client.put(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Quiz.objects.filter(card_id=1).count(), 1)
        self.assertEqual(Quiz.objects.get(card_id=1, quiz_id=2).quiz_id.id, 2)
