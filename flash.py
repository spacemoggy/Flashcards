import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd 
import plotly.express as px 
import utils
import layout_utils

#declare a global variable to keep track of which row I'm on
nRowCounter = 0

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    # Layout for Prior flashcard
    html.Div([
        html.Div([
            html.Label('Prior flashcard'),
            html.Div([
                layout_utils.create_flashcard_display('English word', 'prior-english'),
                layout_utils.create_flashcard_display('French word', 'prior-french'),
                layout_utils.create_flashcard_display('Clue', 'prior-clue', display_style={'width': '300px', 'background-color': 'lightgrey'}, rows=3),
            ], style={'display': 'flex', 'flex-direction': 'row'}),
        ]),
    ], style={'padding': '10px'}),

    # Layout for Current flashcard
    html.Div([
        html.Div([
            html.Label('Current flashcard'),
            html.Div([
                layout_utils.create_flashcard_display('English word', 'current-english'),
                layout_utils.create_flashcard_display('French word', 'current-french'),
                layout_utils.create_flashcard_display('Clue', 'current-clue', display_style={'width': '300px', 'background-color': 'lightgrey'}, rows=3),
            ], style={'display': 'flex', 'flex-direction': 'row'}),
        ]),
    ], style={'padding': '10px'}),

    # Buttons section
    html.Div([
        html.Button('Next Flashcard', id='next-button'       , style={'background-color': 'mintcream'                   , 'width': '150px', 'height': '50px'}),
        html.Button('Clue'          , id='clue-button'       , style={'background-color': 'amber'                       , 'width': '150px', 'height': '50px'}),
        html.Button('Show answer'   , id='show-answer-button', style={'background-color': 'lightcoral'                  , 'width': '150px', 'height': '50px'}),
        html.Button('Prior is wrong', id='prior-wrong-button', style={'background-color': 'black'     , 'color': 'white', 'width': '150px', 'height': '50px'}),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'padding-top': '20px'})
])

# Load the CSV file
df = utils.load_word_list('wordList 2024-10-07.csv')

#################
### CALLBACKS ###
#################

# Next Button
@app.callback(
    [Output('current-english', 'children'),
     Output('current-clue'  , 'children'),
     Output('prior-english'  , 'children'),
     Output('prior-french'  , 'children'),
     Output('prior-clue'  , 'children')],
    Input('next-button', 'n_clicks')
)
def update_output(n_clicks):
    # increment the nRowCounter variable to keep track of which flashcard we're on
    global nRowCounter
    nRowCounter += 1

    # Handle the initial state where n_clicks is None
    if n_clicks is None:
        return [''] * 5

    #set the current_row variable to be the dataframe row corresponding to the n_clicks (need to adjust for zero indexing)
    current_row = df.iloc[nRowCounter - 1]

    #set the prior_row to be blanks if it's the first click
    if n_clicks == 1:
        prior_row = pd.Series(['']* len(df.columns), index=df.columns)
    #otherwise, set it to be the dataframe row prior to current row
    else:
        prior_row = df.iloc[nRowCounter - 2]

    print(f'nRowCounter in Next function is {nRowCounter}')
    return (current_row['English'],
    '', 
    prior_row['English'], 
    prior_row['French'], 
    prior_row['Clue'])

# Clue Button
@app.callback(
    Output('current-clue', 'children', allow_duplicate=True),
    Input('clue-button', 'n_clicks'),
    prevent_initial_call=True
)
def update_clue(n_clicks):
    global nRowCounter
    # Handle the initial state where n_clicks is None
    if n_clicks is None:
        return 'None'
    #set the current_row variable to be the dataframe row corresponding to the nRowCounter (need to adjust for zero indexing)
    current_row = df.iloc[nRowCounter-1]
    print(f'nRowCounter in Clue function is {nRowCounter}')
    print(current_row['Clue'])
    return current_row['Clue']

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)