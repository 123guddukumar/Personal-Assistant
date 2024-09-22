from googletrans import Translator

class TranslationService:
    def __init__(self):
        self.translator = Translator()

    def translate_to_english(self, hindi_text):
        """Translate Hindi text to English."""
        translated = self.translator.translate(hindi_text, src='hi', dest='en')
        return translated.text

    def translate_to_hindi(self, english_text):
        """Translate English text to Hindi."""
        translated = self.translator.translate(english_text, src='en', dest='hi')
        return translated.text
