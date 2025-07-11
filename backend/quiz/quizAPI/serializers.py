from django.contrib.auth.models import User
from rest_framework import serializers
import markdown  # type: ignore
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


#########
# Cards #
#########
class CardSerializer(serializers.ModelSerializer):
    front_html = serializers.SerializerMethodField()
    back_html = serializers.SerializerMethodField()

    class Meta:
        model = models.Card
        fields = ["id", "front", "back", "card_type", "front_html", "back_html"]

    def get_front_html(self, obj):
        return markdown.markdown(obj.front)

    def get_back_html(self, obj):
        return markdown.markdown(obj.back, extensions=["fenced_code", "codehilite"])


###########
# Quizzes #
###########
class QuizViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizDetails
        fields = ["id", "name", "category"]


class QuizSerializer(serializers.ModelSerializer):
    card_id_detail = CardSerializer(source="card_id", read_only=True)
    details = QuizViewSerializer(source="quiz_id", read_only=True)

    class Meta:
        model = models.Quiz
        fields = ["quiz_id", "card_id", "card_id_detail", "details"]


##############
# Categorize #
##############
class CardCategorizeSerializer(serializers.ModelSerializer):
    quizzes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Card
        fields = ["id", "front", "quizzes"]

    def get_quizzes(self, obj):
        quizzes = models.Quiz.objects.filter(card_id=obj.id)
        return [
            {"quiz_id": quiz.quiz_id.id, "name": quiz.quiz_id.name}  # type: ignore[ReportAttributeAccessIssue]
            for quiz in quizzes
        ]


class SingleCardCategorizeSerializer(serializers.ModelSerializer):
    quizzes = serializers.ListField()

    class Meta:
        model = models.Quiz
        fields = ["quizzes"]
