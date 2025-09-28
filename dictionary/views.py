import os
from django.shortcuts import render
from django.http import JsonResponse
from google.cloud import translate_v2 as translate
from django.views.decorators.csrf import csrf_exempt


# Path to your JSON credentials file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/irakl/Desktop/Projects/2025/Django/English/dictionary-463816-91a65c0fd582.json"

# Initialize the Google Translate client
translate_client = translate.Client()


def translate_word(request):
    translation = None
    word = request.GET.get('word')
    lang = request.GET.get('lang', 'ka')  # default to Georgian

    if word:
        try:
            result = translate_client.translate(word, target_language=lang)
            translation = result['translatedText']
        except Exception as e:
            translation = f"Error: {e}"

    return render(request, 'translate.html', {
        'word': word,
        'translation': translation,
        'lang': lang
    })


# @csrf_exempt
# def translate_word(request):
#     word = request.GET.get('word')
#     target = request.GET.get('lang')  # 'ru' for Russian, 'ka' for Georgian

#     if not word or not target:
#         return JsonResponse({'error': 'Missing word or lang parameters'}, status=400)

#     try:
#         result = translate_client.translate(word, target_language=target)
#         return JsonResponse({
#             'original': word,
#             'translated': result['translatedText'],
#             'language': target
#         }, json_dumps_params={'ensure_ascii': False})
#         # print(result)
#         # return result

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
    