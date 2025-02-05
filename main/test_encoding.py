import pandas as pd

# Try reading with UTF-8
print("Reading with UTF-8:")
df1 = pd.read_csv('main/wordList 2024-10-07.csv', encoding='utf-8')
print(df1['French'].head())

# Save with UTF-8
df1.to_csv('main/wordList 2024-10-07.csv', index=False, encoding='utf-8')

# Read again to verify
print("\nAfter saving with UTF-8:")
df2 = pd.read_csv('main/wordList 2024-10-07.csv', encoding='utf-8')
print(df2['French'].head()) 