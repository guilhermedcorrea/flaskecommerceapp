from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db
    
class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    groupuser = db.Column()
    usuariologado = db.Column()
    datalogado = db.Column()
    bitativo = db.Column()
    dataupdate  = db.Column()


class UserGroup(db.Model):
    groupid = db.Column(db.Integer, primary_key=True)
    nomegrupo =  db.Column()
    dataupdate =  db.Column()

class Cliente(db.Model):
    idcliente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Integer, primary_key=True)
    groupid = db.Column()
    endereco = db.Column()
    telefone= db.Column()
    email = db.Column()
    totalpedido = db.Column()
    pedidosrealizados = db.Column()
    dataupdate = db.Column()

