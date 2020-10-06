import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    html.H3('MENU: '),
    html.Hr(),
    html.Div([
        dcc.Link('Wybierz technologię', href='/tech'),
        html.Br(),
        dcc.Link('Wyświetl logo', href='/logo'),
        html.Hr()
    ]),
    html.H6('Korzystasz z aplikacji w fazie dev')
])

tech_layout = html.Div([
    html.Div([
        html.H4('Wybierz technologię z podanych poniżej'),
        html.Hr(),
        dcc.Tabs(
            id='tech-1-tabs',
            children=[
                dcc.Tab(label='Python', value='tab-1'),
                dcc.Tab(label='SQL', value='tab-2'),
                dcc.Tab(label='Java', value='tab-3')
            ],
            value='tab-1'
        )
    ]),
    html.Div(id='tech-1-div'),
    html.Hr(),
    html.Div([
        dcc.Link('Wróć do menu', href='/')
    ])
])

logo_layout = html.Div([
    html.Div([
        html.H4('Wybierz technologię, aby wyświetlic logo')
    ]),
    html.Hr(),
    dcc.RadioItems(
        id='logo-1-radio',
        options=[{'label': i, 'value': i} for i in ['Python', 'SQL', 'Java']]
    ),
    html.Hr(),
    html.Div(id='logo-1-div'),
    html.Hr(),
    dcc.Link('Wróć do menu', href='/')
])


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/tech':
        return tech_layout
    elif pathname == '/logo':
        return logo_layout
    else:
        return index_page


@app.callback(
    Output('tech-1-div', 'children'),
    [Input('tech-1-tabs', 'value')]
)
def tech_1_tabs(value):
    if value == 'tab-1':
        return html.Div([
            dcc.Markdown(
                '''
                ```
                def fetch_financial_data(company='AMZN'):
                    """
                    This function fetches stock market quotations.
                    """
                    import pandas_datareader.data as web
                    return web.DataReader(name=company, data_source='stooq')
                ```
                '''
            )
        ])
    elif value == 'tab-2':
        return html.Div([
            dcc.Markdown('''
            ```sql
            CREATE TABLE Persons (
                PersonID int,
                LastName varchar(255),
                FirstName varchar(255),
                Address varchar(255),
                City varchar(255)
            );
            ```
            ''')
        ])
    elif value == 'tab-3':
        return html.Div([
            dcc.Markdown('''
            ```
             //declaration statement
            int number;
            //expression statement
            number = 4;
            //control flow statement
            if (number < 10 )
            {
              //expression statement
              System.out.println(number + " is less than ten");
            }
            ```
            ''')
        ])


img_py = 'D:/Users/biern/PycharmProjects/proj_01/07_case_studies/python.png'
img_sql = "D:/Users/biern/PycharmProjects/proj_01/07_case_studies/sql.jpg"
img_java: str = 'D:/Users/biern/PycharmProjects/proj_01/07_case_studies/java.jpg'
encoded_image_python = base64.b64encode(open(img_py, 'rb').read())
encoded_image_sql = base64.b64encode(open(img_sql, 'rb').read())
encoded_image_java = base64.b64encode(open(img_java, 'rb').read())


@app.callback(
    Output('logo-1-div', 'children'),
    [Input('logo-1-radio', 'value')]
)
def logo_1_radio(value):
    if value == 'Python':
        return html.Div([
            html.Img(src=f'data:image/jpg;base64,{encoded_image_python.decode()}',
                     style={'width': '300px'})
        ])
    elif value == 'SQL':
        return html.Div([
            html.Img(src=f'data:image/png;base64,{encoded_image_sql.decode()}',
                     style={'width': '300px'})
        ])
    elif value == 'Java':
        return html.Div([
            html.Img(src=f'data:image/jpg;base64,{encoded_image_java.decode()}',
                     style={'width': '300px'})
        ])
    else:
        return html.Div([
            html.H6('Wybierz opcję')
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
