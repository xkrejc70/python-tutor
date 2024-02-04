from app import app
from app.tests.test_utils import RestrictedEnvironment, Project, Function
from app.tests.test_utils import import_function_from_file, clean_function_string
from app.tests.openai_api import model
import inspect
import re
import requests

# Test project 4
def test_project4(file_path, test_data):
    passed = 0
    num_tests = 0
    comment = []

    # ============= Test match_permutations_substrings =============
    # TODO: rewrite to proj4
    p8_first_with_given_key = import_function_from_file(file_path, Function.FIRST_WITH_GIVEN_KEY)
    tests = test_data.get(Project.P8, {}).get(Function.FIRST_WITH_GIVEN_KEY, [])

    if p8_first_with_given_key[1] != 200:
        comment.append(p8_first_with_given_key[0])
    else:
        for test_case in tests:
            input_data = test_case.get('in')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with RestrictedEnvironment():
                    result = p8_first_with_given_key[0](input_data, key=len)
                    all_items = [item for item in result]
                    if all_items == expected_output:
                        passed += 1
            except Exception as e:
                comment.append(str(e))

    # ============= Model evaluation =============
    function_string = inspect.getsource(p8_first_with_given_key[0])

    model_response = "no hint"
    function_string = clean_function_string(p8_first_with_given_key[0])

    if len(function_string) > 1000:
        model_response = "[ERROR]: Over limit"
    else:
        url = 'http://localhost:5050/proj8'
        data = {'input_string': function_string}

        # dev
        data = """
            def first_with_given_key(iterable, key = lambda x: x):
                seen = set()
                for x in iterable:
                    if repr(key(x)) not in seen:
                        seen.add(repr(key(x)))
                        yield x
                """

        response = requests.post(url, json=data)
        model_response = response.json()

    # ============= Final evaluation =============
    evaluation = {
        "comment": list(set(comment)),
        "model_response": model_response,
        "num_tests": num_tests,
        "passed": passed
    }
    
    return evaluation
