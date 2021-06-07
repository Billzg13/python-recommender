from flask_restful import Resource, fields
from flask import jsonify, request, make_response
from flask_restful_swagger import swagger
import numpy as np
import pandas as pd
import json
#import src.util.recommender_v2 as recommender
import src.util.recommender_wrapper as recommender
import logging
logger = logging.getLogger(__name__)

COLLABORATIVE_TYPE = 'collaborative'
CONTENT_TYPE = 'content'
# print(__name__)


class quick_search_controller(Resource):
    def post(self):
        print('in quick search')
        json_data = request.get_json(force=True)
        if json_data['type'] == COLLABORATIVE_TYPE:
            data_places = recommender.recommend_collaborative(json_data)
        else: 
            data_places = recommender.recommend_content_based(json_data)
        logger.debug("In action: post quick search controller")
        return {"result": data_places}

'''
def func(json_data):
    data_places = json_data["user"]["favourites"]
    data_user_id = json_data["user"]["id"]
    blacklisted_places = []  # blacklisted places
    result = []
    for place in data_places:
        if not place['name']:  # if name is null break the for loop and go on
            break
        blacklisted_places.append(place['name'])

    for place in data_places:
        prediction = recommender.predict(place['name'])
        for item in prediction['Correlation']:
            if item not in blacklisted_places:
                result.append({
                    'name': item,
                    'correlation': prediction['Correlation'][item],
                    'placeId': 9999,
                    'correlationWith': place['placeId']
                })
                blacklisted_places.append(item)
    return result    
'''    


