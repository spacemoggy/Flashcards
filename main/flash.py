import os
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

print('flash.py starting')
import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd 
import plotly.express as px 
import utils as utils
import layouts.game_layout as game_layout
import callbacks.buttons_nextFlashcard as buttons_nextFlashcard
import callbacks.buttons_showAnswer as buttons_showAnswer
import callbacks.buttons_clue as buttons_clue
import dash_bootstrap_components as dbc
import card_selection  # Add this import at the top with other imports
import callbacks.debug_display as debug_display  # Add this import
import callbacks.histogram_display as histogram_display  # Make sure this is here
import data_updates.update_durations as update_durations  # Change from: callbacks.update_durations as update_durations
import callbacks.buttons_startNewRound as buttons_startNewRound  # Add this import
import layouts.home_layout as home_layout  # Keep this

# Load the CSV file
full_df = utils.load_word_list('main/wordList 2024-10-07.csv')
# Load initial study cards
study_df = card_selection.select_study_cards()
# study_df = card_selection.select_study_cards_for_testing(full_df)  # Testing version

# Initialize the Dash app
app = dash.Dash(__name__, 
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap'
    ]
)

# Add container layout with Location
app.layout = html.Div([
    dcc.Location(id='url'),                    # Tracks which screen we're on
    html.Div(id='current-screen')              # Will hold home or game layout
])

# Start with home layout
@callback(
    Output('current-screen', 'children'),
    Input('url', 'pathname')
)
def display_screen(pathname):
    if pathname == '/study':
        # Select new study cards each time we go to study screen
        study_df = card_selection.select_study_cards()
        return game_layout.create_layout(study_df)
    return home_layout.create_layout()

server = app.server

# Run the app
if __name__ == '__main__':
    debug_mode = os.environ.get('DASH_DEBUG', 'True') == 'True'
    app.run_server(debug=debug_mode)

