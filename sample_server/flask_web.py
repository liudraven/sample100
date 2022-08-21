# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/6/30
# aim:

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


app.run(host='0.0.0.0', port=9000)

api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
