import pandas as pd
import utils

def update_durations(study_df):
    """
    Update Duration values in CSV for cards that were just studied
    """
    # Load the full CSV using utils function
    full_df = utils.load_word_list('main/wordList 2024-10-07.csv')
    
    # Update durations for each card in our study set
    for index, row in study_df.iterrows():
        # Find matching row in full CSV (using English as key)
        mask = full_df['English'] == row['English']
        # Get the old duration and new timing data
        old_duration = full_df.loc[mask, 'Duration'].iloc[0]
        latest_timing = row['session_time']
        # Calculate new duration using the formula
        new_duration = ((old_duration * 5) + latest_timing) / 6
        full_df.loc[mask, 'Duration'] = new_duration
    
    # Save the updated full CSV
    full_df.to_csv('main/wordList 2024-10-07.csv', index=False) 