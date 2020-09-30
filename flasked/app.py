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
"""
#simple example
#runs on http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def get():
    return jsonify({'message': 'hallo'})
"""

class User(db.Model):
    pass


class Order(db.Model):
    pass


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float)


class Server(db.Model):
    pass



# Todo: get, post, routes, schemas



if __name__ == '__main__':
    # starts sever
    app.run(debug=True)


