import numpy as np
import pandas as pd
import os

ratings_data = pd.read_csv(os.getcwd() +"/data/actual_ratings.csv") #show head(10)

place_names = pd.read_csv(os.getcwd() + "/data/places.csv", error_bad_lines=False) # show head(10)

# Merge place names and ratings 
place_data = pd.merge(ratings_data, place_names, on='placeId') # show head(10)

# Get the mean ratings of places
ratings_mean_count = pd.DataFrame(place_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(place_data.groupby('title')['rating'].count())

user_place_rating = place_data.pivot_table(index='userId', columns='title', values='rating')

def predict(place_name):
  place_ratings = user_place_rating[place_name]
  places_like_place = user_place_rating.corrwith(place_ratings)
  corr_place = pd.DataFrame(places_like_place, columns=['Correlation'])
  corr_place = corr_place.sort_values('Correlation', ascending=False)
  corr_place = corr_place.join(ratings_mean_count['rating_counts'])
  corr_place.dropna(inplace=True)
  return corr_place[corr_place['rating_counts']>15].sort_values('Correlation', ascending=False).head(10).to_dict()
