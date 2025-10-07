from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    """
    Represents a thematic category of vocabulary
    (e.g., Food, Travel, Work, Education, etc.)
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["id"]

    def __str__(self):
        return self.name


class EnglishLevel(models.Model):
    name = models.CharField(verbose_name='Cefr Level sufix', max_length=3)
    description = models.CharField(verbose_name='Cefr Level text', max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} - {self.description}'
    
    

class QuizWord(models.Model):
    """
    Represents an English word linked to a category,
    with CEFR level and Georgian translation.
    """
    # CEFR_LEVELS = [
    #     ("A1", "A1 Beginner"),
    #     ("A2", "A2 Elementary"),
    #     ("B1", "B1 Intermediate"),
    #     ("B1+", "B1+ Pre-Upper Intermediate"),
    #     ("B2", "B2 Upper Intermediate"),
    #     ("B2+", "B2+ Advanced Candidate"),
    #     ("C1", "C1 Advanced"),
    #     ("C2", "C2 Proficient"),
    # ]

    quiz_word = models.CharField(max_length=100)
    translation_ka = models.CharField(max_length=200)  # Georgian translation
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="words"
    )
    level = models.ForeignKey(EnglishLevel, default=None, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
        ordering = ["level", "category__name", "quiz_word"]
        unique_together = ("quiz_word", "level", "category")

    def __str__(self):
        return f"{self.quiz_word} ({self.level.name})"




class UserQuizSession(models.Model):
    """Represents one testing session for a specific level."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quiz_sessions")
    level = models.ForeignKey("EnglishLevel", on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    score = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=10)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        return f"{self.user} - {self.level.name} ({self.score}/{self.total_questions})"


class UserQuizAnswer(models.Model):
    session = models.ForeignKey(UserQuizSession, on_delete=models.CASCADE, related_name="answers")
    word = models.ForeignKey(QuizWord, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    class Meta:
        unique_together = ("session", "word")

    def __str__(self):
        return f"{self.word.quiz_word} → {self.user_answer} ({'✅' if self.is_correct else '❌'})"
