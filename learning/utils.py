import os
import json
import google.generativeai as genai
from openai import OpenAI
from typing import Dict
from google import genai

from google.genai import types
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# OpenAI TTS setup
def generate_tts_audio(book_title: str, text: str, output_path: str):
    """
    Generate TTS audio from book text using OpenAI and save to output_path.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",  # "alloy", "verse", "ember", etc.
        input=text,
        instructions="Speak in a cheerful and positive tone.",
    ) as response:
        response.stream_to_file(Path(output_path))

    return output_path




def translate_with_gemini_structured(word: str) -> Dict[str, str]:
    client = genai.Client()

    resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
        {{
        "translation": "<translation of '{word}' in the user's native language [Georgian] if known, else a simple gloss in English>",
        "definition": "<a short Georgian definition of '{word}'>",
        "example": "<a short example sentence in English using '{word}'>",
        "translated example": "<translate example to georgian language>"
        }}
        """,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        thinking_config=types.ThinkingConfig(thinking_budget=0)  # Disable thinking
    ),
)
    raw = resp.text.strip()

    try:
        data = json.loads(raw)
        # minimal hardening
        return {
            "translation": data.get("translation", "").strip(),
            "definition": data.get("definition", "").strip(),
            "example": data.get("example", "").strip(),
            "translated example": data.get("translated example", "").strip()
        }
    except Exception:
        # Fallback: dump everything into translation field if parsing fails
        return {"translation": raw, "definition": "", "example": ""}
