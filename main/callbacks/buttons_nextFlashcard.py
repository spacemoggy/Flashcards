from dash import Input, Output, State, callback
import pandas as pd
import time
from datetime import datetime
import data_updates.update_durations as update_durations
import utils

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
     Output('word-data', 'data'),
     Output('completion-div', 'style')],
    Input('next-card-button', 'n_clicks'),
    [State('game-state', 'data'),
     State('word-data', 'data'),
     State('start-time', 'data'),
     State('completion-div', 'style')]
)
def next_flashcard(n_clicks, old_index, word_data, start_time, completion_style):
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
        
        # Show first card on initial load
        current_row = df.iloc[current_index]
        current_english = current_row['English']
        current_french = ""  # Start empty, will be shown with Show Answer button
        # Check if clue exists and set indicator
        clue_value = current_row['Clue']  # Get the raw clue value
        clue_text = clue_value.strip() if isinstance(clue_value, str) else ""  # Strip if it's a string, else empty
        clue_is_string = isinstance(clue_value, str)  # Is it a string type?
        
        if clue_text and clue_is_string:  # Checks first if anything is populated in clue, then if what's populated is a string
            current_clue = "*****"
        else:
            current_clue = ""  # Show asterisks only if there's actual clue text

            
    else:
        current_index = (old_index + 1) % len(df)
        # Get prior word
        prior_english = df.iloc[old_index]['English']
        prior_french = df.iloc[old_index]['French']
        prior_clue = df.iloc[old_index]['Clue']
        
        # Calculate elapsed time (capped at 10 seconds)
        elapsed_seconds = min(time.time() - start_time, 10) if start_time else 0
        elapsed_time = f"{elapsed_seconds:.1f}s"
        
        # Store the time and timestamp in DataFrame
        df.at[old_index, 'session_time'] = elapsed_seconds
        df.at[old_index, 'timestamp'] = datetime.now().isoformat()
        
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
        
        # If we've reached the end (current_index = 0) but not on initial load (n_clicks not None)
        # This distinguishes between:
        # 1. Starting the app (current_index = 0, n_clicks = None)
        # 2. Completing a round (current_index = 0, n_clicks has value)
        # When round is complete:
        # - Update the durations in the CSV file
        # - Save learning history for this round
        # - Record today's duration distribution
        # - Show the completion overlay
        if current_index == 0 and n_clicks is not None:
            # First update the durations in the CSV file
            update_durations.update_durations(df)
            update_durations.update_result_log(df)
            
            # Then load the updated CSV for distribution calculation
            full_df = utils.load_word_list('main/wordList 2024-10-07.csv')
            update_durations.update_duration_distribution(full_df)
            
            completion_style["display"] = "block"
    
    # Get current word (only if not at end of round)
    if current_index == 0 and n_clicks is not None:  # Only clear if it's end of round
        current_english = ""
        current_french = ""
        current_clue = ""
    else:
        current_row = df.iloc[current_index]
        current_english = current_row['English']
        current_french = ""  # Start empty, will be shown with Show Answer button
        # Check if clue exists and set indicator
        clue_value = current_row['Clue']  # Get the raw clue value
        clue_text = clue_value.strip() if isinstance(clue_value, str) else ""  # Strip if it's a string, else empty
        clue_is_string = isinstance(clue_value, str)  # Is it a string type?
        
        if clue_text and clue_is_string:  # Checks first if anything is populated in clue, then if what's populated is a string
            current_clue = "*****"
        else:
            current_clue = ""  # Show asterisks only if there's actual clue text
    
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
        df.to_dict('records'),  # word-data
        completion_style    # completion-div style
    ]