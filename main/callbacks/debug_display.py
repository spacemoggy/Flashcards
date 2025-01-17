from dash import callback, Output, Input, html
import pandas as pd

@callback(
    Output('debug-div', 'children'),
    Input('word-data', 'data')
)
def show_times(word_data):
    df = pd.DataFrame(word_data)
    if 'session_time' in df.columns:
        times = df[['English', 'session_time']].dropna(subset=['session_time'])
        return html.Pre(str(times))
    return "No times recorded yet" 