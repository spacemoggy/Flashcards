import pandas as pd

def load_word_list(file_path):
    return pd.read_csv(file_path, encoding='utf-8')