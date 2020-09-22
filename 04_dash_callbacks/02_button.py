import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        dcc.Input(id='input-1', type='text', value=''),
    ]),
    html.Button(id='button-1', children='Submit', n_clicks=0),
    html.Div(id='div-1', children='Wprowadź tekst i naciśnij submit')
])

@app.callback(
    Output(component_id='div-1', component_property='children'),
    [Input(component_id='input-1', component_property='value'),
     Input(component_id='button-1', component_property='n_clicks')]
)
def update_output(val, n_clic):
    return f'Wprowadziłeś {val} i nacisnąłeś przycisk {n_clic} razy'

if __name__ == '__main__':
    app.run_server(debug=True)
