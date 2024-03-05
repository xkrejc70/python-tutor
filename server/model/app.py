from flask import Flask, jsonify, request

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
        'classification': "[HARD-CODED] Use specific set operation for more efficient and readable solution."
    }

    return jsonify(result)


@app.route('/proj4', methods=['POST'])
def proj4():
    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Extract predictions as needed
    result = {
        'input_string': input_string,
        'classification': "[HARD-CODED] Explore a technique for quickly initializing a dictionary with default values for specified keys."
    }

    return jsonify(result)


"""

from setfit import SetFitModel

def map_classification_result(prediction, classification_mapping):
    mapped_result = classification_mapping.get(prediction, "Unknown Class")
    return mapped_result


# ============= PROJECT 4 =============

# Load the pre-trained models saved locally
model_proj4 = SetFitModel.from_pretrained("hojzas/proj4-all-labs")

# Feedback
classification_mapping_proj4 = {
    0: "Consider using specific set operation for more efficient and readable solution.",
    1: "Perfect solution.",
    2: "There is a simpler and more readable implementation approach.",
    3: "Consider using specific function to sort elements of an iterable.",
    4: "Perfect solution.",
    5: "Explore a technique for quickly initializing a dictionary with default values for specified keys.",
    6: "Perfect solution.",
}

@app.route('/proj4', methods=['POST'])
def proj4():
    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Make classification using the loaded model
    predictions = model_proj4([input_string])

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
    0: "Consider using a set instead of a list to improve efficiency, sets provide faster membership checks.",
    1: "Perfect solution.",
    2: "For unique key tracking, a set is more natural and efficient than storing key-value pairs in dictionary.",
}

@app.route('/proj8', methods=['POST'])
def proj8():
    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Make classification using the loaded model
    predictions = model_proj8([input_string])

    numerical_prediction = predictions.item()
    mapped_result = map_classification_result(numerical_prediction, classification_mapping_proj8)

    # Extract predictions as needed
    result = {
        'input_string': input_string,
        'classification': mapped_result
    }

    return jsonify(result)

"""
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)