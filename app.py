from flask import Flask
from flask_restful import Resource, Api
import os
from flask_cors import CORS, cross_origin
from flask_restful_swagger import swagger
import logging
from logging.handlers import TimedRotatingFileHandler
import src.util.recommender
from src.controllers.hello_controller import hello_controller
from src.controllers.quick_search_controller import quick_search_controller
from src.controllers.advanced_search_controller import advanced_search_controller

app = Flask(__name__)
CORS(app)
api = swagger.docs(Api(app), apiVersion='0.1')

file_handler = TimedRotatingFileHandler(
    "logs/all_logs.log", when="midnight", interval=1)
formatter = logging.Formatter(
    '%(asctime)s||%(levelname)s||%(message)s', datefmt='%m/%d/%Y %H:%M:%S')
file_handler.setFormatter(formatter)
logging.basicConfig(level=logging.DEBUG, handlers=[file_handler])

##
# Actually setup the Api resource routing here
##
api.add_resource(hello_controller, '/hello')
api.add_resource(quick_search_controller, '/search')
api.add_resource(advanced_search_controller, '/advanced_search')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
