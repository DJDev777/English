from django.db import models
from django.contrib.auth.models import User
from quizzes.models import EnglishLevel


class ProfessionalDirection(models.Model):
    """Тематическое направление английского: Developer, Finance и т.д."""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        verbose_name='User Avatar', 
        default="user/avatar/avatar.jpg", 
        upload_to="user/avatar"
    )
    bio = models.TextField(blank=True)
    english_level = models.ForeignKey(
        EnglishLevel, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    @property
    def total_words(self):
        """Количество слов в Knowledge Base (логика добавится позже)"""
        from learning.models import Word  # пример
        return Word.objects.filter(user=self.user).count()