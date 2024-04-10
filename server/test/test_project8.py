from flask import jsonify
import test_utils as tu
import builtins
import requests

# Test project 8
def test_project8(request):
    data = request.json
    file_path = data.get('file_path')
    test_data = data.get('test_data')
    project = data.get('project')

    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    # ============= Test first_with_given_key =============
    p8_first_with_given_key = tu.import_function_or_class_from_file(file_path, tu.Function.FIRST_WITH_GIVEN_KEY)
    tests = test_data.get(tu.Project.P8, {}).get(tu.Function.FIRST_WITH_GIVEN_KEY, [])

    if p8_first_with_given_key[1] != 200:
        comment.append(f"Function {tu.Function.FIRST_WITH_GIVEN_KEY} not found")
    else:
        for test_case in tests:
            input_data = test_case.get('in')
            expected_output = test_case.get('out')
            input_key_str = test_case.get('key')
            input_key = getattr(builtins, input_key_str, lambda x: x)

            num_tests += 1
            try:
                with tu.RestrictedEnvironment():
                    result = p8_first_with_given_key[0](input_data, key=input_key)
                    all_items = [item for item in result]
                    if all_items == expected_output:
                        passed += 1
                    else:
                        #comment.append(f"Test case failed: {input_data}.\nExpected {expected_output}, but got {all_items}.")
                        comment.append(f"Test case failed: {input_data}.\nExpected {expected_output}.")
            except Exception as e:
                comment.append("Test failed")

        # Model evaluation
        function_string = tu.clean_function_string(p8_first_with_given_key[0])

        if len(function_string) > 1000:
            model_response.append("[ERROR]: Over limit")
        else:
            url = tu.Url.MODEL + '/model/' + project
            data = {'input_string': function_string}

            response = requests.post(url, json=data)
            response_json = response.json()
            if 'classification' in response_json:
                model_response.append(response_json['classification'])
            else:
                model_response = []

    result = {
        "comment": comment,
        "num_tests": num_tests,
        "passed": passed,
        "model_response": model_response
    }

    return jsonify(result)