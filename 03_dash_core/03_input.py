import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(
        type='text'
    ),
    dcc.Input(
        type='text',
        placeholder='Wprowadź text'
    ),
    dcc.Input(
        type='number',
        placeholder='Wprowadź liczbę'
    ),
    dcc.Input(
        type='password',
        placeholder='Wprowadź hasło'
    ),
    dcc.Input(
        type='email',
        placeholder='Wprowadź email'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
