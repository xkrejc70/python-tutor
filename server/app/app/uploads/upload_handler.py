from app import app
from flask import jsonify
from werkzeug.utils import secure_filename
import os
import re

from app.uploads.uploads_config import UploadsConfig
from app.tests.test_handler import test

# Config
app.config.from_object(UploadsConfig)

# Allowed file type
# TODO: unittest
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# TODO: move to uplaod utils
# TODO: unittest
def check_filename(filename, project):
    # Define the regex pattern for the filename
    pattern = re.compile(r'^isj_proj[1-9]_x[a-zA-Z]{5}\d{2}\.py$')
    expected_project = f'{project}'

    # Check if the filename matches the pattern and the project is correct
    if re.match(pattern, filename) and expected_project in filename:
        return True
    else:
        return False

# Check and Save file to project folder
def upload_handler(request):
    if request.method == 'POST':
        # Check if the post request has all needed parts
        if 'file' not in request.files:
            app.logger.debug('No file part')
            return jsonify({"error": "File is required."}), 400
        file = request.files['file']
        
        if 'project' not in request.form:
            app.logger.debug('No project part')
            return jsonify({"error": "Project is required."}), 400
        project = request.form['project']        

        if file.filename == '':
            app.logger.debug('No selected file')
            return jsonify({"error": "No selected file."}), 400
        
        # Check for maximum content length
        if file.content_length > app.config['MAX_CONTENT_LENGTH']:
            return jsonify({"error": f"File size exceeds the maximum allowed limit of {app.config['MAX_CONTENT_LENGTH']} bytes."}), 400
        
        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file type. Only python (.py) files are allowed."}), 400

        # Check filename
        if not check_filename(file.filename, project):
            return jsonify({"error": "Wrong file name. Expected isj_projX_xlogin00.py"}), 400

        try:
            # Save uploaded file into project folder
            filename = secure_filename(file.filename)
            project_folder = os.path.join(app.config['UPLOAD_FOLDER'], project)
            os.makedirs(project_folder, exist_ok=True)
            file_path = os.path.join(project_folder, filename)
            # TODO: if exists, rename (keep all uploaded projects)
            file.save(file_path)
            app.logger.debug('File successfully uploaded')

            # Run tests move to different try
            test_result = test(file_path, project)

            response_data = {
                "success": True,
                "message": "File successfully uploaded.",
                "test": test_result,
            }
            return jsonify(response_data), 200
        except Exception as e:
            app.logger.error(f"Error during file upload: {str(e)}")
            return jsonify({"error": "An error occurred during file upload."}), 500