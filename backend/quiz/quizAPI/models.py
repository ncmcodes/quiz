from django.db import models

# ╔════╦══════════════════════════════════╗  ╔═════════════════════╗
# ║    ║           Quiz Details           ║  ║         Quiz        ║
# ╠════╬═══════════════╦══════════════════╣  ╠═══════════╦═════════╣
# ║ ID ║ Name          ║ Category         ║  ║ quiz      ║ card_id ║
# ╠════╬═══════════════╬══════════════════╣  ╠═══════════╬═════════╣
# ║ 1  ║ US Presidents ║ History          ║  ║ 1         ║ 1       ║  (card about US presidents, History)
# ╠════╬═══════════════╬══════════════════╣  ╠═══════════╬═════════╣
# ║ 2  ║ WWI           ║ History          ║  ║ 1         ║ 2       ║  (card about US presidents, History)
# ╠════╬═══════════════╬══════════════════╣  ╠═══════════╬═════════╣
# ║ 3  ║ OS            ║ Computer Science ║  ║ 3         ║ 3       ║  (card about OS, CS)
# ╠════╬═══════════════╬══════════════════╣  ╚═══════════╩═════════╝
# ║ 4  ║ Data Struct   ║ Computer Science ║
# ╠════╬═══════════════╬══════════════════╣
# ║ 5  ║ Algorithms    ║ Computer Science ║
# ╠════╬═══════════════╬══════════════════╣
# ║ 6  ║ Backend       ║ Programming      ║
# ╚════╩═══════════════╩══════════════════╝


class CardTypeChoices(models.TextChoices):
    FLASHCARD = "Flashcard"
    MATCHCARD = "Matchcard"


class Card(models.Model):
    front = models.CharField(max_length=500)
    back = models.CharField(max_length=5000)
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
    quiz = models.ForeignKey(QuizDetails, on_delete=models.PROTECT)
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Quizzes"
        unique_together = ("quiz", "card_id")

    def __str__(self):
        return f"{self.quiz} - {self.card_id}"
