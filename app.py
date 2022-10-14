from operator import ge
from model import Arbre
import pandas as pd
import plotly.express as xp
from dash import Dash, html, dcc



def getProjectedData(columns):
    dataContainer = {}
    for col in columns:
        dataContainer[col] = []
    query = Arbre.select().dicts()
    for row in query:
        for col in columns:
            dataContainer[col].append(row[col])
    return pd.DataFrame(data=dataContainer)


def ScatterPlot():
    df = getProjectedData(["Hauteur","Circonference","Domanialite"])
    fig = xp.scatter(df,
                     x="Hauteur",
                     y="Circonference",
                     color="Domanialite",
                     title= "Correlation entre Hauteur et circonference")
    scatter_plot = dcc.Graph(figure=fig)
    return scatter_plot
def PiePlot():
    df = getProjectedData(["Domanialite"])
    fig = xp.pie(df,
                 names= "Domanialite",
                 title= "Commbien de Domanialite sont-ils?")
    pie_plot = dcc.Graph(figure=fig)
    return pie_plot
app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Arbre Remarquables dashboard'),
    html.Div(children='''
        Dash: on a 2 figures graphiques
    '''),
    ScatterPlot(),
    PiePlot(),
])

if __name__ == '__main__':
    app.run_server(debug=True)
