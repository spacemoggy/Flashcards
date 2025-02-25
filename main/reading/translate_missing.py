import pandas as pd
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

def translate_text(text, target_language='en'):
    """Translate text to target language using Google Translate API"""
    # Load credentials explicitly
    credentials = service_account.Credentials.from_service_account_file(
        'main/credentials/flashcards-451921-0dac76c6c97b.json'  # Replace with your actual JSON filename
    )
    translate_client = translate.Client(credentials=credentials)
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def translate_missing_words():
    """Find and translate words missing English translations"""
    # Load lemmas file
    df = pd.read_csv('main/french_lemmas.csv')
    
    # Find rows missing translations
    missing_translations = df[df['english'].isna()]
    print(f"Found {len(missing_translations)} words needing translation")
    
    # Translate missing words
    for index, row in missing_translations.iterrows():
        french = row['french_formatted']
        try:
            english = translate_text(french)
            df.at[index, 'english'] = english
            print(f"Translated: {french} → {english}")
        except Exception as e:
            print(f"Error translating {french}: {e}")
    
    # Save updated file
    df.to_csv('main/french_lemmas.csv', index=False)
    print("Saved updated translations")

if __name__ == '__main__':
    translate_missing_words() 