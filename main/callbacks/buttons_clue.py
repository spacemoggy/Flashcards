from dash import Input, Output, State, callback
import pandas as pd

@callback(
    [Output('current-clue', 'children', allow_duplicate=True),
     Output('word-data', 'data', allow_duplicate=True)],
    Input('clue-button', 'n_clicks'),
    [State('game-state', 'data'),
     State('word-data', 'data')],
    prevent_initial_call=True
)
def show_clue(n_clicks, current_index, word_data):
    if n_clicks is None:
        return "", word_data
        
    # Convert to DataFrame
    df = pd.DataFrame(word_data)
    
    # Mark current card as having used clue
    df.at[current_index, 'used_clue'] = True
    
    # Get current word's clue
    current_clue = df.iloc[current_index]['Clue']
    
    return current_clue, df.to_dict('records')
