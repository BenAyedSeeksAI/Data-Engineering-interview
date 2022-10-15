from peewee import SqliteDatabase, Model, CharField, IntegerField, AutoField, FloatField, BooleanField

db = SqliteDatabase("database.db")
class Arbre(Model):
    Id = AutoField()
    Adresse = CharField()
    Arrondissement = CharField()
    Circonference = FloatField()
    ComplementAdresse = CharField()
    Domanialite = CharField()
    Espece = CharField()
    Genre = CharField()
    Hauteur = FloatField()
    Idbase = FloatField()
    LibelleFrancais = CharField()
    GeometrieX = FloatField()
    GeometrieY = FloatField()
    Pepiniere = CharField()
    Remarquable = BooleanField()
    TypeEmplacement = CharField()
    class Meta:
        database = db