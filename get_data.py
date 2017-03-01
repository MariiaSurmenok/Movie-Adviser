# In the future we will call web service to obtain data about movies.
import json

filepath = './data/movies_in_theaters.json'

recent_movies = [
    'get out', 'collide', 'rock dog', 
    'bitter harvest', 'as you are'
]


with open(filepath, 'w') as f_obj:
    json.dump(recent_movies, f_obj)

def log_data(filepath, data):
    """Write requests to file"""
    with open(filepath, 'a') as f_obj:
        f_obj.write("\n")
        json.dump(data, f_obj)

def get_recent_movies(filepath):
    """Return list of recent movies"""
    try:
        with open(filepath) as f_obj:
            return json.load(f_obj)
    except FileNotFoundError:
        print("File not found, check your json path")