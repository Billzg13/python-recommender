import src.util.recommender_v2 as recommender

def recommend(json_data):
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
