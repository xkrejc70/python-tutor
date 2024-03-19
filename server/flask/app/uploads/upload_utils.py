from app import app
import os
import re

# Function to generate a unique filename with iteration number
def generate_unique_filename(project_folder, filename):
    # Extract the base filename and extension
    base_name, ext = os.path.splitext(filename)
    
    iteration = 1
    while True:
        unique_filename = f"{base_name}_{iteration:02d}{ext}"
        file_path = os.path.join(project_folder, unique_filename)
        
        # Check if the filename already exists
        if not os.path.exists(file_path):
            return unique_filename
        iteration += 1

# TODO: unittest
# Check filename format
def check_filename(filename, project):
    return True
    # Define the regex pattern for the filename
    pattern = re.compile(r'^isj_proj[1-9]_x[a-zA-Z]{5}\d{2}\.py$')
    expected_project = f'{project}'

    # Check if the filename matches the pattern and the project is correct
    if re.match(pattern, filename) and expected_project in filename:
        return True
    else:
        return False
    
# Allowed file type
# TODO: unittest
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']