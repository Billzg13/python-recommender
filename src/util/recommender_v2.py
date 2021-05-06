import numpy as np
import pandas as pd
import os

ratings_data = pd.read_csv(os.getcwd() +"/data/actual_ratings.csv")

place_names = pd.read_csv(os.getcwd() + "/data/places.csv")

# Merge place names and ratings 
place_data = pd.merge(ratings_data, place_names, on='placeId')

# Get the mean ratings of places
ratings_mean_count = pd.DataFrame(place_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(place_data.groupby('title')['rating'].count())

user_place_rating = place_data.pivot_table(index='userId', columns='title', values='rating')

#Melia_ratings = user_place_rating['Meliá Athens']
#places_like_Melia = user_place_rating.corrwith(Melia_ratings)

#corr_Melia_athens = pd.DataFrame(places_like_Melia, columns=['Correlation'])
#corr_Melia_athens.dropna(inplace=True)

#corr_Melia_athens = corr_Melia_athens.join(ratings_mean_count['rating_counts'])
#print(corr_Melia_athens)

def predict(place_name):
  place_ratings = user_place_rating[place_name]
  places_like_place = user_place_rating.corrwith(place_ratings)
  corr_place = pd.DataFrame(places_like_place, columns=['Correlation'])
  corr_place.dropna(inplace=True)
  corr_place = corr_place.join(ratings_mean_count['rating_counts'])
  return corr_place.sort_values('Correlation', ascending=False).head(10).to_dict()
