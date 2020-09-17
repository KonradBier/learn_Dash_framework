import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown="""
Nagłowki

# H1
## H2
### H3
#### H4

Znaczniki tekstu:  
Kursywa: *tekst kursywą* lub _tekst kursywą_  
Pogrubienie: **tekst pogrubiony** lub __tekst pogrubiony__  
Kursywa i pogrubienie: **pogrubienie i _kursywa_**  

Lista uporządkowana:  
1. Python  
2. SQL  
3. Java  

Lista nieuporządkowana:
* Python
* SQL
* Java

Linkowanie:
[google.com](https://www.google.com)

Kod:  
Użyj `print('Hello Word')`

```
import numpy as np
x = np.random.randn(1000)
print(x)
```
```
SELECT surname FROM tb.table1
```
  
  
Table:  
  
|UserID |Rating |Age|  
|-------|-------|---|  
|001    |4.5    |23 |  
|002    |5      |45 |  
  
  
Cytowanie:  
> Python jest fajny  
  
  > Warning: This is a development server. Do not use app.run_server
 in production, use a production WSGI server like gunicorn instead.  
  
  
Linie horyzontalne:  
  
---
***  
  
"""

app.layout = html.Div([
    dcc.Markdown(markdown)
])

if __name__ == '__main__':
    app.run_server(debug=True)
