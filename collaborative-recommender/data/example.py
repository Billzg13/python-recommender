import numpy as np
import pandas as pd


ratings_data = pd.read_csv("ratings.csv")
#print(ratings_data.head())

movie_names = pd.read_csv("movies.csv")
#print(movie_names.head())

# Merge movie names and ratings 
movie_data = pd.merge(ratings_data, movie_names, on='movieId')
#print(movie_data.head())
#print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head())

# Get the mean ratings of movies
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())
#print(ratings_mean_count.head())

user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')


forrest_gump_ratings = user_movie_rating['Forrest Gump (1994)']
movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])
corr_forrest_gump.dropna(inplace=True)

corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])


print(corr_forrest_gump[corr_forrest_gump ['rating_counts']>50].sort_values('Correlation', ascending=False).head())
#corr_forrest_gump.head()

rambo_ratings = user_movie_rating['Rambo III (1988)']
movies_like_rambo = user_movie_rating.corrwith(rambo_ratings)

corr_rambo = pd.DataFrame(movies_like_rambo, columns=['Correlation'])
corr_rambo.dropna(inplace=True)
corr_rambo = corr_rambo.join(ratings_mean_count['rating_counts'])

print(corr_rambo[corr_rambo['rating_counts']>50].sort_values('Correlation', ascending=False).head(20))
