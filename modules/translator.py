from deep_translator import GoogleTranslator

def translate(text, language):
    try:
        return GoogleTranslator(source='auto', target=language).translate(text)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    translate("Hello World!", 'es')