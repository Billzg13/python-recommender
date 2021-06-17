import numpy as np
import pandas as pd

ratings_data = pd.read_csv("collaborative-recommender/data/actual_example_places/actual_ratings.csv")
#print(ratings_data.head())


place_names = pd.read_csv("collaborative-recommender/data/actual_example_places/places.csv")
#print(place_names.head())


# Merge place names and ratings 
place_data = pd.merge(ratings_data, place_names, on='placeId')
place_data.head()

#print(place_data.groupby('title')['rating'].count().sort_values(ascending=False).head(10))
#print(place_data.head())

# Get the mean ratings of places
ratings_mean_count = pd.DataFrame(place_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(place_data.groupby('title')['rating'].count())
#print(ratings_mean_count.head())


# convert to userId x place1, place2, place3, ....., placeN
user_place_rating = place_data.pivot_table(index='userId', columns='title', values='rating') 
#print(user_place_rating.head(5))

Melia_ratings = user_place_rating['Meliá Athens']

#Melia_ratings.head()


places_like_Melia = user_place_rating.corrwith(Melia_ratings)
corr_Melia_athens = pd.DataFrame(places_like_Melia, columns=['Correlation'])
corr_Melia_athens.dropna(inplace=True)
corr_Melia_athens = corr_Melia_athens.sort_values('Correlation', ascending=False)


#corr_Melia_athens.head()

corr_Melia_athens = corr_Melia_athens.join(ratings_mean_count['rating_counts'])

corr_Melia_athens[corr_Melia_athens['rating_counts'] > 18].sort_values('Correlation', ascending=False).head()

#print(corr_Melia_athens.head(10))

#print(corr_Melia_athens)
