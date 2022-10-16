from typing import Any
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(300), unique=True)
    idcategoria = db.Column(db.Integer)
    iddepartamento = db.Column(db.Integer)
    preco = db.Column(db.Float) #in cents
    saldo = db.Column(db.Float)
    marca = db.Column(db.String(400))
    metro = db.Column(db.Float)
    descricao = db.Column(db.String(5000))
    imagem = db.Column(db.String(2000))
    bitativo = db.Column(db.Boolean)
    orders = db.relationship('Order_Item', backref='product', lazy=True)

class Precos(db.Model):
    idpreco =  db.Column(db.Integer, primary_key=True)
    idproduto = db.Column(db.Integer)
    idmarca = db.Column(db.Integer)
    precocusto = db.Column(db.Float)
    precovenda = db.Column(db.Float)
    margem = db.Column(db.Float)
    ean = db.Column(db.String(30))
    sku = db.Column(db.String(30))
    data_alterado = db.Column(db.DateTime)
    idunidade = db.Column(db.Integer)
    metroproduto = db.Column(db.Float)
    preco_frete = db.Column(db.Float)
    produtoativo = db.Column(db.Boolean)


class ListaDePrecos(db.Model):
    idlistapreco = db.Column(db.Integer, primary_key=True)
    idproduto = db.Column(db.Integer)
    idmarcaproduto = db.Column(db.Integer)
    custo = db.Column(db.Float)
    precoproduto = db.Column(db.Float)
    margem = db.Column(db.Float)
    bitativo = db.Column(db.Boolean)
    dataalterado =db.Column(db.DateTime)


class Promocoes(db.Model):
    idprodmocao  =db.Column(db.Integer, primary_key=True)
    idproduto = db.Column(db.Integer)
    nomepromocao = db.Column(db.String(2000))
    datainicio = db.Column(db.DateTime)
    datafinal =db.Column(db.DateTime)
    descontoproduto = db.Column(db.Float)
    listaprodutos = db.Column(db.String)
    bitativo = db.Column(db.Boolean)

class Categorias(db.Model):
    idcategoria =  db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(300))

class Departamentos(db.Model):
    iddepartamento =  db.Column(db.Integer, primary_key=True)
    departamento = db.Column(db.String(300))

class Concorrente(db.Model):
    idconcorrente = db.Column(db.Integer, primary_key=True)
    precoconcorrente = db.Column(db.Float)
    concorrente = db.Column(db.Float)
    url_google = db.Column(db.String(2000))
    url_anuncio = db.Column(db.String(2000))
    data_anuncio = db.Column(db.DateTime)
    produtoativo = db.Column(db.Boolean)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referencia = db.Column(db.String(5))
    nomecliente = db.Column(db.String(20))
    sobrenome = db.Column(db.String(20))
    telefone = db.Column(db.Integer)
    email = db.Column(db.String(50))
    endereco = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(20))
    status = db.Column(db.String(10))
    pagamento = db.Column(db.String(10))
    items = db.relationship('Order_Item', backref='order', lazy=True)

    def order_total(self) -> Any:
        return db.session.query(db.func.sum(Order_Item.quantity * Product.preco)).join(Product).filter(Order_Item.order_id == self.id).scalar() + 1000

    def quantity_total(self) -> Any:
        return db.session.query(db.func.sum(Order_Item.quantity)).filter(Order_Item.order_id == self.id).scalar()

class Order_Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)

