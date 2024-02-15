from app import app
import yaml
import os
from app.tests.proj1.test_project1 import test_project1
from app.tests.test_project8 import test_project8
from app.tests.test_project4 import test_project4

def not_found():
    return "test function not found"

def run_tests_for_project(file_path, project, tests):
    test_functions = {
        'proj1': test_project1,
        'proj4': test_project4,
        'proj8': test_project8
    }

    # Get test project function
    test_function = test_functions.get(project, not_found)
    return test_function(file_path, tests)

def test(file_path, project):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_p = os.path.join(script_dir, 'test_data.yaml')
    with open(file_p, 'r') as file:
        test_data = yaml.safe_load(file)

    result = run_tests_for_project(file_path, project, test_data)

    return result

    # TODO: jsonify({"state": "error"})