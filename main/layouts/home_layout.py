import dash_bootstrap_components as dbc
from dash import html, dcc
import callbacks_home.progress_chart  # Absolute import
import callbacks_home.learning_time   # Add this import

def create_layout():
    """Create the home/splash screen layout"""
    return html.Div([
        dbc.Container([
            # Top row with logo
            dbc.Row([
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
            ], className="mb-4"),
            
            # Main navigation/content area
            dbc.Row([
                dbc.Col([
                    dbc.Tabs([
                        dbc.Tab([
                            dbc.Button(
                                "Start Learning",
                                href="/study",
                                color="primary",
                                size="lg",
                                className="mt-4 mb-4"
                            ),
                            html.P("Continue your language journey...")
                        ], label="Study"),
                        
                        dbc.Tab([
                            html.H3("Learning Progress", className="mt-4"),
                            dcc.Graph(
                                id='progress-chart',
                                style={'height': '600px'}
                            ),
                            html.H3("Word Categories", className="mt-4"),
                            dcc.Graph(id='categories-chart')
                        ], label="Analysis"),
                        
                        dbc.Tab([
                            html.H3("Daily Learning Time", className="mt-4"),
                            dcc.Graph(
                                id='learning-time-chart',
                                style={'height': '600px'}
                            )
                        ], label="Learning Time"),
                        
                        dbc.Tab([
                            html.H3("Settings", className="mt-4"),
                            # We can add settings controls here later
                        ], label="Settings")
                    ])
                ])
            ])
        ])
    ],
    style={'background': 'linear-gradient(to bottom, #e0e0e0, #ffffff)', 
           'min-height': '100vh', 
           'font-family': 'Roboto, sans-serif'}) 