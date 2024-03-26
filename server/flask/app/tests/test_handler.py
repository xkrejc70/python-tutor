from app import app
import json
import yaml
import os

from app.tests.static_analysis import run_code_analysis
from app.tests.test_project4 import test_project4
from app.tests.test_project5 import test_project5
from app.tests.test_project6 import test_project6
from app.tests.test_project8 import test_project8
from app.tests.test_project import test_project

TESTS = 'test_data.json'
CONFIG = 'config'

# Define paths to test data files
TEST_P = os.path.join(CONFIG, TESTS)

# Function to run tests for a specific project
def run_tests_for_project(file_path, project, test_data, test_data_special):
    # Hard coded tests for specific projects
    test_functions = {
        'proj4': test_project4,
        'proj5': test_project5,
        'proj6': test_project6,
        # 'proj7': test_project7,
        'proj8': test_project8
    }

    # Determine which test data to use based on the project
    if project in test_functions:
        function_tests = test_data
    else:
        function_tests = test_data_special

    app.logger.debug('Running tests for ' + file_path + ' on project with id ' + project)

    # Get the test function corresponding to the project, defaulting to test_project if not found
    test_function = test_functions.get(project, test_project)
    return test_function(file_path, function_tests, project)

# Main test function
def test(file_path, project):
    project_tests = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_p = os.path.join(script_dir, 'test_data.yaml')

    # Load YAML test data file
    with open(file_p, 'r') as file:
        test_data = yaml.safe_load(file)

    # Load JSON test data file
    with open(TEST_P, 'r') as file:
        test_data_special = json.load(file)

    # If project-specific tests exist, get them
    if project in test_data_special:
        project_tests = test_data_special[project]

    # Run tests for the specified project
    result = run_tests_for_project(file_path, project, test_data, project_tests)

    analysis_result = run_code_analysis(file_path)

    return (result, analysis_result)
