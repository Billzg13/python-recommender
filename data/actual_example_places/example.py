import numpy as np
import pandas as pd

ratings_data = pd.read_csv("actual_ratings.csv")

place_names = pd.read_csv("places.csv")


# Merge movie names and ratings 
place_data = pd.merge(ratings_data, place_names, on='placeId')

# Get the mean ratings of places
ratings_mean_count = pd.DataFrame(place_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(place_data.groupby('title')['rating'].count())

user_place_rating = place_data.pivot_table(index='userId', columns='title', values='rating')

Melia_ratings = user_place_rating['Meliá Athens']
places_like_Melia = user_place_rating.corrwith(Melia_ratings)

corr_Melia_athens = pd.DataFrame(places_like_Melia, columns=['Correlation'])
corr_Melia_athens.dropna(inplace=True)

corr_Melia_athens = corr_Melia_athens.join(ratings_mean_count['rating_counts'])
print(corr_Melia_athens.to_dict())
print(corr_Melia_athens)


{
  'Correlation': 
    {
      'Bits and Bytes': 0.8660254037844385, 
      'Meliá Athens': 1.0, 
      'Radisson Blu Park Hotel Athens': 0.9999999999999999, 
      'The Athenian Callirhoe Exclusive Hotel': 0.5
    }, 
  'rating_counts': 
    {
      'Bits and Bytes': 5, 
      'Meliá Athens': 4, 
      'Radisson Blu Park Hotel Athens': 6, 
      'The Athenian Callirhoe Exclusive Hotel': 6
    }
}
