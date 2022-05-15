from flask import Flask
import flask.scaffold
from matplotlib.pyplot import hot
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api
from Resources.hoteis import Hoteis

app = Flask(__name__)
api = Api(app)



api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug = True)