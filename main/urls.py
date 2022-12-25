from django.urls import path, include
from .views import *

urlpatterns = [
    path('course/', IndexPage.as_view(), name="index"),
    path('course/<str:name>/', Chapters.as_view(), name="chapter"),
    path('course/<str:name>/<str:slug_field>/', SummaryPage.as_view(), name="summary"),
    path('quiz/', QuizHomePage.as_view(), name="quiz"),
    path('quiz/<str:name>/', QuizListPage.as_view(), name="quiz_list"),
    path('start_quiz/<int:pk>/', StartQuiz.as_view(), name="start_quiz"),
    path('theory/<str:name>/', PracticeQuestionList.as_view(), name="practice_list"),
    path('theory/<str:name>/<str:slug_field>/', PracticeQuestionPage.as_view(), name="practice_page")
]