from django.contrib import admin
from .models import Category, QuizWord, EnglishLevel
 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(QuizWord)
class QuizWordAdmin(admin.ModelAdmin):
    list_display = ('quiz_word', 'translation_ka', 'category', 'level')
    search_fields = ('quiz_word', 'translation_ka')


@admin.register(EnglishLevel)
class EnglishLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')