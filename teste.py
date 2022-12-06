from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = r'C:\flaskecommerce\images'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(r"C:\flaskecommerce", 'storeapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecret'
    

#configure_uploads(app, photos)

db = SQLAlchemy(app)



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True)
    preco = db.Column(db.Integer) #in cents
    saldo = db.Column(db.Integer)
    descricao = db.Column(db.String(500))
    marca = db.Column(db.String(500))
    imagem = db.Column(db.String(100))

    orders = db.relationship('Order_Item', backref='product', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referencia = db.Column(db.String(5))
    nome = db.Column(db.String(20))
    sobrenome = db.Column(db.String(20))
    telefone = db.Column(db.Integer)
    email = db.Column(db.String(50))
    endereco = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estadi = db.Column(db.String(20))
    pais = db.Column(db.String(20))
    status = db.Column(db.String(10))
    pagamento = db.Column(db.String(10))
    items = db.relationship('Order_Item', backref='order', lazy=True)

    def order_total(self):
        return db.session.query(db.func.sum(Order_Item.quantidade * Product.preco)).join(Product).filter(Order_Item.order_id == self.id).scalar() + 1000

    def quantity_total(self):
        return db.session.query(db.func.sum(Order_Item.quantidade)).filter(Order_Item.order_id == self.id).scalar()

class Order_Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantidade = db.Column(db.Integer)



