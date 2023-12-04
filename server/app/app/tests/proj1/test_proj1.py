from app import app
from app.tests.test_utils import import_function_from_file


# TODO: load function name, inputs and output from test_example_config.py
# Test project 1
def test_proj1(file_path):
    return "good"
    # Import functions for tests
    # TODO: from json + in out
    p1_camel_to_snake_case = import_function_from_file(file_path, 'camel_to_snake_case')




    passed, failed = 0

    # Test 1
    result = p1_camel_to_snake_case('camelCaseNameAllowed')
    if result == 'camel_case_name_allowed':
        passed += 1
    else:
        failed += 1

    evaluation = {
        "comment": "brief comment about tests",
        "passed": passed,
        "failed": failed
    }
    
    return evaluation
