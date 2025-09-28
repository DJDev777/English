from django.urls import path
from . import views

app_name = 'learning'


urlpatterns = [
    path("", views.home, name="home"),

    # Books
    path("books/", views.book_list, name="book_list"),
    path("reader/<int:book_id>/", views.reader, name="reader"),
    path("books/<int:book_id>/generate-audio/", views.generate_audio_for_book, name="generate_audio_for_book"),

    # Words
    path("words/add/", views.word_add_page, name="word_add_page"),
    path("words/translate/", views.translate_word_htmx, name="translate_word_htmx"),
    path("words/save/", views.save_word_htmx, name="save_word_htmx"),

    path("knowledge-base/", views.knowledge_base, name="knowledge_base"),
]
