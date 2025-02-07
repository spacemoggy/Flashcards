import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

def create_layout(df):
    return html.Div(
        [  # List of children starts here
            # Store component for state management
            dcc.Store(id='game-state', data=0),
            dcc.Store(id='word-data', data=df.to_dict('records')),
            dcc.Store(id='start-time', data=None),
            
            html.Div(style={'height': '2rem'}),  # Spacer div
            dbc.Container([
                # Logo and histogram row
                dbc.Row([
                    # Logo column
                    dbc.Col(
                        html.Img(
                            src='assets/Logo 2025-01-03.png', 
                            style={
                                'height': '80px',
                                'border-radius': '15px',
                                'border': '2px solid #0d6efd'
                            }
                        ), 
                        width=3
                    ),
                    # Histogram column
                    dbc.Col(
                        dcc.Graph(
                            id='time-histogram',
                            config={'displayModeBar': False},
                            style={'height': '80px'}
                        ),
                        width=9
                    )
                ], className="mb-4 align-items-center"),
                
                # Headers row
                dbc.Row([
                    dbc.Col(width=2, style={"padding-right": "0px", "margin-right": "-30px"}),
                    dbc.Col(html.H4("English word", style={"text-align": "center"}), width=3),
                    dbc.Col(html.H4("French word" , style={"text-align": "center"}), width=3),
                    dbc.Col(html.H4("Clue"        , style={"text-align": "center"}), width=4)
                ]),
                
                # Prior flashcard row
                dbc.Row([
                    dbc.Col([
                        html.H5("Prior flashcard"),
                        dbc.Card(dbc.CardBody(id="prior-time", style={"padding": "0.5rem"}), 
                                style={"min-height": "40px", "width": "70%"})
                    ], width=2, style={"padding-right": "0px", "margin-right": "-30px"}),
                    dbc.Col(dbc.Card(dbc.CardBody(id="prior-english"), style={"min-height": "120px"}), width=3),
                    dbc.Col(dbc.Card(dbc.CardBody(id="prior-french"),  style={"min-height": "120px"}), width=3),
                    dbc.Col(dbc.Card(dbc.CardBody(id="prior-clue"),    style={"min-height": "120px"}), width=4)
                ], className="align-items-center mb-3"),
                
                # Current flashcard section with overlay
                html.Div([  # Container for positioning
                    # Current flashcard row
                    dbc.Row([
                        dbc.Col([
                            html.H5("Current flashcard"),
                            dbc.Card(dbc.CardBody(id="current-time", style={"padding": "0.5rem"}), 
                                    style={"min-height": "40px", "width": "70%"})
                        ], width=2, style={"padding-right": "0px", "margin-right": "-30px"}),
                        dbc.Col(dbc.Card(dbc.CardBody(id="current-english"), style={"min-height": "120px"}), width=3),
                        dbc.Col(dbc.Card(dbc.CardBody(id="current-french"),  style={"min-height": "120px"}), width=3),
                        dbc.Col(dbc.Card(dbc.CardBody(id="current-clue"),    style={"min-height": "120px"}), width=4)
                    ], className="align-items-center mb-4"),
                    
                    # Completion overlay
                    html.Div([
                        html.H3("Round Complete!", className="text-center mb-3"),
                        html.P("Cards reviewed this round", className="text-center"),
                        dbc.Button(
                            "Start New Round", 
                            id="start-new-round-button", 
                            color="primary",
                            className="d-block mx-auto"
                        )
                    ], 
                    id="completion-div",
                    style={
                        "display": "none",
                        "position": "absolute",
                        "top": "0",
                        "left": "0",
                        "width": "100%",
                        "height": "100%",
                        "background": "linear-gradient(135deg, #e0f7fa 0%, #80deea 100%)",  # Soft aqua gradient
                        "border-radius": "0.5rem",
                        "padding": "2rem",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.1)"
                    })
                ], style={"position": "relative"}),  # Enable absolute positioning of overlay
                
                # spacer div
                html.Div(style={'height': '2rem'}),

                # Buttons row
                dbc.Row([
                    dbc.Col([
                        dbc.Button("Next Flashcard", id="next-card-button"  , color="primary"  , className="me-2"),
                        dbc.Button("Clue"          , id="clue-button"       , color="secondary", className="me-2"),
                        dbc.Button("Show answer"   , id="show-answer-button", color="secondary", className="me-2")
                    ], width=12, className="text-center")
                ]),

                # Debug div
                html.Div(id='debug-div', style={'margin-top': '20px'})
            ])
        ],
        style={'background': 'linear-gradient(to bottom, #e0e0e0, #ffffff)', 'min-height': '100vh', 'font-family': 'Roboto, sans-serif'}
    )


# For standalone testing
if __name__ == '__main__':
    app = dash.Dash(__name__, external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap'
    ])
    app.layout = create_layout()
    app.run_server(debug=True)
