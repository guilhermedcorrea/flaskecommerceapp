from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db


class Atributos(db.Model):
    atributoid = db.Column(db.Integer, primary_key=True)
    idproduto = db.Column()
    especificacoes = db.Column()
    idimagem = db.Column()
    dataupdate = db.Column()
    bitativo = db.Column()


class ProductImage(db.Model):
    image = db.Column(db.Integer, primary_key=True)
    idproduto = db.Column()
    sku = db.Column()
    dataupdate = db.Column()
    bitativo = db.Column()

class Saldo(db.Model):
    saldoid = db.Column(db.Integer, primary_key=True)
    idproduto = db.Column()
    saldo = db.Column()
    dataupdate = db.Column()
    bitativo = db.Column()


class Brand(db.Model):
    brandid = db.Column(db.Integer, primary_key=True)
    sku = db.Column()
    name = db.Column()
    dataupdate = db.Column()


class Category(db.Model):
    categoryid = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    sku = db.Column(db.String)


class Collections(db.Model):
    idcollection = db.Column(db.Integer, primary_key=True)
    namecollection = db.Column(db.String)
    idlista = db.Column(db.Integer)
    sku = db.Column(db.String)
    dateupdate = db.Column(db.Integer)
    bitativo = db.Column()