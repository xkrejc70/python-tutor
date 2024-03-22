from app import app
import json
from app.tests.test_utils import RestrictedEnvironment, Project, Function
from app.tests.test_utils import import_function_or_class_from_file, clean_function_string, load_tips_from_yaml


def convert_data(data, data_type):
    if data_type == "string":
        return data
    elif data_type == "list":
        return eval(data)
    elif data_type == "integer":
        return int(data)
    elif data_type == "float":
        return float(data)
    elif data_type == "tuple":
        # Assuming data is provided as a string representation of a tuple, e.g., "(1, 2, 3)"
        return tuple(map(int, data.strip('()').split(',')))
    elif data_type == "dictionary":
        # Assuming data is provided as a JSON string representing a dictionary
        return data
    elif data_type == "boolean":
        if data.lower() in ['true', 'false']:
            return data.lower() == 'true'
        else:
            raise ValueError("Invalid boolean value")
    else:
        raise ValueError("Unsupported data type")

def test_project(file_path, test_data, project):
    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    for function_name, test_cases in test_data.items():
        try:
            # Import the function dynamically
            imported_function, status_code = import_function_or_class_from_file(file_path, function_name)
            if status_code != 200:
                raise Exception(imported_function)  # Raise exception if function import failed
        except Exception as e:
            comment.append(str(e))
            continue

        for test_case in test_cases:
            input_data = test_case.get('in')
            expected_output = test_case.get('out')
            input_type = test_case.get('inputType')
            output_type = test_case.get('outputType')

            num_tests += 1
            try:
                input_data = convert_data(input_data, input_type)

                with RestrictedEnvironment():
                    result = imported_function(input_data)

                    app.logger.debug(input_data)
                    app.logger.debug(result)
                    app.logger.debug(expected_output)

                    expected_output = convert_data(expected_output, output_type)

                    if expected_output == result:
                        passed += 1
                    else:
                        comment.append(f"Test case failed: {input_data}. Expected {expected_output}, but got {result}.")
            except Exception as e:
                comment.append(str(e))

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
    # ============= Final evaluation =============
    evaluation = {
        "num_tests": num_tests,
        "passed": passed,
        "comment": list(set(comment))
    }
    
    return evaluation
