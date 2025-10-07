from django.contrib import messages
from django.shortcuts import render
from .models import Category, QuizWord, EnglishLevel, UserQuizSession, UserQuizAnswer
from random import sample
from accounts.models import Profile

def category_list(request):
    all_category = Category.objects.all()
    return render(request, "quizzes/category_list.html", {"categories": all_category})


# def start_quiz_for_level(user, level):
#     # create session
#     session = UserQuizSession.objects.create(user=user, level=level)

#     # pick 1 random word per category (up to 10)
#     categories = list(Category.objects.all())[:10]
#     print('categories list', categories)
#     categories2 = Category.objects.all()[:10]
#     print('categories2', categories2)
#     for category in categories:
#         word = QuizWord.objects.filter(level=level, category=category).order_by('?').first()
#         if word:
#             UserQuizAnswer.objects.create(session=session, word=word)

#     return session


# def submit_answer(answer_id, user_input):
#     ans = UserQuizAnswer.objects.get(id=answer_id)
#     ans.user_answer = user_input
#     ans.is_correct = (ans.word.translation_ka.lower().strip() == user_input.lower().strip())
#     ans.save()


# def finish_quiz(session):
#     total = session.answers.count()
#     correct = session.answers.filter(is_correct=True).count()
#     session.score = correct
#     session.total_questions = total
#     session.completed = True
#     session.save()

#     if correct == total:
#         next_level = EnglishLevel.objects.filter(id__gt=session.level.id).first()
#         return {
#             "result": "passed",
#             "next_level": next_level.name if next_level else None
#         }
#     else:
#         wrong_answers = session.answers.filter(is_correct=False)
#         return {
#             "result": "failed",
#             "correct": correct,
#             "total": total,
#             "wrong_answers": [
#                 {"word": a.word.quiz_word, "correct": a.word.translation_ka, "user": a.user_answer}
#                 for a in wrong_answers
#             ]
#         }




from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import QuizWord, EnglishLevel, UserQuizSession, UserQuizAnswer
from random import sample

def start_quiz(request, level_id):
    level = get_object_or_404(EnglishLevel, pk=level_id)

    # Create or reuse unfinished session
    session, created = UserQuizSession.objects.get_or_create(
        user=request.user, level=level, completed=False
    )

    profile = getattr(request.user, "profile", None)
    if profile and profile.english_level and profile.english_level.id >= level.id:
        messages.info(request, f"You’ve already completed level {level.name}.")
        return redirect('quizzes:quiz_result', session_id=session.id)  # or home


    if not session.answers.exists():
        # Pick 10 words (1 per category)
        categories = list(set(QuizWord.objects.filter(level=level)
                              .values_list('category_id', flat=True)))[:10]
        for cat_id in categories:
            word = QuizWord.objects.filter(level=level, category_id=cat_id).order_by('?').first()
            if word:
                UserQuizAnswer.objects.create(session=session, word=word)

    # Redirect to first unanswered question
    next_question = session.answers.filter(user_answer="").first()
    return redirect('quizzes:quiz_question', answer_id=next_question.id)


def quiz_question(request, answer_id):
    answer = get_object_or_404(UserQuizAnswer, pk=answer_id, session__user=request.user)

    if request.method == 'POST':
        user_input = request.POST.get('user_answer', '').strip()
        answer.user_answer = user_input
        answer.is_correct = (answer.word.translation_ka.lower() == user_input.lower())
        answer.save()

        # Go to next question or finish
        session = answer.session
        next_q = session.answers.filter(user_answer="").first()
        if next_q:
            return redirect('quizzes:quiz_question', answer_id=next_q.id)
        else:
            return redirect('quizzes:quiz_result', session_id=session.id)

    total = answer.session.answers.count()
    answered = answer.session.answers.exclude(user_answer="").count()
    progress = int((answered / total) * 100) if total else 0

    return render(request, 'quizzes/quiz_question.html', {
        'answer': answer,
        'progress': progress,
        'question_number': answered + 1,
        'total': total,
    })




def quiz_result(request, session_id):
    session = get_object_or_404(UserQuizSession, pk=session_id, user=request.user)
    session.completed = True
    session.finished_at = timezone.now()
    session.score = session.answers.filter(is_correct=True).count()
    session.save()

    next_level = EnglishLevel.objects.filter(id__gt=session.level.id).first()

    # ✅ Update user profile level if passed all questions
    if session.score == session.total_questions:
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.english_level = session.level
        profile.save()

    return render(request, 'quizzes/quiz_result.html', {
        'session': session,
        'answers': session.answers.all(),
        'next_level': next_level,
    })




