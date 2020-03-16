from flask_restful import Resource, fields
from flask import jsonify, request, make_response
from flask_restful_swagger import swagger
import logging
logger = logging.getLogger(__name__)

class advanced_search_controller(Resource):
    def post(self):

        logger.debug("In action: post advanced controller")
        return { "message":"hello!" }