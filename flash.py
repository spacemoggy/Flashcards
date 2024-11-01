import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd 
import plotly.express as px 

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
                html.Div([
                    html.Label('English word'),
                    dcc.Input(id='prior-english', type='text', style={'width': '150px'}),
                ], style={'display': 'inline-block', 'padding': '10px'}),
                html.Div([
                    html.Label('French word'),
                    dcc.Input(id='prior-french', type='text', style={'width': '150px'}),
                ], style={'display': 'inline-block', 'padding': '10px'}),
                html.Div([
                    html.Label('Clue'),
                    dcc.Textarea(id='prior-clue', rows=3, style={'width': '300px'}),
                ], style={'display': 'inline-block', 'padding': '10px'}),
            ], style={'display': 'flex', 'flex-direction': 'row'}),
        ]),
    ], style={'padding': '10px'}),

    # Layout for Current flashcard
    html.Div([
        html.Div([
            html.Label('Current flashcard'),
            html.Div([
                html.Div([
                    html.Label('English word'),
                    dcc.Input(id='current-english', type='text', style={'width': '150px'}),
                ], style={'display': 'inline-block', 'padding': '10px'}),
                html.Div([
                    html.Label('French word'),
                    dcc.Input(id='current-french', type='text', style={'width': '150px'}),
                ], style={'display': 'inline-block', 'padding': '10px'}),
                html.Div([
                    html.Label('Clue'),
                    dcc.Textarea(id='current-clue', rows=3, style={'width': '300px'}),
                ], style={'display': 'inline-block', 'padding': '10px'}),
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

#import the csv file
df = pd.read_csv('wordList 2024-10-07.csv', encoding='latin1')
#print(df)

#################
### CALLBACKS ###
#################

#Next Button
@app.callback(
    [Output('current-english', 'value'),
     Output('prior-english'  , 'value'),
     Output('prior-french'  , 'value'),
     Output('prior-clue'  , 'value')],
    Input('next-button', 'n_clicks')
)
def update_output(n_clicks):
    # increment the nRowCounter variable to keep track of which flashcard we're on
    global nRowCounter
    nRowCounter += 1

    # Handle the initial state where n_clicks is None
    if n_clicks is None:
        return [''] * 4

    #set the current_row variable to be the dataframe row corresponding to the n_clicks (need to adjust for zero indexing)
    current_row = df.iloc[n_clicks - 1]

    #set the prior_row to be blanks if it's the first click
    if n_clicks == 1:
        prior_row = pd.Series(['']* len(df.columns), index=df.columns)
    #otherwise, set it to be the dataframe row prior to current row
    else:
        prior_row = df.iloc[n_clicks - 2]

    #english_word = current_row['English']
    return current_row['English'], prior_row['English'], prior_row['French'], prior_row['Clue']

#Clue Button
@app.callback(
    Output('current-clue', 'value'),
    Input('clue-button', 'n_clicks')
)
def update_clue(n_clicks):
    global nRowCounter

    # Handle the initial state where n_clicks is None
    if n_clicks is None:
        return ['None']

    #set the current_row variable to be the dataframe row corresponding to the n_rowCounter (need to adjust for zero indexing)
    current_row = df.iloc[nRowCounter - 1]
    print(current_row['Clue'])

    #return current_row['Clue']
    return('hello')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

#a test change for github
