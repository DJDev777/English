from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="words")
    word = models.CharField(max_length=100)
    translation = models.TextField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.word} - {self.translation}"


class Book(models.Model):
    LEVEL_CHOICES = [
        ("A1", "A1"), ("A2", "A2"),
        ("B1", "B1"), ("B2", "B2"),
        ("C1", "C1"), ("C2", "C2"),
    ]
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    image = models.ImageField('image', upload_to="book_cover/", blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} (Level - {self.level})"


class UserBookAudio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="audiobooks")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="audiobooks")
    audio_file = models.FileField(upload_to="audiobooks/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
