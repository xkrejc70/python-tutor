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

# ============= PROJECT 8 =============

save_locally()

# Load the pre-trained models saved locally
model_proj8 = SetFitModel.from_pretrained("./models/proj8/")

# Feedback
classification_mapping = {
    0: "List",
    1: "Set",
    2: "Dictionary",
}

def map_classification_result(prediction):
    mapped_result = classification_mapping.get(prediction, "Unknown Class")
    return mapped_result

@app.route('/proj8', methods=['POST'])
def proj8():
    # Get the input string from the request
    data = request.json
    input_string = data.get('input_string', '')

    # Make classification using the loaded model
    predictions = model_proj8([input_string])

    print(predictions)

    numerical_prediction = predictions.item()
    mapped_result = map_classification_result(numerical_prediction)

    # Extract predictions as needed
    result = {
        'input_string': input_string,
        'classification': mapped_result
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)