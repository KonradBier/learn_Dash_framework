import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from datetime import  datetime as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.DatePickerSingle(
        date=dt(2012, 1, 1),
        display_format='DD-MM-YY'
    ),
    dcc.DatePickerRange(
        start_date=dt(2020, 9, 1),
        end_date=dt(2020, 10, 5)

    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
