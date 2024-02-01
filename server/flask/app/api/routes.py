from app import app
from flask import jsonify, request
from app.uploads.upload_handler import upload_handler
from app.upload_and_test import upload_and_test
import requests

# TODO: delete
import socket

@app.route('/model')
def make_prediction():
    # Make a request to the Hugging Face model service
    model_url = 'http://model:6000/predict'
    response = requests.get(model_url)

    # Extract prediction from the response
    prediction = response.json()

    # Process the prediction as needed
    return jsonify({'prediction': prediction})

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