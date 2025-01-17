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
     Output('prior-time', 'style'),
     Output('game-state', 'data'),
     Output('start-time', 'data'),
     Output('word-data', 'data')],
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
        time_style = {"padding": "0.5rem"}
    else:
        current_index = (old_index + 1) % len(df)
        # Get prior word
        prior_english = df.iloc[old_index]['English']
        prior_french = df.iloc[old_index]['French']
        prior_clue = df.iloc[old_index]['Clue']
        
        # Calculate elapsed time (capped at 10 seconds)
        elapsed_seconds = min(time.time() - start_time, 10) if start_time else 0
        elapsed_time = f"{elapsed_seconds:.1f}s"
        
        # Store the time in DataFrame
        df.at[old_index, 'session_time'] = elapsed_seconds
        
        # Set color based on time
        if elapsed_seconds < 1.5:
            bg_color = "#90EE90"      # Light green
        elif elapsed_seconds < 2.7:
            bg_color = "#FFEB3B"      # Pure yellow
        elif elapsed_seconds < 5:
            bg_color = "#FF6200"      # Pure intense orange
        else:
            bg_color = "#DDA0DD"      # Plum
            
        time_style = {
            "padding": "0.5rem",
            "background-color": bg_color
        }
    
    # Get current word
    current_english = df.iloc[current_index]['English']
    current_french = ""  # Start empty, will be shown with Show Answer button
    
    # Check if clue exists and set indicator
    current_clue_populated = df.iloc[current_index]['Clue']
    current_clue = "*****" if isinstance(current_clue_populated, str) and current_clue_populated.strip() else ""
    
    return [
        current_english,    # current-english
        current_french,     # current-french
        current_clue,       # current-clue
        prior_english,      # prior-english
        prior_french,       # prior-french
        prior_clue,        # prior-clue
        elapsed_time,       # prior-time
        time_style,        # prior-time style
        current_index,      # game-state
        new_start_time,     # start-time
        df.to_dict('records')  # word-data
    ]