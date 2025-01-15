from dash import Input, Output, State, callback
import pandas as pd

@callback(
    Output('current-french', 'children', allow_duplicate=True),
    Input('show-answer-button', 'n_clicks'),
    [State('game-state', 'data'),
     State('word-data', 'data')],
    prevent_initial_call=True
)
def show_answer(n_clicks, current_index, word_data):
    if n_clicks is None:
        return ""
        
    # Convert to DataFrame
    df = pd.DataFrame(word_data)
    
    # Get current word's French translation
    current_french = df.iloc[current_index]['French']
    
    return current_french