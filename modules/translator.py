# Translate text using Google Translate API
from deep_translator import GoogleTranslator

def translate_segment(text, language='en'):
    try:
        translated_segment = GoogleTranslator(source='auto', target=language).translate(text)
        return translated_segment
    except Exception as e:
        print(f"Error translating segment: {e}")
        return None

def translate(text, language, ignore=["\n", "_"]):
    for char in ignore:
        text = text.replace(char, " ." + char + ". ")
    print(text)

    translated_text = GoogleTranslator(source='auto', target=language).translate(text)
    print(translated_text)
    for char in ignore:
        translated_text = translated_text.replace(" ." + char + ". ", char)

    return translated_text

if __name__ == "__main__":
    translate("asldfkjasdflajksdf_asdlfjas;dlfkjasdf_a__as;ldfkjas;dlf\n\n", 'es')