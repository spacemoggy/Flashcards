import pandas as pd

# Read with cp1252 encoding
df = pd.read_csv('main/wordList 2024-10-07.csv', encoding='cp1252')

# Save back with same encoding
df.to_csv('main/wordList 2024-10-07.csv', index=False, encoding='cp1252') 