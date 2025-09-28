from django.contrib import admin
from .models import Word, Book, UserBookAudio

admin.site.register(Word)
admin.site.register(UserBookAudio)

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'level')