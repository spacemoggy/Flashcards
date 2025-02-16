import pandas as pd
import utils
from datetime import datetime
import os
import numpy as np

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
        new_duration = ((old_duration * 2) + latest_timing) / 3
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

def update_duration_distribution(full_df):
    """Update/create today's duration distribution record"""
    file_path = 'main/duration_distribution.csv'
    today = datetime.now().date()
    
    # Create buckets from 0 to 10 seconds in 0.1s increments
    # pd.cut works like this:
    # 1. Creates ranges: [0-0.1), [0.1-0.2), etc  (where [ means "include", ) means "exclude")
    # 2. Takes each Duration value and sees which range it falls into
    # 3. Counts how many values are in each range
    # Making end=10.1 ensures we include the value 10.0 in our last bucket
    buckets = pd.interval_range(start=0, end=10.1, freq=0.1)
    # Get distribution and sort by bucket order (not by frequency)
    distribution = pd.cut(full_df['Duration'], bins=buckets).value_counts().sort_index()
    
    # Create the record for today:
    # 1. Start with empty dictionary
    new_record = {}
    
    # 2. Add the date
    new_record['date'] = today
    
    # 3. Create a column for each 0.1s bucket and its count
    # zip pairs up items from two lists like a zipper:
    # If seconds = [0.0, 0.1, 0.2] and distribution = [5, 3, 7]
    # Then zip creates pairs: (0.0,5), (0.1,3), (0.2,7)
    for seconds, count in zip(np.arange(0, 10, 0.1), distribution):
        column_name = f'duration_{seconds:.1f}'  # Makes names like 'duration_0.1'
        new_record[column_name] = count
    
    # 4. Add total word count
    new_record['total_words'] = len(full_df)
    
    # 5. Convert record to DataFrame and save
    if os.path.exists(file_path):
        # Load existing records
        dist_df = pd.read_csv(file_path)
        # Remove today's record if it exists
        dist_df = dist_df[pd.to_datetime(dist_df['date']).dt.date != today]
        # Add new record
        dist_df = pd.concat([dist_df, pd.DataFrame([new_record])])
        dist_df.to_csv(file_path, index=False)
    else:
        # Create new file with just today's record
        pd.DataFrame([new_record]).to_csv(file_path, index=False) 