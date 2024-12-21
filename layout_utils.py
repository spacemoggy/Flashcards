from dash import html
from dash import dcc

def create_flashcard_input(label_text, input_id, input_type='text', input_style={'width': '150px'}, rows=3):
    if input_type == 'textarea':
        return html.Div([
            html.Label(label_text),
            dcc.Textarea(id=input_id, rows=rows, style=input_style),
        ], style={'display': 'inline-block', 'padding': '10px'})
    else:
        return html.Div([
            html.Label(label_text),
            dcc.Input(id=input_id, type=input_type, style=input_style),
        ], style={'display': 'inline-block', 'padding': '10px'})
    




def create_flashcard_display(label_text, display_id, display_style={'width': '150px', 'background-color':'lightgrey', 'min-height': '50px'}, rows=None):
    if rows:
        display_style = {**display_style, 'height': f'{rows * 20}px'}
    return html.Div([
        html.Label(label_text),
        html.Div(id=display_id, style=display_style),
    ], style={'display': 'inline-block', 'padding': '10px'})