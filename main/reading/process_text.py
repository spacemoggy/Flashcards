import pandas as pd
import re
import os

def load_lemmas():
    """Load our processed lemmas with translations"""
    return pd.read_csv('main/french_lemmas.csv')

def split_text_into_components(text):
    """Split text into words and other characters, preserving everything"""
    # Match either:
    # - Words (letters, including accented)
    # - Single characters (punctuation, spaces, etc)
    pattern = r'([a-zA-ZÀ-ÿ]+|.)'
    return re.findall(pattern, text)

def get_lemma(word, lemma_dict):
    """Get the lemma for a word using Lexique dictionary"""
    # Convert word to lowercase for matching
    word = word.lower()
    return lemma_dict.get(word, word)

def get_word_rank(lemma, lemmas_df):
    """Get the rank of a word in our top 10,000"""
    if lemma in lemmas_df.index:
        return lemmas_df.index.get_loc(lemma) + 1
    return None

def get_color(rank):
    """Get color based on word rank"""
    if rank is None:
        return 'black'
    elif rank <= 2500:
        return 'green'
    elif rank <= 5000:
        return 'blue'
    elif rank <= 7500:
        return 'orange'
    elif rank <= 10000:
        return 'red'
    else:
        return 'black'

def process_bible_text():
    """Process Matthew's Gospel and analyze vocabulary"""
    # Load our data
    lemmas_df = load_lemmas().set_index('lemme')
    lexique_df = pd.read_csv('main/Lexique383.tsv', sep='\t')
    
    # Create fast lookup dictionary for lemmas
    lemma_dict = dict(zip(lexique_df['ortho'], lexique_df['lemme']))
    
    print("Current working directory:", os.getcwd())
    
    # Read the text file
    try:
        with open('main/Texts/La Sainte Bible - Matthew.txt', 'r', encoding='utf-8') as f:
            text = f.read()
    except UnicodeDecodeError:
        with open('main/Texts/La Sainte Bible - Matthew.txt', 'r', encoding='latin-1') as f:
            text = f.read()
    
    # Split into components
    components = split_text_into_components(text)
    
    # Create DataFrame with explicit columns
    df = pd.DataFrame({
        'component': components,
        'is_word': [bool(re.match(r'\w+', comp)) for comp in components],
        'lemma': pd.NA,
        'rank': pd.NA,
        'color': 'black'
    })
    
    # Now apply lemmatization
    mask = df['is_word'].astype(bool)  # ensure boolean type
    df.loc[mask, 'lemma'] = df.loc[mask, 'component'].str.lower().apply(lambda x: get_lemma(x, lemma_dict))
    
    # Add rank and color
    df['rank'] = df['lemma'].apply(
        lambda x: get_word_rank(x, lemmas_df) if pd.notna(x) else None
    )
    df['color'] = df['rank'].apply(get_color)
    
    # Load translations
    translations_df = pd.read_csv('main/french_lemmas.csv')
    translations_dict = dict(zip(translations_df['lemme'], translations_df['english']))  # using column name
    
    # Add translations to our DataFrame
    df['translation'] = df['lemma'].map(translations_dict)
    
    # Print summary statistics
    print("\nText Analysis Summary:")
    print(f"Total components: {len(df)}")
    print(f"Total words: {df['is_word'].sum()}")
    print(f"Unique words: {df[df['is_word']]['lemma'].nunique()}")
    print("\nColor distribution:")
    print(df['color'].value_counts())
    
    print("\nFirst few components with analysis:")
    print(df.head(50))
    
    return df

if __name__ == '__main__':
    process_bible_text() 