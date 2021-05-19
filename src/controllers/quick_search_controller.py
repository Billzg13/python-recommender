from flask_restful import Resource, fields
from flask import jsonify, request, make_response
from flask_restful_swagger import swagger
import numpy as np
import pickle as p
import pandas as pd
import json
import src.util.recommender_v2 as recommender
import logging
logger = logging.getLogger(__name__)

# print(__name__)


class quick_search_controller(Resource):
    def post(self):
        print('in quick search')
        json_data = request.get_json(force=True)
        data_places = func(json_data)
        logger.debug("In action: post quick search controller")
        #print('return this: ')
        #print(data_places)
        return {"result": data_places}


def func(json_data):
    data_places = json_data["user"]["favourites"]
    data_user_id = json_data["user"]["id"]
    blacklisted_places = ['Meliá Athens']  # blacklisted places
    result = []
    for place in data_places:
        if not place['name']:  # if name is null break the for loop and go on
            break
        blacklisted_places.append(place['name'])

    for place in data_places:
        if not place['name']:  # if name is null break the for loop and go on
            break
        blacklisted_places.append(place['name'])
        prediction = recommender.predict(place['name'])
        for item in prediction['Correlation']:
            if item not in blacklisted_places:
                result.append({
                    'name': item,
                    'correlation': prediction['Correlation'][item],
                    'placeId': place['placeId']
                })

    prediction = recommender.predict("Meliá Athens")
    print(prediction['Correlation'])
    for item in prediction['Correlation']:
        print(prediction['Correlation'][item])
        if item not in blacklisted_places:
            result.append({
                    'name': item,
                    'correlation': prediction['Correlation'][item],
                    'placeId':1
                })
    print(result)
    return result



# This recommender is now obsolete, these lines should be deleted
if __name__ == 'src.controllers.quick_search_controller':
    print('in here yeay!')
    modelfile = 'models/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
