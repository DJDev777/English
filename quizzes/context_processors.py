from quizzes.models import EnglishLevel

def english_levels_context(request):
    return {'english_levels': EnglishLevel.objects.all()}
