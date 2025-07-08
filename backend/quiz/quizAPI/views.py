from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
import json
from . import models
from . import serializers


def index(request):
    return render(request, "home.html")


########
# CARD #
########
# URL/api/card/
class CardView(generics.ListCreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    permission_classes = [permissions.IsAuthenticated]


# URL/api/card/<int>
class SingleCardView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    permission_classes = [permissions.IsAuthenticated]


########
# QUIZ #
########
# View a list of all quizzes with their details (does not include flashcards)
class QuizView(generics.ListAPIView):
    queryset = models.QuizDetails.objects.all().order_by("category")
    serializer_class = serializers.QuizViewSerializer


# View a single quiz (includes flashcards)
class SingleQuizView(generics.ListAPIView):
    serializer_class = serializers.QuizSerializer

    def get_queryset(self):  # type: ignore[reportIncompatibleMethodOverride]
        quiz_id = self.kwargs["quiz"]
        return models.Quiz.objects.filter(quiz_id=quiz_id)


# # Frontend does NOT consume this API
# # URL/quiz/add
class QuizAdd(generics.ListCreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["quiz_id"]
    permission_classes = [permissions.IsAuthenticated]


##############
# Categorize #
##############
# URL/api/cards/categorize
class CardsCategorizeView(generics.ListAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardCategorizeSerializer


# URL/api/cards/categorize/<int>
class SingleCardsCategorizeView(APIView):
    def put(self, request, pk):
        serializer = serializers.SingleCardCategorizeSerializer(data=request.data)

        def return_if_id_inexistant(card_id, quiz_ids):
            if not models.Card.objects.filter(id=card_id).exists():
                message = f"Card ID {card_id} not found"
                print(f"[ERROR] {message}")
                return message
            for quiz_id in quiz_ids:
                if not models.Quiz.objects.filter(quiz_id=quiz_id).exists():
                    message = f"Quiz ID {quiz_id} not found"
                    print(f"[ERROR] {message}")
                    return message
            return ""

        if serializer.is_valid():
            card_id = pk
            quizzes = json.loads(request.data["quizzes"])
            query = models.Quiz.objects.filter(card_id=card_id)
            set_a = set([card.quiz_id for card in query])  # type: ignore[reportAttributeAccessIssue]
            set_b = set(quizzes)

            id_exists = return_if_id_inexistant(card_id, set_b)
            if len(id_exists) > 0:
                return Response({"message": id_exists}, status=status.HTTP_404_NOT_FOUND)

            # Items that were removed from the original set
            for i in set_a - set_b:
                print(f"[INFO] Deleting quiz_id {i} for card_id {card_id}")
                tmp = models.Quiz.objects.get(card_id=card_id, quiz_id=i)
                tmp.delete()

            # Items that were added to the original set
            for i in set_b - set_a:
                try:
                    print(f"[INFO] Adding QUIZ ({i}) for CARD ({card_id})")
                    quiz_details = models.QuizDetails.objects.get(id=i)
                    card = models.Card.objects.get(id=card_id)
                    models.Quiz.objects.create(card_id=card, quiz_id=quiz_details)
                except models.QuizDetails.DoesNotExist:
                    print(f"[ERROR] There is no QUIZ with an ID of {i}.")

            message = f"PUT request received. Card = {card_id}. Quizzes = {quizzes}."
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
