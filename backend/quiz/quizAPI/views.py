# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render
import logging
from . import models
from . import serializers

logger = logging.getLogger(__name__)


class LoggedAPI(APIView):
    def dispatch(self, request, *args, **kwargs):
        logger.info(f"➡️ Request: {request.method} {request.path} by {request.user}")

        if request.GET:
            logger.debug(f"Query params: {request.GET}")

        try:
            logger.debug(f"Request data: {request.data}")
        except Exception as e:
            logger.debug(f"Failed to log request.data: {e}")

        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Unhandled exception: {str(e)}")
            raise

        logger.info(f"⬅️ Response status: {response.status_code}")

        try:
            logger.debug(f"Response data: {getattr(response, 'data', 'No .data')}")
        except Exception as e:
            logger.debug(f"Failed to log response data: {e}")

        return response


##################
# Home and Tests #
##################
@api_view(["GET"])
def index(request):
    return render(request, "home.html")


@api_view(["GET"])
def health_check(request):
    return Response(
        {"status": "healthy", "message": "Service is up and running"}, status=status.HTTP_200_OK
    )


@api_view(["GET"])
def auth_status(request):
    if request.user.is_authenticated:
        return Response({"message": "Logged in"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Not Logged in"}, status=status.HTTP_403_FORBIDDEN)


########
# CARD #
########
# URL/api/card/
class CardView(LoggedAPI, generics.ListCreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    permission_classes = [permissions.IsAuthenticated]


# URL/api/card/<int>
class SingleCardView(LoggedAPI, generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
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


##############
# Categorize #
##############
# URL/api/cards/categorize
class CardsCategorizeView(generics.ListAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardCategorizeSerializer


# URL/api/cards/categorize/<int>
class SingleCardsCategorizeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        serializer = serializers.SingleCardCategorizeSerializer(data=request.data)

        def return_if_id_inexistant(card_id, quiz_ids):
            if not models.Card.objects.filter(id=card_id).exists():
                message = f"The CARD with an ID of {card_id} does not exist"
                logger.error(f"[QUIZ] {message}")
                return message
            for quiz_id in quiz_ids:
                if not models.QuizDetails.objects.filter(id=quiz_id).exists():
                    message = f"The QUIZ with an ID of {quiz_id} does not exist"
                    logger.error(f"[QUIZ] {message}")
                    return message
            return ""

        if serializer.is_valid():
            card_id = pk
            quizzes = request.data["quizzes"]
            query = models.Quiz.objects.filter(card_id=card_id)
            set_a = set([card.quiz_id for card in query])  # type: ignore[reportAttributeAccessIssue]
            set_b = set(quizzes)

            id_exists = return_if_id_inexistant(card_id, set_b)
            if len(id_exists) > 0:
                return Response({"message": id_exists}, status=status.HTTP_404_NOT_FOUND)

            # Items that were removed from the original set
            for i in set_a - set_b:
                logger.info(f"[QUIZ] Deleting quiz_id {i} for card_id {card_id}")
                tmp = models.Quiz.objects.get(card_id=card_id, quiz_id=i)
                tmp.delete()

            # Items that were added to the original set
            for i in set_b - set_a:
                try:
                    logger.info(f"[QUIZ] Adding QUIZ ({i}) for CARD ({card_id})")
                    quiz_details = models.QuizDetails.objects.get(id=i)
                    card = models.Card.objects.get(id=card_id)
                    models.Quiz.objects.create(card_id=card, quiz_id=quiz_details)
                except models.QuizDetails.DoesNotExist:
                    logger.error(f"[QUIZ] Adding QUIZ ({i}) for CARD ({card_id})")

            message = f"PUT request received. Card = {card_id}. Quizzes = {quizzes}."
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
