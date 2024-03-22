from app import app
from app.tests.test_utils import RestrictedEnvironment, Project, Function, Model
from app.tests.test_utils import import_function_or_class_from_file, clean_function_string, load_tips_from_yaml
import inspect
import builtins
import re
import requests

# Test project 8
def test_project8(file_path, test_data, project):
    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    # ============= Test first_with_given_key =============
    p8_first_with_given_key = import_function_or_class_from_file(file_path, Function.FIRST_WITH_GIVEN_KEY)
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
            url = Model.URL + '/' + project
            data = {'input_string': function_string}

            app.logger.debug('Calling model for ' + project)

            response = requests.post(url, json=data)
            model_response.append(response.json()['classification'])

    # ============= Final evaluation =============
    if num_tests == passed and passed != 0:
        comment.append("All tests passed without errors.")

    # Tips
    practice_tips = load_tips_from_yaml(project, "practice")
    external_tips = load_tips_from_yaml(project, "external")

    # ============= Final evaluation =============
    evaluation = {
        "comment": list(set(comment)),
        "model_response": model_response,
        "num_tests": num_tests,
        "practice_tips": practice_tips,
        "external_tips": external_tips,
        "passed": passed
    }
    
    return evaluation