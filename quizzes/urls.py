from django.urls import path
from . import views

app_name = "quizzes"

urlpatterns = [
    path('start/<int:level_id>/', views.start_quiz, name='start_quiz'),
    path('question/<int:answer_id>/', views.quiz_question, name='quiz_question'),
    path('result/<int:session_id>/', views.quiz_result, name='quiz_result'),
    # path('levels/', views.english_levels_context, name='english_levels_context')
    
]
