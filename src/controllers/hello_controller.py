from flask_restful import Resource, fields
from flask import jsonify, request, make_response
from flask_restful_swagger import swagger
import logging
logger = logging.getLogger(__name__)

class hello_controller(Resource):
    def get(self):
        logger.debug("In action: get")
        return { "message":"hello!" }