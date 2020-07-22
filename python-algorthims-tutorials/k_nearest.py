import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

def custom_predict(data):
  prediction = clf.predict(data)
  print(prediction)
  return prediction

df = pd.read_csv('breast-cancer-wisconsin.txt')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([5,2,1,1,2,1,4,1,2])
example_measures = example_measures.reshape(1, -1)

custom_predict(example_measures)

