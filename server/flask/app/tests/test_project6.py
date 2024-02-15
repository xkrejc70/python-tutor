from app import app
from app.tests.test_utils import RestrictedEnvironment, Project, Function, Classes
from app.tests.test_utils import import_function_or_class_from_file, clean_function_string

# Test project 6
def test_project6(file_path, test_data):
    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    # ============= Test Polynomial =============
    p6_polynomial = import_function_or_class_from_file(file_path, Classes.POLYNOMIAL)
    tests = test_data.get(Project.P6, {}).get(Classes.POLYNOMIAL, [])

    if p6_polynomial[1] != 200:
        comment.append(p6_polynomial[0])
    else:
        for test_case in tests:
            input_data_str = test_case.get('in')
            input_data = [int(x) for x in input_data_str.split(',')]
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                app.logger.debug(p6_polynomial)
                with RestrictedEnvironment():
                    result = p6_polynomial[0](input_data)
                    str_result = str(result)
                    if str_result == expected_output:
                        passed += 1
                    else:
                        comment.append(f"Test case failed: {input_data}. Expected {expected_output}, but got {str_result}.")
            except Exception as e:
                comment.append("Error: " + str(e))

    """
    # Model evaluation
    function_string = clean_function_string(p6_polynomial[0])

    if len(function_string) > 1000:
        model_response.append("[ERROR]: Over limit")
    else:
        url = 'http://localhost:5050/proj8'
        data = {'input_string': function_string}


        response = requests.post(url, json=data)
        model_response.append(response.json()['classification'])
    """

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