import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#a9cfc7',
    'text': '#4f544e'
}

app.layout = html.Div([

    html.H2('Hello dash',
            style={'color': colors['text'],
                   'textAlign': 'center'}
            )

    html.Div('Dash: A web application framework for Python')
])

if __name__ == '__main__':
    app.run_server(debug=True)