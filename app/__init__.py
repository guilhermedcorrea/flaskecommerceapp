from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os




basedir = os.path.abspath(os.path.dirname(__file__))



db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['UPLOADED_PHOTOS_DEST'] = r'C:\flaskecommerce\images'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(r"C:\flaskecommerce", 'trendy.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'mysecret'
    
    from .models.models import configure

    db.init_app(app)
    configure(app)
    with app.app_context():
        from .routes.routes import ecommerce_bp
        app.register_blueprint(ecommerce_bp)

    return app
