from flask import Flask, jsonify, request
import requests
import test_utils
from test_project4 import test_project4
from test_project5 import test_project5
from test_project6 import test_project6
from test_project8 import test_project8
from test_project_urls import test_project_urls

app = Flask(__name__)

@app.route('/test/proj4', methods=['POST'])
def test_proj4():
    return test_project4(request)

@app.route('/test/proj5', methods=['POST'])
def test_proj5():
    return test_project5(request)

@app.route('/test/proj6', methods=['POST'])
def test_proj6():
    return test_project6(request)

@app.route('/test/proj8', methods=['POST'])
def test_proj8():
    return test_project8(request)

@app.route('/test/projurls', methods=['POST'])
def test_proj_urls():
    return test_project_urls(request)

@app.route('/test', methods=['POST'])
def test_proj():
    data = request.json
    
    file_path = data.get('file_path')
    test_data = data.get('test_data')
    project = data.get('project')

    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    for function_name, test_cases in test_data.items():
        try:
            # Import the function dynamically
            imported_function, status_code = test_utils.import_function_or_class_from_file(file_path, function_name)
            if status_code != 200:
                raise Exception(imported_function)  # Raise exception if function import failed
        except Exception as e:
            app.logger.debug(str(e))
            comment.append(f"Function {function_name} not found")
            num_tests += 1
            continue

        for test_case in test_cases:
            input_data = test_case.get('in')
            expected_output = test_case.get('out')
            input_type = test_case.get('inputType')
            output_type = test_case.get('outputType')

            num_tests += 1
            try:
                input_data = test_utils.convert_data(input_data, input_type)

                with test_utils.RestrictedEnvironment():
                    result = imported_function(input_data)

                    expected_output = test_utils.convert_data(expected_output, output_type)

                    if expected_output == result:
                        passed += 1
                    else:
                        app.logger.debug(f"Test case failed: {input_data}.Expected {expected_output}, but got {result}.")
                        #comment.append(f"Test case failed: {input_data}.\nExpected {expected_output}, but got {result}.")
                        comment.append(f"Test case failed: {input_data}.\nExpected {expected_output}")
            except Exception as e:
                app.logger.debug(str(e))
                comment.append("Test failed")

        # Model evaluation
        function_string = test_utils.clean_function_string(imported_function)

        if len(function_string) > 1000:
            model_response.append("[ERROR]: Over limit")
        else:
            url = test_utils.Url.MODEL + '/model/' + project
            data = {'input_string': function_string}

            app.logger.debug('Calling model for ' + project)

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


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5080)