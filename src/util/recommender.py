import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd
import src.util.http_requests

#everything that has to do with the recommender will be here
'''
gender: 0 || male 0, female 1
age: 24 || 13 - 100
price_level: 4 || 0 - 5
restaurant: 0 - 5
lodging: 0 - 5
food: 0 - 5
point_of_interest: 0 - 5
establishment: 0 - 5
bar: 0 - 5
cafe: 0 - 5
health: 0 - 5
gym: 0 - 5
'''
data = http_requests.get_recommender_data()

#make the data object "good" for the machine learning algorithm


def make_prediction(data):
  prediction = clf.predict(data)
  print(prediction)
  return prediction