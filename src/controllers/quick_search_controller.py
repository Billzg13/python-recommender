from flask_restful import Resource, fields
from flask import jsonify, request, make_response
from flask_restful_swagger import swagger
import numpy as np
import pickle as p
import pandas as pd
import json
import logging
logger = logging.getLogger(__name__)

print(__name__)

'''
  "id": 123,
    "gender": 0,        -> json_data.user.gender
    "age": 24,          -> json_data.user.age
    "price_level": 4,   -> json_data.user.priceLevel
    "restaurant": 1,    -> json_data.user.types.restaurant
    "lodging": 1,
    "food": 1,
    "point_of_interest": 0,
    "establishment": 0,
    "bar": 0,
    "cafe": 1,
    "health": 1,
    "gym": 1,
    "placeId": 1

'''


class quick_search_controller(Resource):
    def post(self):
        print('in quick search')
        json_data = request.get_json(force=True)
        # print(json_data)
        data = json_data["user"]["types"]
        data["gender"] = 0
        data["age"] = 20
        data["price_level"] = 1
        data_array = np.array([data["gender"], data["age"], data["price_level"], data["restaurant"], data["lodging"], data["food"],
                               data["pointOfInterest"], data["establishment"], data["bar"], data["cafe"]+1, data["health"], data["gym"]])

        data_array = data_array.reshape(1, -1)
        print(data_array)
        prediction = np.array2string(model.predict(data_array))

        # we want json_data.user.types
        # print(model.predict(data_array))
        #user = json_data['user']
        # print(user['types'])
        logger.debug("In action: post quick search controller")
        return jsonify(prediction)


if __name__ == 'src.controllers.quick_search_controller':
    print('in here yeay!')
    modelfile = 'models/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
