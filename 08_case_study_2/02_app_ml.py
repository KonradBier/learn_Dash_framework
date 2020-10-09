import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
import pickle

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('data_cleaned.csv', index_col=0)

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H3('Model Uczenia Maszynowego - Regresyjny Model Przewidywania Ceny Samochodów Używanych'),
        html.H6('Model Lasów Losowych (biblioteka scikit-learn)')
    ], style={'textAlign': 'center'}),
    html.Hr(),
    html.Div([
        html.Label('Podaj rok produkcji samochodu:'),
        dcc.Slider(
            id='slider-1',
            min=df.Year.min(),
            max=df.Year.max(),
            step=1,
            marks={i: str(i) for i in range(df.Year.min(), df.Year.max()+1)}
        ),
        html.Hr(),
        html.Label('Podaj rozmiar silnika:'),
        dcc.Slider(
            id='slider-2',
            min=0,
            max=6000,
            step=1,
            marks={i: str(i) for i in range(0, 6001, 500)},
            tooltip={'placement': 'bottom'}
        ),
        html.Hr(),
        html.Label('Podaj moc samochodu:'),
        dcc.Slider(
            id='slider-3',
            min=0,
            max=580,
            step=1,
            marks={i: str(i) for i in range(0, 581, 50)},
            tooltip={'placement': 'bottom'}
        )], style={'width': '80%', 'textAlign': 'left', 'margin': '0 auto', 'fontSize': 22})
])

if __name__ == '__main__':
    app.run_server(debug=True)
