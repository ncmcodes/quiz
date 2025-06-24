# from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
import json
from . import models
from . import serializers


def index(request):
    return render(request, "home.html")


########
# CARD #
########
# Frontend is consuming
# URL/api/card/
class CardView(generics.ListCreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    # permission_classes = [permissions.IsAuthenticated]


# URL/api/card/<int>
class SingleCardView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    # permission_classes = [permissions.IsAuthenticated]


########
# QUIZ #
########
# URL/api/add/
class QuizAdd(generics.ListCreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["quiz"]
    # permission_classes = [permissions.IsAuthenticated]


# Frontend is consuming
# URL/api/quiz/
class QuizView(generics.ListAPIView):
    queryset = models.QuizDetails.objects.all().order_by("category")
    serializer_class = serializers.QuizViewSerializer


# Frontend is consuming
# URL/api/quiz/<int>
class SingleQuizView(generics.ListAPIView):
    serializer_class = serializers.QuizSerializer

    def get_queryset(self):  # type: ignore[reportIncompatibleMethodOverride]
        quiz_id = self.kwargs["quiz"]
        return models.Quiz.objects.filter(quiz=quiz_id)


##############
# Categorize #
##############
# URL/api/cards/categorize
class CardsCategorizeView(generics.ListAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardCategorizeSerializer


# TEST:
# http://127.0.0.1:8000/api/cards/categorize/2 → {"quizzes": "[1, 2, 3]"}
# HTTPie: http PUT 127.0.0.1:8000/api/cards/categorize/2 quizzes="[1, 2, 3]"


# URL/api/cards/categorize/<int>
class SingleCardsCategorizeView(APIView):
    def put(self, request, pk):
        serializer = serializers.SingleCardCategorizeSerializer(data=request.data)

        if serializer.is_valid():
            card_id = pk
            quizzes = json.loads(request.data["quizzes"])
            message = f"PUT request received. Card = {card_id}. Quizzes = {quizzes}."
            # 1. Remove all quizzes for the given card_id
            # 2. Iterate over quizzes and add them to models.Quiz
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
