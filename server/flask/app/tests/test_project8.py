from app import app
from app.tests.test_utils import RestrictedEnvironment, Project, Function
from app.tests.test_utils import import_function_from_file, clean_function_string
import inspect
import builtins
import re
import requests

# Test project 8
def test_project8(file_path, test_data):
    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    # ============= Test first_with_given_key =============
    p8_first_with_given_key = import_function_from_file(file_path, Function.FIRST_WITH_GIVEN_KEY)
    tests = test_data.get(Project.P8, {}).get(Function.FIRST_WITH_GIVEN_KEY, [])

    if p8_first_with_given_key[1] != 200:
        comment.append(p8_first_with_given_key[0])
    else:
        for test_case in tests:
            input_data = test_case.get('in')
            expected_output = test_case.get('out')
            input_key_str = test_case.get('key')
            input_key = getattr(builtins, input_key_str, lambda x: x)

            num_tests += 1
            try:
                with RestrictedEnvironment():
                    result = p8_first_with_given_key[0](input_data, key=input_key)
                    all_items = [item for item in result]
                    if all_items == expected_output:
                        passed += 1
                    else:
                        comment.append(f"Test case failed: {input_data}. Expected {expected_output}, but got {all_items}.")
            except Exception as e:
                comment.append("Error: " + str(e))

    # Model evaluation
    function_string = clean_function_string(p8_first_with_given_key[0])

    if len(function_string) > 1000:
        model_response.append("[ERROR]: Over limit")
    else:
        url = 'http://localhost:5050/proj8'
        data = {'input_string': function_string}


        response = requests.post(url, json=data)
        model_response.append(response.json()['classification'])

    if num_tests == passed:
        comment.append("Success: All tests passed without errors.")

    # ============= Final evaluation =============
    evaluation = {
        "comment": list(set(comment)),
        "model_response": model_response,
        "num_tests": num_tests,
        "passed": passed
    }
    
    return evaluation