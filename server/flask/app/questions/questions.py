from app import app
from flask import jsonify
import yaml
import os

def get_questions(project):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'questions.yaml')
    
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    if project in data:
        return jsonify(data[project])
    else:
        # Handle the case when the specified project is not found
        return jsonify([])