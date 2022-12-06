from typing import Any
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure_prices(app):
    db.init_app(app)
    app.db = db
    
"""
Armazena informações de preços, valores promocionais, coletas de preços 
e precificação dinamica realizada pelo airflow
Lista de Preços com os ids das tabelas

"""

class ListPrice(db.Model):
    idlista = db.Column(db.Integer, primary_key=True)
    idpromo = db.Column(db.Integer)
    dataupdate = db.Column(db.Datetime)
    unidadename = db.Column(db.Integer)
    percentoff = db.Column(db.Float)
    dataupdate = db.Column(db.Datetime)
    bitativo = db.Column(db.Boolean)


class Prices(db.Model):
    priceid = db.Column(db.Integer, primary_key=True)
    idlistprice = db.Column(db.Integer)
    sku  = db.Column(db.String(300))
    custo = name = db.Column(db.Float)
    price = name = db.Column(db.Float)
    idcollection = db.Column(db.Integer)
    dataupdate = db.Column(db.Datetime)


class GoogleShopping(db.Model):
    googleid = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(300))
    seller = db.Column(db.String(300))
    urlgoogle = db.Column(db.String(2000))
    ean = db.Column(db.String(20))
    urlanuncio = db.Column(db.String(2000))
    priceseller = db.Column(db.Float)
    dateupdate = db.Column(db.Datetime)
    myprice = db.Column(db.Float)
    diferenca = db.Column(db.Float)
    bitativo = db.Column(db.Boolean)

class Promocional(db.Model):
    promoid = db.Column(db.Integer, primary_key=True)
    idcollection = db.Column(db.integer)
    idcliente = db.Column(db.Integer)
    idsku = db.Column(db.Integer)
    idgoogle = db.Column(db.Integer)
    idcategory = db.Column(db.Integer)
    datade = db.Column(db.Datetime)
    dataate = db.Column(db.Datetime)
    percentof = db.Column(db.Datetime)
    valueoff = db.Column(db.Float)
    idbrand = db.Column(db.Integer)
    dataupdate = db.Column(db.Datetime)
    bitativo = db.Column(db.Boolean)
