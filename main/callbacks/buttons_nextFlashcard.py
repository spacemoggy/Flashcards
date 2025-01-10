from dash import Input, Output, State, callback
import pandas as pd
import utils

@callback(
    # Outputs
    [Output('current-english', 'children'),
     Output('current-french', 'children'),
     Output('current-clue', 'children'),
     Output('prior-english', 'children'),
     Output('prior-french', 'children'),
     Output('prior-clue', 'children'),
     Output('game-state', 'data')],
    
    # Inputs
    Input('next-card-button', 'n_clicks'),
    
    # State
    State('game-state', 'data')
)
def next_flashcard(n_clicks, current_index):
    # Load word list
    df = utils.load_word_list('main/wordList 2024-10-07.csv')
    
    # Get current word
    current_english = df.iloc[current_index]['English']
    current_french = ""  # Start empty, will be shown with Show Answer button
    current_clue = ""    # Start empty, will be shown with Clue button
    
    # Get prior word (if not first word)
    if current_index > 0:
        prior_english = df.iloc[current_index - 1]['English']
        prior_french = df.iloc[current_index - 1]['French']
        prior_clue = df.iloc[current_index - 1]['Clue']
    else:
        prior_english = ""
        prior_french = ""
        prior_clue = ""
    
    # Move to next word
    next_index = (current_index + 1) % len(df)
    
    return [
        current_english,  # current-english
        current_french,   # current-french
        current_clue,     # current-clue
        prior_english,    # prior-english
        prior_french,     # prior-french
        prior_clue,      # prior-clue
        next_index       # game-state
    ]