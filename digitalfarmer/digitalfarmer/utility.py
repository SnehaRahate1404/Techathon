from .translations import translations

def get_translation(key, lang='en'):
    """
    Retrieve the translation for a given key and language.
    Defaults to English if the key or language is not found.
    """
    return translations.get(lang, translations['en']).get(key, key)
