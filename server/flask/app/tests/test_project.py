from app import app
import json
from app.tests.test_utils import RestrictedEnvironment
from app.tests.test_utils import import_function_or_class_from_file, load_tips_from_yaml, convert_data

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

                    expected_output = convert_data(expected_output, output_type)

                    if expected_output == result:
                        passed += 1
                    else:
                        app.logger.debug(f"Test case failed: {input_data}. Expected {expected_output}, but got {result}.")
                        comment.append(f"Test case failed: {input_data}. Expected {expected_output}, but got {result}.")
            except Exception as e:
                comment.append(str(e))

    # ============= Final evaluation =============
    if num_tests == passed and passed != 0:
        comment.append("All tests passed without errors.")
        app.logger.debug(f"All tests passed without errors.")

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
