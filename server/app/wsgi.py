from flask import Flask, jsonify
import socket

app = Flask(__name__)

# api
@app.route("/api")
def return_home():
    return jsonify({"host": "Hostname: " + socket.gethostname()})

if __name__ == "__main__":
    app.run(debug=True)