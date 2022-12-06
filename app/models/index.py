
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db


class CollectionsHomeProduct(db.Model):
    idcollectionp = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String)
    namecollection = db.Column(db.String)
    dataupdate = db.Column(db.Datetime)
    bitativo = db.Column()
