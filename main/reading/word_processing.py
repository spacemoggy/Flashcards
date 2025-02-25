import pandas as pd

def add_existing_translations(result):
    """Add English translations from existing word list"""
    wordlist = pd.read_csv('main/wordList 2024-10-07.csv')
    translations = dict(zip(wordlist['French'], wordlist['English']))
    result['english'] = result['french_formatted'].map(translations)
    
    # Show stats
    matched = result['english'].notna().sum()
    print(f"\nMatched {matched} words with existing translations")
    print(f"Missing translations for {len(result) - matched} words")
    return result

def find_unmatched_known_words(result):
    """Find words we know that didn't match in top 10,000"""
    wordlist = pd.read_csv('main/wordList 2024-10-07.csv')
    known_words = set(wordlist['French'])
    matched_words = set(result['french_formatted'])
    unmatched = known_words - matched_words
    print("\nKnown words not in top 10,000:")
    for word in unmatched:
        print(f"  {word}")

def process_lexique_data():
    """Process Lexique into top 10,000 frequency-ranked lemmas"""
    # Load Lexique
    lexique_df = pd.read_csv('main/Lexique383.tsv', sep='\t')
    
    # First sort by frequency to get most common usage of each word
    lexique_df = lexique_df.sort_values('freqlivres', ascending=False)
    
    # Group by lemma, keeping first (most frequent) POS and gender
    result = lexique_df[['lemme', 'cgram', 'genre', 'freqlivres']].groupby('lemme').first().reset_index()
    
    # Sum frequencies for each lemma
    lemma_totals = lexique_df.groupby('lemme')['freqlivres'].sum().reset_index()
    
    # Add total frequencies to result
    result = pd.merge(result, lemma_totals, on='lemme', suffixes=('_form', '_total'))
    
    # Sort by total lemma frequency
    result = result.sort_values('freqlivres_total', ascending=False)
    
    # Add gender column for nouns by looking up exact matches in original data
    noun_base_forms = lexique_df[
        (lexique_df['ortho'] == lexique_df['lemme']) & 
        (lexique_df['cgram'] == 'NOM')
    ]
    base_genders = noun_base_forms.set_index('lemme')['genre']
    result['gender'] = result[result['cgram'] == 'NOM']['lemme'].map(base_genders)
    
    # Fill in missing genders from overrides file
    try:
        overrides = pd.read_csv('main/gender_overrides.csv').set_index('lemme')['gender']
        result['gender'] = result['gender'].fillna(result['lemme'].map(overrides))
    except FileNotFoundError:
        print("Warning: gender_overrides.csv not found")
    
    # Check for any remaining missing genders in top 10,000
    nouns = result[result['cgram'] == 'NOM'].head(10000)
    missing_genders = nouns[nouns['gender'].isna()]
    if len(missing_genders) > 0:
        print("\nWarning: Missing genders for these nouns:")
        print(missing_genders[['lemme', 'freqlivres_total']].sort_values('freqlivres_total', ascending=False).to_string())
    
    # Add formatted French column
    def format_word(row):
        if row['cgram'] == 'NOM':
            article = 'le' if row['gender'] == 'm' else 'la'
            return f"{article} {row['lemme']}"
        else:
            return row['lemme']
    
    result['french_formatted'] = result.apply(format_word, axis=1)
    
    # Add English translations from existing word list
    result = add_existing_translations(result)
    
    # Find known words that didn't match
    find_unmatched_known_words(result)
    
    # Keep top 10,000 and only needed columns
    result = result.head(10000)[['lemme', 'cgram', 'gender', 'freqlivres_total', 'french_formatted', 'english']]
    
    # Save to file
    result.to_csv('main/french_lemmas.csv', index=False)
    print(f"Saved top {len(result)} lemmas to french_lemmas.csv")

if __name__ == '__main__':
    process_lexique_data()