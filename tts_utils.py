from googletrans import Translator
from gtts import gTTS
import os


def translate_text_to_language(text, target_language='hi'):
    """
    Translates English text into the target language (default: Hindi).
    :param text: The input English text.
    :param target_language: Language code for translation (default: 'hi').
    :return: Translated text.
    """
    translator = Translator()
    result = translator.translate(text, dest=target_language)
    return result.text


def text_to_speech(text, language='hi'):
    """
    Translates the given English text into the specified language (default: Hindi) and speaks it.
    :param text: The input English text.
    :param language: Language code for translation and speech (default: 'hi').
    """
    # Translate the text
    translated_text = translate_text_to_language(text, target_language=language)
    print(f"Translated Text ({language}): {translated_text}")

    # Convert translated text to speech
    tts = gTTS(text=translated_text, lang=language, slow=False)
    filename = "translated_speech.mp3"
    tts.save(filename)

    # Play the MP3 file
    if os.name == 'nt':  # Windows
        os.system(f"start {filename}")
    else:
        os.system(f"afplay {filename} || mpg123 {filename}")
