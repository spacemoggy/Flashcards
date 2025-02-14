import pandas as pd
import random
from datetime import datetime
import os

# Time thresholds (in seconds)
TIME_GREEN = 1.5
TIME_YELLOW = 2.7
TIME_PURPLE = 5.0
DEFAULT_TIME = 10.0
TARGET_TIME = 60

# Category definitions
def get_category(time):
    if time < TIME_GREEN:
        return 'green'
    elif time < TIME_YELLOW:
        return 'yellow'
    elif time < TIME_PURPLE:
        return 'amber'
    else:
        return 'purple'

def select_study_cards_for_testing(df):
    """
    Temporary version for testing - just returns first 3 cards
    """
    # Create a copy to avoid modifying original
    df = df.copy()
    
    # Fill any missing durations
    df['Duration'] = df['Duration'].fillna(DEFAULT_TIME)
    
    # Just return first 3 cards
    return df.head(3)

def select_study_cards(df):
    """
    Select cards for study session based on time ratios.
    Avoids selecting cards already studied today.
    
    Args:
        df (pandas.DataFrame): Full flashcard dataset
        
    Returns:
        pandas.DataFrame: Selected subset of cards for study, with added columns:
            - used_clue: Tracks if clue was used
            - session_id: Unique ID for this study session
            - timestamp: When each card was completed
    """
    # Create a copy to avoid modifying original
    df = df.copy()
    
    # Filter out any words already studied today
    today = datetime.now().date()
    if os.path.exists('main/learning_history.csv'):
        history_df = pd.read_csv('main/learning_history.csv')
        
        # Process timestamps into dates:
        # 1. pd.to_datetime() converts timestamp strings to datetime objects
        # 2. .dt accessor lets us access datetime properties of a Series
        # 3. .date property gets just the date part of each datetime
        datetime_series = pd.to_datetime(history_df['timestamp'])  # Convert strings to datetime objects
        history_df['date'] = datetime_series.dt.date              # Extract just the date part
        
        # Get list of words studied today:
        # 1. Filter history to just today's entries
        todays_entries = history_df[history_df['date'] == today]
        # 2. Get the English words from those entries (no duplicates)
        todays_words = todays_entries['english'].unique()
        
        # Remove today's words from selection pool:
        # The isin operation works like this:
        # 1. df['English'] looks at the English column of our word list
        # 2. .isin(todays_words) checks each word: "Is this in today's list?"
        #    Returns True for words we've studied, False for words we haven't
        available_words = df[~df['English'].isin(todays_words)]
        df = available_words
    
    # Fill any missing durations
    df['Duration'] = df['Duration'].fillna(DEFAULT_TIME)
    
    # Split into categories
    categories = {
        'green': df[df['Duration'] < TIME_GREEN],
        'yellow': df[(df['Duration'] >= TIME_GREEN) & (df['Duration'] < TIME_YELLOW)],
        'amber': df[(df['Duration'] >= TIME_YELLOW) & (df['Duration'] < TIME_PURPLE)],
        'purple': df[df['Duration'] >= TIME_PURPLE]
    }
    
    # Define category sequence for selection
    category_order = ['green', 'yellow', 'yellow', 'amber', 'amber', 'amber', 
                     'purple', 'purple', 'purple', 'purple']
    
    selected_cards = []
    total_time = 0
    position = 0
    
    while total_time < TARGET_TIME:
        current_category = category_order[position]
        
        # Check if category has available cards
        if len(categories[current_category]) > 0:
            # Select random card from category
            card = categories[current_category].sample(n=1)
            
            # Update total time
            total_time += float(card['Duration'].iloc[0])
            
            if total_time > TARGET_TIME:
                break
                
            # Add card to selection and remove from category
            selected_cards.append(card)
            categories[current_category] = categories[current_category].drop(card.index)
        
        # Move to next position
        position = (position + 1) % len(category_order)
        
        # Check if we've tried all positions and no cards are available
        if position == 0:
            if all(len(cat_df) == 0 for cat_df in categories.values()):
                break
    
    # Combine all selected cards
    if selected_cards:
        study_df = pd.concat(selected_cards)
        
        # Initialize tracking columns
        study_df['used_clue'] = False
        study_df['session_id'] = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        study_df['timestamp'] = None
        
        return study_df
    else:
        return pd.DataFrame()  # Return empty DataFrame if no cards selected
