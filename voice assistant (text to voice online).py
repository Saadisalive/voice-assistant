import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
from deep_translator import GoogleTranslator

def speak(text, language="en"):
    try:
        
        tts = gTTS(text=text, lang=language)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_file = fp.name
        tts.save(temp_file)

        os.system(f"start {temp_file}")
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n Please speak in english...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Api Error; {e}")
    return ""

def translate_text(text, target_language='es'):
    translater = GoogleTranslator(source='en', target=target_language)
    translated_text = translater.translate(text)
    print(f"Translated text: {translated_text}")
    return translated_text

def display_language_options():
    print("\nChoose target language:")
    print("1. Urdu")
    print("2. Spanish")
    print("3. chinese")
    print("4. French")
    print("5. German")
    print("6. Italian")
    print("7. Russian")
    print("8. Japanese")
    print("9. Korean")
    print("10. Portuguese")
    print("11. Arabic")
    print("12. Dutch")
    print("13. Greek")
    print("14. Polish")
    print("15. Swedish")
    print("16. Turkish")
    print("17. philippines")
    print("18. Vietnamese")
    print("19. Indonesian")
    print("20. Thai")

    choice = input("Enter the number corresponding to your choice (1-20): ")

    language_dict = {
        '1': 'ur',
        '2': 'es',
        '3': 'zh-CN',
        '4': 'fr',
        '5': 'de',
        '6': 'it',
        '7': 'ru',
        '8': 'ja',
        '9': 'ko',
        '10': 'pt',
        '11': 'ar',
        '12': 'nl',
        '13': 'el',
        '14': 'pl',
        '15': 'sv',
        '16': 'tr',
        '17': 'tl',
        '18': 'vi',
        '19': 'id',
        '20': 'th'

    }
    return language_dict.get(choice, 'es')

def main():

    target_language = display_language_options()

    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(original_text, target_language)
        
        speak(translated_text, language=target_language)
        print("Finished speaking the translated text.")

if __name__ == "__main__":
    main()