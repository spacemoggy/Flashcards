import dash
from dash import html
import dash_bootstrap_components as dbc
from layouts import home_layout

# Initialize simple Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Just display the layout we want to test
app.layout = home_layout.create_layout()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051) 