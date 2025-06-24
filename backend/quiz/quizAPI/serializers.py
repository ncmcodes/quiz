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
        return markdown.markdown(obj.back)


###########
# Quizzes #
###########
class QuizViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizDetails
        fields = ["id", "name", "category"]


# Frontend is consuming: api/quiz/${quiz_id}
class QuizSerializer(serializers.ModelSerializer):
    card_id_detail = CardSerializer(source="card_id", read_only=True)
    details = QuizViewSerializer(source="quiz", read_only=True)

    class Meta:
        model = models.Quiz
        fields = ["quiz", "card_id", "card_id_detail", "details"]


##############
# Categorize #
##############
class CardCategorizeSerializer(serializers.ModelSerializer):
    # card_front = serializers.CharField(source="card_id.front", read_only=True)
    quizzes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Card
        fields = ["id", "front", "quizzes"]

    def get_quizzes(self, obj):
        quizzes = models.Quiz.objects.filter(card_id=obj.id)
        return [
            {"quiz_id": quiz.quiz.id, "name": quiz.quiz.name}  # type: ignore[ReportAttributeAccessIssue]
            for quiz in quizzes
        ]


class SingleCardCategorizeSerializer(serializers.ModelSerializer):
    quizzes = serializers.CharField()

    class Meta:
        model = models.Quiz
        fields = ["quizzes"]
