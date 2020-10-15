from flask_restful import Resource, fields
from flask import jsonify, request, make_response
from flask_restful_swagger import swagger
import numpy as np
import pickle as p
import logging
logger = logging.getLogger(__name__)

print(__name__)


class quick_search_controller(Resource):
    def post(self):
        print('in quick search')
        json_data = request.get_json(force=True)
        print(json_data)
        #user = json_data['user']
        # print(user['types'])
        logger.debug("In action: post quick search controller")
        return {"message": "hello!"}


if __name__ == 'src.controllers.quick_search_controller':
    modelfile = 'models/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
