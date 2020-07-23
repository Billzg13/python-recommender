import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd
import src.util.http_requests as http_requests

#everything that has to do with the recommender will be here
'''
genderNumeric: 0 || male 0, female 1
age: 24 || 13 - 100
priceLevel: 4 || 0 - 5
restaurant: 0 - 5
lodging: 0 - 5
food: 0 - 5
pointOfInterest: 0 - 5
establishment: 0 - 5
bar: 0 - 5
cafe: 0 - 5
health: 0 - 5
gym: 0 - 5
'''
data_json = http_requests.get_recommender_data() #array of json
if data_json != 0:  
  df = pd.read_json(data_json)
  df.replace('?', -99999, inplace=True)
  df.drop(['id'], 1, inplace=True)
  df.drop(['userId'], 1, inplace=True)

  X = np.array(df.drop(['placeId'], 1))
  y = np.array(df['placeId'])

  X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

  clf = neighbors.KNeighborsClassifier()
  clf.fit(X_train, y_train)

  accuracy = clf.score(X_test, y_test)
  print(accuracy)

#example_measures = np.array([5,2,1,1,2,1,4,1,2])
#example_measures = example_measures.reshape(1, -1)

#custom_predict(example_measures)


#make the data object "good" for the machine learning algorithm


def make_prediction(data):
  #also has to reshare the data
  prediction = clf.predict(data)
  print(prediction)
  return prediction