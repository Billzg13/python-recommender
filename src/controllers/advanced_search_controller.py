from flask_restful import Resource, fields
from flask import jsonify, request, make_response
from flask_restful_swagger import swagger
import numpy as np
import pickle as p
import logging
logger = logging.getLogger(__name__)


class advanced_search_controller(Resource):
    def post(self):
        print('In post advanced search')
        json_request = request.get_json(force=True)
        print(json_request)

        logger.debug("In action: post advanced controller")
        return {"message": "hello!"}


if __name__ == 'src.controllers.advanced_search_controller':
    modelfile = 'models/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
