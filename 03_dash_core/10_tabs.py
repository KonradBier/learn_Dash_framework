import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H3('Hello world - porównanie'),

    dcc.Tabs(children=[
        dcc.Tab(
            label='Python',
            children=[
                dcc.Markdown(
                    """
                    ```
                    print('Hello world')
                    ```
                    """
                )
            ]
        ),
        dcc.Tab(
            label='Java',
            children=[
                dcc.Markdown(
                    """
                    ```
                    class HelloWorld {
                        public static void main(String[] args) {
                            System.out.print("Hello, World!");
                        }
                    }
                    ```
                    """
                )
            ]
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
