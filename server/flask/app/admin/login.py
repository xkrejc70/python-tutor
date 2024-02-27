from app import app
from flask import Flask, request, jsonify
import json
import os

CONFIG_FILE = 'admin_config.json'

script_dir = os.path.dirname(os.path.abspath(__file__))
file_p = os.path.join(script_dir, CONFIG_FILE)

# Load credentials
def load_credentials():
    with open(file_p, 'r') as json_file:
        config_data = json.load(json_file)
        credentials = config_data.get('credentials', {})
    return credentials

# Admin authentication
def authenticate(request):
    data = request.json
    username = data.get('username')
    password = data.get('password')

    credentials = load_credentials()

    # Check against the loaded credentials
    if username == credentials.get('username') and password == credentials.get('password'):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid username or password"}), 401