from django.urls import path
from . import views

app_name = 'dictionary'


urlpatterns = [
    path('translate/', views.translate_word, name='translate_word'),
]