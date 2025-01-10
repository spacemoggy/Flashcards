from dash import Input, Output
from simple.simple_app import app, message

@app.callback(
    Output('counter-button', 'children'),
    Input('counter-button', 'n_clicks')
)
def update_button(n_clicks):
    if n_clicks is None:
        return 'Click me: 0'
    #return f'Click me: {n_clicks}'
    return message