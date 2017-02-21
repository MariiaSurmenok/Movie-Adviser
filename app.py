#!flask/Scripts/python
from flask import Flask
from flask import jsonify

import json

app = Flask(__name__)

filepath = './data/movies_in_theaters.json'
recent_movies = []

# Read new movies from json
try:
    with open(filepath) as f_obj:
        recent_movies = json.load(f_obj)
except FileNotFoundError:
    print("File not found, check your json path")

# Prepare response body
message = "There are few movies in theaters: "
for movie in recent_movies:
    message = message + movie + ", "

# Handle POST request from API.AI.
@app.route('/movie-adviser/api', methods=['POST'])
def get_movies_in_theaters():
    return jsonify({'speech': message, 'displayText': message})

# Start web service.
if __name__ == '__main__':
    app.run(debug=True, port=5001)