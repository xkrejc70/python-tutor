from app import app
from flask import jsonify, request
from app.uploads.upload_handler import upload_handler
from app.upload_and_test import upload_and_test
from app.upload_and_test import upload_and_test
from app.admin.settings import load_settings, save_settings
from app.admin.login import authenticate
from app.questions.questions import get_questions
import requests

# TODO: delete
import socket

@app.route('/proj4')
def proj4():

    url = 'http://localhost:5050/proj4'
    data = {'input_string': """
        perms = all_permutations_substrings(string)
        return set(words) & set(perms) 
    """}

    response = requests.post(url, json=data)
    result = response.json()

    # Process the prediction as needed
    return jsonify({'model_response': result})

@app.route('/proj8')
def proj8():

    url = 'http://localhost:5050/proj8'
    data = {'input_string': """
    def first_with_given_key(iterable, key = lambda x: x):
                seen = set()
                for x in iterable:
                    if repr(key(x)) not in seen:
                        seen.add(repr(key(x)))
                        yield x
    """}

    response = requests.post(url, json=data)
    result = response.json()

    # Process the prediction as needed
    return jsonify({'model_response': result})

# TODO: move to utils
@app.route('/api/questions/<string:project>', methods=['GET'])
def get_questions_route(project):
    return get_questions(project)

# TODO: delete
@app.route("/api/test", methods=['GET', 'POST'])
def api_upload():
    return ("host")

# Upload and test
@app.route("/api/upload", methods=['GET', 'POST'])
def upload():
    return upload_and_test(request)

# TODO: delete
# Show server
@app.route("/s", methods=['GET'])
def return_home():
    return jsonify({"host": "Hostname: " + socket.gethostname()})



# todo: secure admin requests
@app.route('/api/admin/projects', methods=['GET'])
def get_items():
    return load_settings()

@app.route('/api/admin/save', methods=['POST'])
def save_projects():
    return save_settings(request)

@app.route('/api/admin/login', methods=['POST'])
def login():
    return authenticate(request)