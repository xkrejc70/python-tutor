from app import app
from flask import jsonify
from datetime import datetime
from werkzeug.utils import secure_filename
import os

from app.uploads.uploads_config import UploadsConfig
from app.uploads.upload_utils import generate_unique_filename, check_filename, allowed_file, to_camel_case

# Config
app.config.from_object(UploadsConfig)

# Check and Save file to project folder, run tests
def upload_handler(request):
    try:
        app.logger.debug("Received upload request.")
        
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

            if 'projectName' not in request.form:
                app.logger.debug('No projectName part')
                return jsonify({"error": "Project name is required."}), 400
            projectName = to_camel_case(request.form['projectName'])

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

            # Save uploaded file into project folder
            filename = secure_filename(file.filename)
            current_year = datetime.now().year
            
            project_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(current_year), projectName)
            os.makedirs(project_folder, exist_ok=True)

            # Generate a unique filename
            unique_filename = generate_unique_filename(project_folder, filename)

            file_path = os.path.join(project_folder, unique_filename)

            # Save the file
            file.save(file_path)
            app.logger.debug('File successfully uploaded - ' + unique_filename)

            # Read the content of the uploaded file and save it to 'file_content'
            with open(file_path, 'r') as f:
                file_content = f.read()

            return {
                "file_path": file_path,
                "project": project,
                "file_content": file_content,
                "filename": file.filename
            }, 200
    except Exception as e:
        app.logger.error(f"Error during file upload: {str(e)}")
        return jsonify({"error": "An error occurred during file upload."}), 500
