from deep_translator import GoogleTranslator

def translate_segment(text, language='en'):
    try:
        translated_segment = GoogleTranslator(source='auto', target=language).translate(text)
        return translated_segment
    except Exception as e:
        print(f"Error translating segment: {e}")
        return None

def translate(text, language):
    
    segments = text.split('\n')
    translated_segments = []
    for segment in segments:
        translated_segment = translate_segment(segment, language)
        if translated_segment:
            translated_segments.append(translated_segment)
    translated_text = '\n'.join(translated_segments)
    return translated_text

if __name__ == "__main__":
    translate("Hello World!", 'es')