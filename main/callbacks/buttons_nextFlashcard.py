from dash import Input, Output, State, callback
import pandas as pd
import time

@callback(
    # Outputs
    [Output('current-english', 'children'),
     Output('current-french', 'children'),
     Output('current-clue', 'children'),
     Output('prior-english', 'children'),
     Output('prior-french', 'children'),
     Output('prior-clue', 'children'),
     Output('prior-time', 'children'),
     Output('game-state', 'data'),
     Output('start-time', 'data')],
    Input('next-card-button', 'n_clicks'),
    [State('game-state', 'data'),
     State('word-data', 'data'),
     State('start-time', 'data')]
)
def next_flashcard(n_clicks, old_index, word_data, start_time):
    # Convert to DataFrame
    df = pd.DataFrame(word_data)
    
    # Set new start time for this card
    new_start_time = time.time()
    
    # Handle initial load
    if n_clicks is None:
        current_index = 0
        prior_english = ""
        prior_french = ""
        prior_clue = ""
        elapsed_time = ""
    else:
        current_index = (old_index + 1) % len(df)
        # Get prior word
        prior_english = df.iloc[old_index]['English']
        prior_french = df.iloc[old_index]['French']
        prior_clue = df.iloc[old_index]['Clue']
        # Calculate elapsed time
        elapsed_time = f"{time.time() - start_time:.1f}s" if start_time else ""
    
    # Get current word
    current_english = df.iloc[current_index]['English']
    current_french = ""  # Start empty, will be shown with Show Answer button
    
    # Check if clue exists and set indicator
    current_clue_populated = df.iloc[current_index]['Clue']
    current_clue = "*****" if pd.notna(current_clue_populated) and current_clue_populated.strip() else ""
    
    return [
        current_english,  # current-english
        current_french,   # current-french
        current_clue,     # current-clue
        prior_english,    # prior-english
        prior_french,     # prior-french
        prior_clue,      # prior-clue
        elapsed_time,     # prior-time
        current_index,    # game-state
        new_start_time   # start-time
    ]