from model import Arbre, db
from config import URLARBRES
import requests as req
import json


def SetupDB():
    print("setting up database ...")
    db.connect()
    db.create_tables([Arbre])
    db.close()
    

def downloadData():
    response = req.get(URLARBRES)
    if response.status_code == 200:
        print("content type : ",type(response.content))
        data = json.loads(response.content)
        print("data type :",type(data))
        return data["records"]
    return None
def seperateData(data):
    if data:
        result = []
        for row in data:
            result.append(row["fields"])
        return result
    return None

def loadData():
    def check(row):
        if "adresse" not in row.keys():
            row["adresse"] = "NON DISPONIBLE"
        if "arrondissement" not in row.keys():
            row["arrondissement"] = "NON DISPONIBLE"
        if "circonferenceencm" not in row.keys():
            row["circonferenceencm"] = -1.0
        if "complementadresse" not in row.keys():
            row["complementadresse"] = "NON DISPONIBLE"
        if "domanialite" not in row.keys():
            row["domanialite"] = "NON DISPONIBLE"
        if "espece" not in row.keys():
            row["espece"] = "NON DISPONIBLE"
        if "genre" not in row.keys():
            row["genre"] = "NON DISPONIBLE"
        if "geom_x_y" not in row.keys():
            row["geom_x_y"] = [-1.0,-1.0]
        if "hauteurenm" not in row.keys():
            row["hauteurenm"] = -1
        if "idbase" not in row.keys():
            row["idbase"] = -1
        if "idemplacement" not in row.keys():
            row["idemplacement"] = "NON DISPONIBLE"
        if "libellefrancais" not in row.keys():
            row["libellefrancais"] = "NON DISPONIBLE"
        if "pepiniere" not in row.keys():
            row["pepiniere"] = "NON DISPONIBLE"
        if "remarquable" not in row.keys():
            row["remarquable"] = None
        return row
            
    result = seperateData(downloadData())
    for row in result:
        row = check(row)
        Arbre.create(
            Adresse = row["adresse"],
            Arrondissement = row["arrondissement"],
            Circonference = row["circonferenceencm"],
            ComplementAdresse = row["complementadresse"],
            Domanialite = row["domanialite"],
            Espece = row["espece"],
            Genre = row["genre"],
            Hauteur = row["hauteurenm"],
            Idbase = row["idbase"],
            LibelleFrancais = row["libellefrancais"],
            GeometrieX = row["geom_x_y"][0],
            GeometrieY = row["geom_x_y"][1],
            Pepiniere = row["pepiniere"],
            Remarquable = (row["remarquable"] == "OUI"),
            TypeEmplacement = row["typeemplacement"]
        )
        print("Row created successfully ...")    

SetupDB()
loadData()
# pprint(result)