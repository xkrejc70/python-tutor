from app import app
from flask import jsonify
import json
import os

CONFIG_FILE = 'settings.json'

script_dir = os.path.dirname(os.path.abspath(__file__))
file_p = os.path.join(script_dir, CONFIG_FILE)

def read_config():
    try:
        with open(file_p, 'r') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        config_data = []
    return config_data

def write_config(config_data):
    with open(file_p, 'w') as file:
        json.dump(config_data, file, indent=2)

def load_settings():
    return jsonify(read_config())

def save_settings(request):
    try:
        # Receive data from the request in the desired format
        received_data = request.json

        # Extract the selected items
        selected_items = received_data if isinstance(received_data, list) else []

        # Read existing settings from the JSON file
        with open(file_p, 'r') as json_file:
            existing_settings = json.load(json_file)

        # Update the existing settings with the new selected items
        updated_settings = []
        for existing_item in existing_settings:
            updated_item = next((item for item in selected_items if item['id'] == existing_item['id']), None)
            if updated_item:
                # Use the updated item if available
                updated_settings.append(updated_item)
            else:
                # If the item is not in selected_items, set 'checked' to False
                existing_item['checked'] = False
                updated_settings.append(existing_item)

        # Save the updated settings to the JSON file
        with open(file_p, 'w') as json_file:
            json.dump(updated_settings, json_file)

        return jsonify({"message": "Settings saved"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
