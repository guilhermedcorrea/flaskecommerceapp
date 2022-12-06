from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db
    

"""
Armazena informações de Usuarios, grupos de usuarios e permissoes

"""
class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    groupuser = db.Column(db.String(100))
    usuariologado = db.Column(db.Boolean)
    datalogado = db.Column(db.Datetime)
    bitativo = db.Column(db.Boolean)
    dataupdate  = db.Column(db.Datetime)

class UserGroup(db.Model):
    groupid = db.Column(db.Integer, primary_key=True)
    nomegrupo =  db.Column(db.String(100))
    dataupdate =  db.Column(db.Datetime)

class Cliente(db.Model):
    idcliente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer)
    endereco = db.Column(db.String(1000))
    telefone= db.Column(db.String(50))
    email = db.Column(db.String(300))
    totalpedido = db.Column(db.Float)
    pedidosrealizados = db.Column(db.Integer)
    dataupdate = db.Column(db.Datetime)

