from app import app
from app.tests.test_utils import RestrictedEnvironment, Project, Function, import_function_or_class_from_file

# TODO: delete folder above
# Test project 1
def test_project1(file_path, test_data):
    passed = 0
    num_tests = 0
    comment = []

    # ============= Test camel_to_snake_case =============
    p1_camel_to_snake_case = import_function_or_class_from_file(file_path, Function.CAMEL_TO_SNAKE_CASE)
    tests = test_data.get(Project.P1, {}).get(Function.CAMEL_TO_SNAKE_CASE, [])

    if p1_camel_to_snake_case[1] != 200:
        comment.append(p1_camel_to_snake_case[0])
    else:
        for test_case in tests:
            input_data = test_case.get('in')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with RestrictedEnvironment():
                    result = p1_camel_to_snake_case[0](input_data)
                    if result == expected_output:
                        passed += 1
            except Exception as e:
                comment.append(str(e))
                

    # ============= Test not_both_titles =============
    p1_not_both_titles = import_function_or_class_from_file(file_path, Function.NOT_BOTH_TITLES)
    tests = test_data.get(Project.P1, {}).get(Function.NOT_BOTH_TITLES, [])

    if p1_not_both_titles[1] != 200:
        comment.append(p1_not_both_titles[0])
    else:
        for test_case in tests:
            input_data = test_case.get('in')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with RestrictedEnvironment():
                    result = p1_not_both_titles[0](input_data)
                    if result == expected_output:
                        passed += 1
            except Exception as e:
                comment.append(str(e))

    # ============= Final evaluation =============
    evaluation = {
        "num_tests": num_tests,
        "passed": passed,
        "comment": list(set(comment))
    }
    
    return evaluation
