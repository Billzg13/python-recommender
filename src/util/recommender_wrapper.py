import src.util.recommender_colaborative_v2 as recommender_collaborative
import src.util.recommender_content as recommender_content

def recommend_collaborative(json_data):
    data_places = json_data["user"]["favourites"]
    data_user_id = json_data["user"]["id"]
    blacklisted_places = []  # blacklisted places
    result = []
    for place in data_places:
        if not place['name']:  # if name is null break the for loop and go on
            break
        blacklisted_places.append(place['name'])

    for place in data_places:
        prediction = recommender_collaborative.predict(place['name'])
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

def recommend_content_based(json_data):
    data_places = json_data["user"]["favourites"]
    data_user_id = json_data["user"]["id"]
    blacklisted_places = []  # blacklisted places
    result = []
    for place in data_places:
        if not place['name']:  # if name is null break the for loop and go on
            break
        blacklisted_places.append(place['name'])
    
    for place in data_places:
        prediction = recommender_content.predict(place['name'])
        for item in prediction:
            if item['title'] not in blacklisted_places:
                result.append({
                    'name': item['title'],
                    'correlation': item['correlation'],
                    'placeId': 9999,
                    'correlationWith': place['placeId']
                })
                blacklisted_places.append(item)
    return result

