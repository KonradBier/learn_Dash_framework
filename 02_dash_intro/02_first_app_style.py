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
            ),

    html.Div('Dash: A web application framework for Python',
             style={
                 'color': colors['text'],
                 'textAlign': 'center'
             }),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=[1,2,3],
                y=[150,180,220],
                marker_color= '#bf86bf',
                marker_line_color='#4f544e',
                marker_line_width= 5,
                name='lokalna'
            ),
            go.Bar(
                x=[1,2,3],
                y=[140,190,250],
                marker_color= '#30d992',
                marker_line_color='#4f544e',
                marker_line_width= 5,
                name='online'
            )],
            layout= go.Layout(
                title='Wizualizacja danych',
                plot_bgcolor=colors['background']
            )

        )
    )
], style={'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)