from flask import Flask, jsonify, request
import logging_config
#from setfit import SetFitModel
import os
import json

# TODO: add logs

app = Flask(__name__)

def map_classification_result(prediction, classification_mapping):
    mapped_result = classification_mapping.get(prediction, "Classification translation is missing")
    return mapped_result

# Load project configurations from config file
file_p = os.path.join("config", "project_models.json")
with open(file_p, 'r') as f:
    project_config = json.load(f)

@app.route('/model/<string:project>', methods=['POST'])
def get_response(project):

    project_specific_config = project_config.get(project, {})
    # Extract project specific configuration
    translations = project_specific_config.get("translations", {})
    # Load model 
    model_url = project_specific_config.get("model_url", "")

    if model_url == "":
        app.logger.debug("No model for project " + project)
        return jsonify({
    })

    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Make classification using the loaded model
    #model = SetFitModel.from_pretrained(model_url)
    #numerical_prediction = model([input_string])
    numerical_prediction = '1'
    mapped_result = map_classification_result(numerical_prediction, translations)    

    # Extract predictions as needed
    result = {
        'input_string': input_string,
        'classification': mapped_result
    }

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)