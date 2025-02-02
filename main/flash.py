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
import callbacks.update_durations as update_durations  # Add this import

# Load the CSV file
full_df = utils.load_word_list('main/wordList 2024-10-07.csv')
study_df = card_selection.select_study_cards(full_df)  # Normal version
# study_df = card_selection.select_study_cards_for_testing(full_df)  # Testing version

# Initialize the Dash app
app = dash.Dash(__name__, 
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap'
    ]
)

# Use the new layout with word data
app.layout = game_layout.create_layout(study_df)

server = app.server

# Run the app
if __name__ == '__main__':
    debug_mode = os.environ.get('DASH_DEBUG', 'True') == 'True'
    app.run_server(debug=debug_mode)

