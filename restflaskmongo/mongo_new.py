#!/usr/bin/env python

from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import fields
from flask_restful import marshal
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()


app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'


mongo = PyMongo(app)


@auth.get_password
def get_password(username):
    if username == 'jacob':
        return 'password'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


star_fields = {
   'name': fields.String,
   'distance': fields.Float,
   }


class Star(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('distance', type=int, location='json')
        super(Star, self).__init__()

    def get(self):
        stars = mongo.db.stars.find()
        return {'result': [marshal(star, star_fields) for star in stars]}

    def post(self):
        stars = mongo.db.stars
        args = self.reqparse.parse_args()
        star = {
            'name': args['name'],
            'distance': args['distance']
        }
        stars.insert(star)
        return {'result': marshal(star, star_fields)}, 201

    # add method for returning a single record

    # add emthod for deleting a record


api = Api(app)
api.add_resource(Star, '/api/v1.0', endpoint='star')


if __name__ == '__main__':
    app.run(debug=True)
