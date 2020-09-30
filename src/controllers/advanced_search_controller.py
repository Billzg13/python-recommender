from flask_restful import Resource, fields
from flask import jsonify, request, make_response
from flask_restful_swagger import swagger
from src.util.recommender import make_prediction 
import logging
logger = logging.getLogger(__name__)

class advanced_search_controller(Resource):
    def post(self):
        print('In post advanced search')
        json_request = request.get_json(force=True)
        predict_data = json_request['advancedSearchRequest']
        ##it goes like this
        result = make_prediction(predict_data)

        logger.debug("In action: post advanced controller")
        return { "message":"hello!" }