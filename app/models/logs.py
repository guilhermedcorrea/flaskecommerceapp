
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db



class LogUser(db.Model):
    pass


class LogOrder(db.Model):
    pass


class LogProduct(db.Model):
    pass


class LogSaldo(db.Model):
    pass


class LogPrice(db.Model):
    pass