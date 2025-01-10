from dash import Input, Output, State, callback
import pandas as pd
import utils

@callback(
    Output('current-french', 'children', allow_duplicate=True),
    Input('show-answer-button', 'n_clicks'),
    State('game-state', 'data'),
    prevent_initial_call=True
)
def show_answer(n_clicks, current_index):
    if n_clicks is None:
        return ""
        
    # Load word list
    df = utils.load_word_list('main/wordList 2024-10-07.csv')
    
    # Get current word's French translation
    current_french = df.iloc[current_index]['French']
    
    return current_french