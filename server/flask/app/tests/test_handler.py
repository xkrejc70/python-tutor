from app import app
import yaml
import json
import os
from app.tests.test_project4 import test_project4
from app.tests.test_project6 import test_project6
from app.tests.test_project8 import test_project8
from app.tests.test_project import test_project

TESTS = 'test_data.json'
CONFIG = 'config'

tests_p = os.path.join(CONFIG, TESTS)

def run_tests_for_project(file_path, project, test_data, test_data_special):
    test_functions = {
        'proj4': test_project4,
        # 'proj5': test_project5,
        'proj6': test_project6,
        # 'proj7': test_project7,
        'proj8': test_project8
    }

    if project in test_functions:
        function_tests = test_data
    else:
        function_tests = test_data_special

    app.logger.debug('Running tests for ' + file_path + ' on project with id ' + project)

    # Get test project function
    test_function = test_functions.get(project, test_project)
    return test_function(file_path, function_tests, project)

def test(file_path, project):
    project_tests = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_p = os.path.join(script_dir, 'test_data.yaml')

    with open(file_p, 'r') as file:
        test_data = yaml.safe_load(file)

    with open(tests_p, 'r') as file:
        test_data_special = json.load(file)

    if project in test_data_special:
        project_tests = test_data_special[project]

    result = run_tests_for_project(file_path, project, test_data, project_tests)

    return result