from dash import Input, Output, State, callback, no_update
import pandas as pd
import utils
import card_selection
from datetime import datetime

@callback(
    [Output('word-data',        'data',     allow_duplicate=True),
     Output('game-state',       'data',     allow_duplicate=True),
     Output('completion-div',   'style',    allow_duplicate=True),
     Output('current-english',  'children', allow_duplicate=True),
     Output('current-french',   'children', allow_duplicate=True),
     Output('current-clue',     'children', allow_duplicate=True)],
    Input('start-new-round-button', 'n_clicks'),
    State('completion-div', 'style'),
    prevent_initial_call=True
)
def start_new_round(n_clicks, completion_style):
    # Load and select new cards
    new_df = card_selection.select_study_cards()
    
    # Initialize tracking columns
    new_df['used_clue'] = False
    new_df['session_id'] = datetime.now().strftime('%Y-%m-%d-%H%M%S')
    
    # Hide completion overlay
    completion_style["display"] = "none"
    
    # Reset game state and show first card
    return [
        new_df.to_dict('records'),  # word-data
        0,                          # game-state
        completion_style,           # completion-div style
        new_df.iloc[0]['English'],  # current-english
        "",                         # current-french (hidden initially)
        "*****" if isinstance(new_df.iloc[0]['Clue'], str) and new_df.iloc[0]['Clue'].strip() else ""  # current-clue
    ] 