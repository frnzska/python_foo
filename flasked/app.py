from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# init app
app = Flask(__name__)

"""
#simple example
#runs on http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def get():
    return jsonify({'message': 'hallo'})
"""

if __name__ == '__main__':
    # starts sever
    app.run(debug=True)


