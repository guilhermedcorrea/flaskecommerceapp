from typing import Any
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db
    

class ListPrice(db.Model):
    idlista = db.Column(db.Integer, primary_key=True)
    idpromo = db.Column(db.Integer)
    dataupdate = db.Column()
    unidadename = db.Column()
    percentoff = db.Column()
    dataupdate = db.Column()
    bitativo = db.Column()


class Prices(db.Model):
    priceid = db.Column(db.Integer, primary_key=True)
    idlistprice = db.Column(db.Integer)
    sku  = db.Column()
    custo = name = db.Column()
    price = name = db.Column()
    idcollection = db.Column()



class GoogleShopping(db.Model):
    googleid = db.Column(db.Integer, primary_key=True)
    sku = db.Column()
    seller = db.Column()
    urlgoogle = db.Column()
    ean = db.Column()
    urlanuncio = db.Column()
    priceseller = db.Column()
    dateupdate = db.Column()
    myprice = db.Column()
    diferenca = db.Column()
    bitativo = db.Column()


class Promocional(db.Model):
    promoid = db.Column(db.Integer, primary_key=True)
    idcollection = db.Column()
    idcliente = db.Column()
    idsku = db.Column()
    idgoogle = db.Column()
    idcategory = db.Column()
    datade = db.Column()
    dataate = db.Column()
    percentof = db.Column()
    valueoff = db.Column()
    idbrand = db.Column()
    dataupdate = db.Column()
    bitativo = db.Column()
