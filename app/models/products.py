from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure_product(app):
    db.init_app(app)
    app.db = db

"""
Armazena informações de produtos e coletas de atributos realizada pelo airflow

"""
class Atributos(db.Model):
    atributoid = db.Column(db.Integer, primary_key=True)
    idproduto = db.Column(db.Integer)
    especificacoes = db.Column(db.String)
    idimagem = db.Column(db.Integer)
    dataupdate = db.Column(db.Datetime)
    bitativo = db.Column(db.Boolean)

class ProductImage(db.Model):
    image = db.Column(db.Integer, primary_key=True)
    idproduto = db.Column(db.Integer)
    sku = db.Column(db.String)
    dataupdate = db.Column(db.Datetime)
    bitativo = db.Column(db.Boolean)

class Saldo(db.Model):
    saldoid = db.Column(db.Integer, primary_key=True)
    idproduto = db.Column(db.Integer)
    saldo = db.Column(db.Float)
    dataupdate = db.Column(db.Datetime)
    bitativo = db.Column(db.Boolean)

class Brand(db.Model):
    brandid = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String)
    name = db.Column(db.String)
    dataupdate = db.Column(db.Datetime)


class Category(db.Model):
    categoryid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    sku = db.Column(db.String)

class Collections(db.Model):
    idcollection = db.Column(db.Integer, primary_key=True)
    namecollection = db.Column(db.String)
    idlista = db.Column(db.Integer)
    sku = db.Column(db.String)
    dateupdate = db.Column(db.Integer)
    bitativo = db.Column(db.Boolean)