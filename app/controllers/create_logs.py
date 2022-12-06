from functools import wraps
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()


