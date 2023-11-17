from flask import Flask, jsonify, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import socket
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# api
@app.route("/api", methods=['GET'])
def return_home():
    return jsonify({"host": "Hostname: " + socket.gethostname()})

# Upload
# TODO: move to diff file.py
@app.route("/api/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if the post request has all needed parts
        if 'file' not in request.files:
            app.logger.debug('No file part')
            return jsonify({"error": "File is required."}), 400
        
        if 'project' not in request.form:
            app.logger.debug('No project part')
            return jsonify({"error": "Project is required."}), 400
        
        file = request.files['file']
        project = request.form['project']

        if file.filename == '':
            app.logger.debug('No selected file')
            return jsonify({"error": "No selected file."}), 400
        
        # Check for maximum content length
        if file.content_length > app.config['MAX_CONTENT_LENGTH']:
            return jsonify({"error": f"File size exceeds the maximum allowed limit of {app.config['MAX_CONTENT_LENGTH']} bytes."}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type. Only python (.py) files are allowed."}), 400

        try:
            # Save uploaded file into project folder
            filename = secure_filename(file.filename)
            project_folder = os.path.join(app.config['UPLOAD_FOLDER'], project)
            os.makedirs(project_folder, exist_ok=True)
            file.save(os.path.join(project_folder, filename))

            response_data = {
                "success": True,
                "message": "File successfully uploaded."
            }
            app.logger.debug('File successfully uploaded')
            return jsonify(response_data), 200
        except Exception as e:
            app.logger.error(f"Error during file upload: {str(e)}")
            return jsonify({"error": "An error occurred during file upload."}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)