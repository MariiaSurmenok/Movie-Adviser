#!flask/Scripts/python
from flask import Flask
from flask import jsonify
from flask import request
import json

import get_data


app = Flask(__name__)

filepath = './data/movies_in_theaters.json'
logpath = './data/request_logs.txt'
recent_movies = []

# Read new movies from json
recent_movies = get_data.get_recent_movies(filepath)

# Prepare response body
message = "There are few movies in theaters: "
for movie in recent_movies:
    message = message + movie + ", "

# Handle POST request from API.AI.
@app.route('/movie-advisor/api', methods=['POST'])
def get_movies_in_theaters():
    get_data.log_data(logpath, request.json)
    return jsonify({'speech': message, 'displayText': message})

# Start web service.
if __name__ == '__main__':
    app.run(debug=True, port=5001)
