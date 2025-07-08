from django.db import models


class CardTypeChoices(models.TextChoices):
    FLASHCARD = "Flashcard"
    MATCHCARD = "Matchcard"


class Card(models.Model):
    front = models.TextField(max_length=500)
    back = models.TextField(max_length=5000)
    card_type = models.CharField(max_length=15, choices=CardTypeChoices.choices)

    def __str__(self):
        return f"{self.front} [{self.card_type}]"


class QuizDetails(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Quiz Details"

    def __str__(self):
        return f"{self.name}"


class Quiz(models.Model):
    quiz_id = models.ForeignKey(QuizDetails, on_delete=models.PROTECT)
    card_id = models.ForeignKey(Card, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Quizzes"
        unique_together = ("quiz_id", "card_id")

    def __str__(self):
        return f"{self.quiz_id} - {self.card_id}"
