from model import Arbre
import pandas as pd
import plotly.express as xp
from dash import Dash, html, dcc


def getData():
    dataContainer = []
    data = Arbre.select()
    for tree in data:
        result = [
            tree.Adresse,
            tree.Arrondissement,
            tree.Circonference,
            tree.ComplementAdresse,
            tree.Domanialite,
            tree.Espece,
            tree.Genre,
            tree.Hauteur,
            tree.Idbase,
            tree.LibelleFrancais,
            tree.GeometrieX,
            tree.GeometrieY,
            tree.Pepiniere,
            tree.Remarquable,
            tree.TypeEmplacement
        ]
        dataContainer.append(result)
    return dataContainer

def getDomanialite():
    dataContainer = {}
    dataContainer["Domanialite"] = []
    for tree in Arbre.select():
        dataContainer["Domanialite"].append(tree.Domanialite)
    return pd.DataFrame(data= dataContainer)

def getCirconferenceHauteurDomanialite():
    dataContainer = {}
    dataContainer["Circonference"] = []
    dataContainer["Hauteur"] = []
    dataContainer["Domanialite"] = []
    for tree in Arbre.select():
        dataContainer["Circonference"].append(tree.Circonference)
        dataContainer["Domanialite"].append(tree.Domanialite)
        dataContainer["Hauteur"].append(tree.Hauteur)
    return pd.DataFrame(data= dataContainer)
def ScatterPlot():
    df = getCirconferenceHauteurDomanialite()
    fig = xp.scatter(df,
                     x="Hauteur",
                     y="Circonference",
                     color="Domanialite",
                     title= "Correlation entre Hauteur et circonference")
    scatter_plot = dcc.Graph(figure=fig)
    return scatter_plot
def PiePlot():
    df = getDomanialite()
    fig = xp.pie(df,
                 names= "Domanialite",
                 title= "Commbien de Domanialite sont-ils?")
    pie_plot = dcc.Graph(figure=fig)
    return pie_plot
app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Arbre Remarquables dashboard'),
    html.Div(children='''
        Dash: on 2 figures graphiques
    '''),
    ScatterPlot(),
    PiePlot(),
])

if __name__ == '__main__':
    app.run_server(debug=True)