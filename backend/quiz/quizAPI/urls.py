from django.urls import path
from . import views

urlpatterns = [
    path("card/", views.CardView.as_view(), name="cards"),
    path(
        "card/<int:pk>",
        views.SingleCardView.as_view(),
        name="card",
    ),
    path("quiz/", views.QuizView.as_view(), name="quiz-list"),
    path("quiz/<int:quiz>", views.SingleQuizView.as_view(), name="quiz-single"),
    path("cards/categorize/", views.CardsCategorizeView.as_view(), name="cards-categorize"),
    path(
        "cards/categorize/<int:pk>",
        views.SingleCardsCategorizeView.as_view(),
        name="cards-categorize-single",
    ),
]
