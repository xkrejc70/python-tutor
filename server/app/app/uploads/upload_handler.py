from app import app
from flask import jsonify
from werkzeug.utils import secure_filename
import os

from app.uploads.uploads_config import UploadsConfig
from app.tests.example.test_example import test_example

# Config
app.config.from_object(UploadsConfig)

# Allowed file type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Check and Save file to project folder
def upload_handler(request):
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
            file_path = os.path.join(project_folder, filename)
            # TODO: if exists, rename (keep all uploaded projects)
            file.save(file_path)

            # Run tests
            test_result = test_example(file_path)

            response_data = {
                "success": True,
                "message": "File successfully uploaded.",
                "test": test_result,
            }
            app.logger.debug('File successfully uploaded')
            return jsonify(response_data), 200
        except Exception as e:
            app.logger.error(f"Error during file upload: {str(e)}")
            return jsonify({"error": "An error occurred during file upload."}), 500