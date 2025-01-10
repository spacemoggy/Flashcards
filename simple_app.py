from dash import Dash, html
app = Dash(__name__)

#create a global variable to pass to the callback
message = 'hello world'

app.layout = html.Div([
    html.Button('Click me: 0', id='counter-button')
])

from simple.button_callback import *

if __name__ == '__main__':
    app.run_server(debug=True)