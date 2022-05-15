from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# essa classe vai ser um recurso da nossa api
class Hoteis(Resource):
    def get(self):
        return {'Hoteis':'meus hoteis'}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug = True)