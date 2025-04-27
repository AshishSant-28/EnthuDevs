#speech to text


import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()
translator = Translator()

def process_speech():
    with sr.Microphone() as source:
        print("Please speak now...")
        audio = recognizer.listen(source)
        
    try:
        # Detect original speech
        original_text = recognizer.recognize_google(audio)
        print(f"Original Text: {original_text}")

        # Translate to English if not English
        translated_text = translator.translate(original_text, dest='en').text
        print(f"Translated Text: {translated_text}")
        return translated_text

    except sr.UnknownValueError:
        print("Sorry, could not understand.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")