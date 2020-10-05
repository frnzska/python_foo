from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB init
db = SQLAlchemy(app)

# Marshmallow init
ma = Marshmallow(app)

# simple example
# runs on http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def get():
    return jsonify({'message': 'hallo'})


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float)


    def __init__(self, description, name, price):
        self.description = description
        self.name = name
        self.price = price


    def __str__(self):
        return f'{self.name}: {self.description} for {self.price} Euro'


    def __repr__(self):
        return f"<Product('{self.name}', '{self.description}', '{self.price}')>"



class ProductSchema(ma.Schema):

    class Meta:
        # fields to show on API
        fields = ('id', 'description', 'name', 'price')


# init schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/product', methods=['POST'])
def add_product():
    description = request.json['description']
    name = request.json['name']
    price = request.json['price']

    new_product = Product(description=description, name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)


@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    #as http://127.0.0.1:5000/product/1
    product = Product.query.get(id)
    return product_schema.jsonify(product)


@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()


@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)
  product.description = request.json['description']
  product.name = request.json['name']
  product.price = request.json['price']
  db.session.commit()


@app.route('/products', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result.data)




if __name__ == '__main__':
    # starts sever
    app.run(debug=True)


"""
create db.sqlite file via python console executing:
>>> from app import db
>>> db.create_all()
"""