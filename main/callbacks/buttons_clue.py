from dash import Input, Output, State, callback
import pandas as pd
import utils

@callback(
    Output('current-clue', 'children', allow_duplicate=True),
    Input('clue-button', 'n_clicks'),
    State('game-state', 'data'),
    prevent_initial_call=True
)
def show_clue(n_clicks, current_index):
    if n_clicks is None:
        return ""
        
    # Load word list
    df = utils.load_word_list('main/wordList 2024-10-07.csv')
    
    # Get current word's clue
    current_clue = df.iloc[current_index]['Clue']
    
    return current_clue
