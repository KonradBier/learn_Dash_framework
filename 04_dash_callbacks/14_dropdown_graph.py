import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Dropdown(
        id='drop-1',
        options=[
            {'label': 'Polska', 'value': 'PL'},
            {'label': 'Niemcy', 'value': 'GER'}
        ],
        value='PL'
    ),

    dcc.Graph(
        id='graph-1'
    )
])


@app.callback(
    Output('graph-1', 'figure'),
    [Input('drop-1', 'value')]
)
def update_graph(value):
    print(value)


if __name__ == '__main__':
    app.run_server(debug=True)
