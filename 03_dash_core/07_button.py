import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Button('Zapisz'),
    html.Button('Zapisz', disabled=True),
    html.Button('Zapisz', disabled=True, type='submit'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
