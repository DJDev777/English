from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.conf import settings
import os

from .models import Word, Book, UserBookAudio
from .utils import translate_with_gemini_structured, generate_tts_audio
from django.core.files import File
from django.urls import reverse

# HOME (optional: keep simple)
def home(request):
    return render(request, "learning/home.html")

@login_required
def book_list(request):
    books = Book.objects.all().order_by("title")
    return render(request, "learning/book_list.html", {"books": books})

# ---------- NEW: Add Word page ----------
@login_required
def word_add_page(request):
    # Just render the page with the form; HTMX handles translation + save
    return render(request, "learning/add_word.html")


@login_required
def translate_word_htmx(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")

    word = (request.POST.get("word") or "").strip()
    if not word:
        return HttpResponseBadRequest("Word is required")

    data = translate_with_gemini_structured(word)

    # Render just the modal body + footer as a partial
    return render(
        request,
        "learning/partials/translation_modal_body.html",
        {
            "word": word,
            "translation": data.get("translation", ""),
            "definition": data.get("definition", ""),
            "example": data.get("example", ""),
            "translated_example": data.get("translated example", "")
        },
    )


@login_required
def save_word_htmx(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")

    word = request.POST.get("word", "").strip()
    translation = request.POST.get("translation", "").strip()
    description = request.POST.get("example", "").strip()
    print("save_word_htmx")
    print('description - ', description)

    if not word or not translation:
        return HttpResponseBadRequest("Word and translation are required")

    Word.objects.create(
        user=request.user,
        word=word,
        translation=translation,   # ✅ clean translation only
        description=description,   # ✅ example (and maybe definition)
    )

    return render(request, "learning/partials/save_success.html", {"word": word})



# ---------- Existing pages still work ----------
@login_required
def knowledge_base(request):
    all_words = Word.objects.filter(user=request.user).order_by("-created_at")

    grouped = {}
    for w in all_words:
        grouped.setdefault(w.created_at, []).append(w)
    return render(request, "learning/knowledge_base.html", {"grouped": grouped})



import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Book, UserBookAudio

SENTENCE_SPLIT = re.compile(r'(?<=[.!?])\s+')
TOKEN_SPLIT = re.compile(r'(\w+|\s+|[^\w\s])', re.UNICODE)

@login_required
def reader(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_audio = UserBookAudio.objects.filter(user=request.user, book=book).first()

    raw_sentences = [s for s in SENTENCE_SPLIT.split(book.content.strip()) if s]
    sentences = []
    for s in raw_sentences:
        tokens = []
        for tk in TOKEN_SPLIT.findall(s):
            if not tk:
                continue
            if tk.isspace():
                tokens.append({"text": tk, "type": "space"})
            elif tk.isalnum():
                tokens.append({"text": tk, "type": "word"})
            else:
                tokens.append({"text": tk, "type": "punct"})
        sentences.append({"text": s, "tokens": tokens})

    return render(
        request,
        "learning/reader.html",
        {"book": book, "user_audio": user_audio, "sentences": sentences},
    )





@login_required
def generate_audio_for_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_audio = UserBookAudio.objects.filter(user=request.user, book=book).first()

    if user_audio:
        # Already exists → just redirect
        return HttpResponseRedirect(reverse("learning:reader", args=[book.id]))

    output_dir = os.path.join(settings.MEDIA_ROOT, "audiobooks")
    os.makedirs(output_dir, exist_ok=True)
    file_name = f"{request.user.username}_{book.id}.mp3"
    output_path = os.path.join(output_dir, file_name)

    # Generate audio with OpenAI
    generate_tts_audio(book.title, book.content, output_path)

    # Save model record
    with open(output_path, "rb") as f:
        user_book_audio = UserBookAudio.objects.create(
            user=request.user,
            book=book,
            audio_file=File(f, name=file_name)
        )

    return HttpResponseRedirect(reverse("learning:reader", args=[book.id]))
