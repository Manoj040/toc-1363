from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Ensure consistent results
DetectorFactory.seed = 0

# Language code to name mapping
language_names = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'zh-cn': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'ru': 'Russian',
    'hi': 'Hindi'
}

def identify_language(text):
    try:
        language_code = detect(text)
        return language_names.get(language_code, language_code)  # Return full name if available, otherwise code
    except LangDetectException as e:
        return f"Language detection error: {str(e)}"

# Get input from the user
text = input("Enter the text you want to identify the language of: ")
language = identify_language(text)
print(f"The language of the given text is: {language}")
