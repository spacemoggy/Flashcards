import pandas as pd
import utils
from datetime import datetime
import os

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
    
    # Prepare DataFrame for saving with only original columns
    original_columns = ['English', 'French', 'Clue', 'Duration']  # Add any other original columns
    save_df = full_df[original_columns]
    
    # Save the filtered DataFrame
    save_df.to_csv('main/wordList 2024-10-07.csv', index=False, encoding='utf-8')

def update_result_log(df):
    """Update result log CSV with details of cards just studied"""
    file_path = 'main/learning_history.csv'
    
    # Prepare the data for this round
    history_data = []
    for index, row in df.iterrows():
        history_data.append({
            'timestamp': row['timestamp'],
            'english': row['English'],
            'french': row['French'],
            'clue': row['Clue'],
            'expected_duration': row['Duration'],
            'actual_duration': row['session_time'],
            'used_clue': row['used_clue'],
            'batch_size': len(df),
            'position_in_batch': index,
            'session_id': row['session_id']
        })
    
    history_df = pd.DataFrame(history_data)
    
    # Append to existing file or create new one
    if os.path.exists(file_path):
        history_df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        history_df.to_csv(file_path, index=False) 