from flask import Flask, jsonify, request
import logging_config
#TODO:production
#from setfit import SetFitModel
import os
import json

app = Flask(__name__)

# Load project configurations from config file
file_p = os.path.join("config", "project_models.json")

def map_classification_result(prediction, classification_mapping):
    mapped_result = classification_mapping.get(prediction, "Classification translation is missing")
    return mapped_result

def load_models():
    with open(file_p, 'r') as f:
        project_config = json.load(f)

    models = {}
    for project, config in project_config.items():
        model_url = config.get("model_url", "")
        if model_url:
            app.logger.debug("Loading model for project " + project)
            model = SetFitModel.from_pretrained(model_url)
            models[project] = model
    return models

# Load models at startup
#app.models = load_models()

def get_model(project):
    return app.models.get(project)

@app.route('/model/<string:project>', methods=['POST'])
def get_response(project): 
    """
    model = get_model(project)
    if not model:
        app.logger.debug("No model found for project " + project)
        return jsonify({})
    """

    data = request.json
    input_string = data.get('input_string', '')

    app.logger.debug("Getting classification for project " + project)
    #predictions = model([input_string])
    #numerical_prediction = predictions.item()
    numerical_prediction = 1

    with open(file_p, 'r') as f:
        project_config = json.load(f)

    project_specific_config = project_config.get(project, {})
    translations = project_specific_config.get("translations", {})
    translations = {int(key): value for key, value in translations.items()}

    mapped_result = map_classification_result(numerical_prediction, translations)

    result = {
        'input_string': input_string,
        'classification': mapped_result
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
