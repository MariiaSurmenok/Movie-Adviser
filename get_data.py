# In the future we will call web service to obtain data about movies.
import json

filepath = './data/movies_in_theaters.json'

recent_movies = [
    'get out', 'collide', 'rock dog', 
    'bitter harvest', 'as you are'
]


with open(filepath, 'w') as f_obj:
    json.dump(recent_movies, f_obj)