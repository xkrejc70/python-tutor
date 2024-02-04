from flask import Flask, jsonify, request
from model_utils import save_locally

app = Flask(__name__)

"""
@app.route('/proj8', methods=['POST'])
def proj8():
    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Extract predictions as needed
    result = {
        'input_string': input_string,
        'classification': "Set"
    }

    return jsonify(result)
"""



"""
"""
from setfit import SetFitModel

def map_classification_result(prediction, classification_mapping):
    mapped_result = classification_mapping.get(prediction, "Unknown Class")
    return mapped_result


# ============= PROJECT 4 =============

# Load the pre-trained models saved locally
model_proj4 = SetFitModel.from_pretrained("hojzas/proj4-match_permutations_substrings-lab1")

# Feedback
classification_mapping_proj4 = {
    0: "Use specific set operation for more efficient and readable solution.",
    1: "Perfect solution.",
}

@app.route('/proj4', methods=['POST'])
def proj4():
    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Make classification using the loaded model
    predictions = model_proj4([input_string])

    print(predictions)

    numerical_prediction = predictions.item()
    mapped_result = map_classification_result(numerical_prediction, classification_mapping_proj4)

    # Extract predictions as needed
    result = {
        'input_string': input_string,
        'classification': mapped_result
    }

    return jsonify(result)


# ============= PROJECT 8 =============

# Load the pre-trained models saved locally
model_proj8 = SetFitModel.from_pretrained("hojzas/proj8-lab2")

# Feedback
classification_mapping_proj8 = {
    0: "List",
    1: "Set",
    2: "Dictionary",
}

@app.route('/proj8', methods=['POST'])
def proj8():
    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Make classification using the loaded model
    predictions = model_proj8([input_string])

    print(predictions)

    numerical_prediction = predictions.item()
    mapped_result = map_classification_result(numerical_prediction, classification_mapping_proj8)

    # Extract predictions as needed
    result = {
        'input_string': input_string,
        'classification': mapped_result
    }

    return jsonify(result)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)