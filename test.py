from google.cloud import translate_v2 as translate
import os

# Set path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/irakl/Desktop/Projects/2025/Django/English/dictionary-463816-91a65c0fd582.json"

# Create a client
translate_client = translate.Client()

# Word to translate
text = "hello"
target_language = "ru"  # use "ka" for Georgian

# Translate
result = translate_client.translate(text, target_language=target_language)

# Print result
print(f"Translated '{text}' to: {result['translatedText']}")
