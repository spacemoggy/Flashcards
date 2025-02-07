import pandas as pd
import random

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
    
    Args:
        df (pandas.DataFrame): Full flashcard dataset
        
    Returns:
        pandas.DataFrame: Selected subset of cards for study
    """
    # Create a copy to avoid modifying original
    df = df.copy()
    
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
        return pd.concat(selected_cards)
    else:
        return pd.DataFrame()  # Return empty DataFrame if no cards selected
