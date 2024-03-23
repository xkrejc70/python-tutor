from app import app
from flask import jsonify
import json
import os

CONFIG_FILE = 'project_settings.json'
TESTS = 'test_data.json'
MODELS = 'project_models.json'
CONFIG = 'config'

file_p = os.path.join(CONFIG, CONFIG_FILE)
tests_p = os.path.join(CONFIG, TESTS)
models_p = os.path.join(CONFIG, MODELS)

# Read configuration data from the JSON file
def read_config():
    try:
        with open(file_p, 'r') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        config_data = []
    return config_data

# Write configuration data to the JSON file
def write_config(config_data):
    with open(file_p, 'w') as file:
        json.dump(config_data, file, indent=2)

# Load and return current settings
def load_settings():
    app.logger.debug("Loading settings...")
    config_data = read_config()

    # Read tests data from tests.json
    with open(tests_p, 'r') as tests_file:
        tests_data = json.load(tests_file)

    # Add 'tests_exist' field to each project in config_data
    for project in config_data:
        project_id = project['id']
        tests_key = f'proj{project_id}'
        tests_exist = tests_key in tests_data and bool(tests_data.get(tests_key))
        project['tests_exist'] = tests_exist

    app.logger.debug("Settings loaded successfully.")
    return jsonify(config_data)

# Receive and save updated settings
def save_settings(request):
    try:
        app.logger.debug("Saving settings...")
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

        app.logger.debug("Settings saved successfully.")
        return jsonify({"message": "Settings saved"})

    except Exception as e:
        app.logger.error(f"Error saving settings: {e}")
        return jsonify({"error": str(e)}), 500

def add_project(request):
    try:
        app.logger.debug("Adding new project...")
        data = request.json
        projectName = data.get('projectName')
        projectInfo = data.get('projectInfo')

        # Read existing settings from the JSON file
        with open(file_p, 'r') as json_file:
            existing_settings = json.load(json_file)

        # Find the maximum id in the existing settings
        max_id = max(item['id'] for item in existing_settings) if existing_settings else 0
        id = max_id + 1

        # Create a new project with the provided name and the next id
        new_project = {
            "id": id,
            "checked": False,
            "editable": True,
            "info": projectInfo,
            "name": projectName
        }

        # Add the new project to the existing settings
        existing_settings.append(new_project)

        # Save the updated settings to the JSON file
        with open(file_p, 'w') as json_file:
            json.dump(existing_settings, json_file, indent=2)

        # Load tests
        with open(tests_p, 'r') as file:
            data = json.load(file)
        # Add new project to tests
        data["proj" + str(id)] = {}
        with open(tests_p, 'w') as file:
            json.dump(data, file)

        # Load models
        with open(models_p, 'r') as file:
            data = json.load(file)

        # Create a new project entry with empty translations and model_url
        new_model_entry = {
            "model_url": "",
            "translations": {}
        }
        # Add new project to models
        data["proj" + str(id)] = new_model_entry
        with open(models_p, 'w') as file:
            json.dump(data, file)

        app.logger.debug("New project added successfully.")
        return jsonify({"message": "New project added successfully"})

    except Exception as e:
        app.logger.error(f"Error adding new project: {e}")
        return jsonify({"error": str(e)}), 500
    
def delete_project(request):
    try:
        app.logger.debug("Deleting project...")
        # Get the project ID from the request
        project_id_to_delete = request.json.get('id')

        # Read existing settings from the JSON file
        with open(file_p, 'r') as json_file:
            existing_settings = json.load(json_file)

        # Check if the project with the given ID exists
        project_to_delete = next((item for item in existing_settings if item['id'] == project_id_to_delete), None)

        if not project_to_delete:
            app.logger.error("Project not found.")
            return jsonify({"error": "Project not found, check config file (admin_settings.json)"}), 404

        # Remove the project from the existing settings
        existing_settings.remove(project_to_delete)

        # Save the updated settings to the JSON file
        with open(file_p, 'w') as json_file:
            json.dump(existing_settings, json_file, indent=2)

        # Remove tests associated with the deleted project
        with open(tests_p, 'r') as file:
            data = json.load(file)
        del data["proj" + str(project_id_to_delete)]
        with open(tests_p, 'w') as file:
            json.dump(data, file)

        # Remove models associated with the deleted project
        with open(models_p, 'r') as file:
            data = json.load(file)
        del data["proj" + str(project_id_to_delete)]
        with open(models_p, 'w') as file:
            json.dump(data, file)

        app.logger.debug("Project deleted successfully with all tests and models.")
        return jsonify({"message": "Project deleted successfully"})

    except Exception as e:
        app.logger.error(f"Error deleting project: {e}")
        return jsonify({"error": str(e)}), 500

def get_tests():
    with open(tests_p, 'r') as tests_file:
        tests_data = json.load(tests_file)
    return jsonify(tests_data)

def update_tests(request):
    # Get the test data from the request
    tests = request.json['tests']

    # Write the test data to a JSON file
    with open(tests_p, 'w') as json_file:
        json.dump(tests, json_file)

    app.logger.debug("Tests updated successfully.")
    return jsonify({"message": "Tests updated successfully"})

def get_model_config(request):
    with open(models_p, 'r') as models_file:
        models_data = json.load(models_file)
    return jsonify(models_data)

def update_models(request):
    # Get the models data from the request
    models = request.json['models']

    # Write the models data to a JSON file
    with open(models_p, 'w') as json_file:
        json.dump(models, json_file)

    app.logger.debug("Models updated successfully.")
    return jsonify({"message": "Models updated successfully"})
