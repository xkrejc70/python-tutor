from flask import Flask, jsonify, request
import logging_config
#from setfit import SetFitModel
import os
import json

# TODO: add logs

app = Flask(__name__)

def map_classification_result(prediction, classification_mapping):
    mapped_result = classification_mapping.get(prediction, "Unknown Class")
    return mapped_result

# Load project configurations from config file
file_p = os.path.join("config", "project_models.json")
with open(file_p, 'r') as f:
    project_config = json.load(f)

@app.route('/model/<string:project>', methods=['POST'])
def get_response(project):

    # Extract project specific configuration
    translations = project_config.get(project, {})

    # Load model 
    #model_url = proj8_config.get("model_url", "")
    #model_proj8 = SetFitModel.from_pretrained(model_url)
    classification_mapping = translations.get("translations", {})

    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Make classification using the loaded model
    #numerical_prediction = model([input_string])
    numerical_prediction = '1'
    mapped_result = map_classification_result(numerical_prediction, classification_mapping)    

    # Extract predictions as needed
    result = {
        'input_string': input_string,
        'classification': mapped_result
    }

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)