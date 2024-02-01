from flask import Flask, jsonify
from model_utils import save_locally

app = Flask(__name__)

@app.route('/predict')
def predict():
    # Your Hugging Face model prediction logic here
    # (replace with actual code based on your model)
    save_locally()

    prediction = {"result": "Model saved"}
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)