from model import Arbre
from config import INTRO

import pandas as pd
import numpy as np
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
    # On a fait une simple aggregation pour manifester les hauteur maximales dans chaque libelle
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

def PiePlotAdresse():
    df = getProjectedData(["Adresse"])
    condition1 = df["Adresse"] == "JARDINS DES CHAMPS ELYSEES - SQUARE MARIGNY / 41 AVENUE GABRIEL"
    condition2 = df["Adresse"] == "PARC MONTSOURIS / 28 BOULEVARD JOURDAN"
    condition3 = df["Adresse"] == "ILE DE BERCY / LAC DAUMESNIL"
    condition4 = df["Adresse"] == "PARC DES BUTTES CHAUMONT"
    df["Adresse"] = np.where(condition1 | condition2 | condition3 | condition4, df["Adresse"], "others" ) 
    fig = xp.pie(df,
                 names="Adresse",
                 title="Répartition des arbres par quartier")
    pie_plot_adresse = dcc.Graph(figure=fig)
    return pie_plot_adresse

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
    html.H1(children="Dashboard d'arbres remarquables"),
    html.Div(children=[html.P(children= INTRO)]),
    ScatterPlot(),
    PiePlot(),
    BarPlot(),
    PiePlotAdresse(),
])

if __name__ == '__main__':
    app.run_server(debug=True)
