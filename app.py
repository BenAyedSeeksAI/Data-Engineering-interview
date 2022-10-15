from operator import ge
from model import Arbre
import pandas as pd
import plotly.express as xp
from dash import Dash, html, dcc



def getProjectedData(columns):
    dataContainer = {}
    for col in columns:
        dataContainer[col] = []
    # retourne les rows de base de données comme des dictionnaire
    query = Arbre.select().dicts()
    for row in query:
        for col in columns:
            dataContainer[col].append(row[col])
    return pd.DataFrame(data=dataContainer)


def getHauteurMaximumParLibelle():
    data = getProjectedData(["Hauteur", "LibelleFrancais"])
    data = pd.DataFrame(data.groupby("LibelleFrancais",as_index=False).agg(
          MaximumHauteur = ("Hauteur","max")
    ))
    return data

def ScatterPlot():
    df = getProjectedData(["Hauteur","Circonference","LibelleFrancais"])
    fig = xp.scatter(df,
                     x="Hauteur",
                     y="Circonference",
                     color="LibelleFrancais",
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

def BarPlot():
    df = getHauteurMaximumParLibelle()
    fig = xp.bar(df,
                 x="LibelleFrancais",
                 y="MaximumHauteur",
                 title="Hauteur maximum par libelle")
    bar_plot = dcc.Graph(figure=fig)
    return bar_plot
app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Arbre Remarquables dashboard'),
    html.Div(children='''
        Dash: on a 2 figures graphiques
    '''),
    ScatterPlot(),
    PiePlot(),
    BarPlot(),
])

if __name__ == '__main__':
    app.run_server(debug=True)
