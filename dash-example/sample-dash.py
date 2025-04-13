from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('./gapminder_unfiltered.csv')

# define port number to be proxied here
proxyPort = 8057

# the url prefix for the proxy is added to the dash constructor
app = Dash(__name__, requests_pathname_prefix='/proxy/{}/'.format(proxyPort))

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == "__main__":
    # when you run the .py from terminal using `python app2.py`, it will not print the url correctly due the existence of the proxy, visit the url @ {jupyter-url}/proxy/{proxyPort}
    app.run(port=proxyPort, debug=True)
    
