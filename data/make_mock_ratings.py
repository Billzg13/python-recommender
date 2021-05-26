#import csv  libray and random
import csv
import random

#model : userId,placeId,rating

with open('actual_ratings_real.csv', mode='w') as ratings_file:
    ratings_writer = csv.writer(ratings_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, 600):
      user_id = random.randint(0, 150)
      for i in range(0,3):
        place_id = random.randint(0,131)
        rating = random.randint(0, 5)
        ratings_writer.writerow([user_id, place_id, rating])
      