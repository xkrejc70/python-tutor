from app import app
from app.tests.test_utils import RestrictedEnvironment, Project, Function, Classes
from app.tests.test_utils import import_function_or_class_from_file, load_tips_from_yaml

# Test project 6
def test_project6(file_path, test_data, project):
    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    def run_init_tests(test_type, parse_func):
        nonlocal num_tests
        nonlocal passed
        nonlocal comment

        p6_polynomial = import_function_or_class_from_file(file_path, Classes.POLYNOMIAL)
        tests = test_data.get(Project.P6, {}).get(test_type, [])

        if p6_polynomial[1] != 200:
            comment.append(p6_polynomial[0])
        else:
            for test_case in tests:
                input_data_str = test_case.get('in')
                expected_output = test_case.get('out')

                input_data = parse_func(input_data_str)

                num_tests += 1
                try:
                    with RestrictedEnvironment():
                        if test_type == Classes.POLYNOMIAL_TUPLE:
                            result = p6_polynomial[0](*input_data)
                        elif test_type == Classes.POLYNOMIAL_KEY:
                            result = p6_polynomial[0](**input_data)
                        elif test_type == Classes.POLYNOMIAL_LIST:
                            result = p6_polynomial[0](input_data)
                        str_result = str(result)
                        if str_result == expected_output:
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {input_data}.\nExpected {expected_output}, but got {str_result}.")
                except Exception as e:
                    comment.append("Error: " + str(e))
            
    def run_ops_tests(test_op):
        nonlocal num_tests
        nonlocal passed
        nonlocal comment

        p6_polynomial = import_function_or_class_from_file(file_path, Classes.POLYNOMIAL)

        if p6_polynomial[1] != 200:
            comment.append(p6_polynomial[0])
        else:
            try:
                with RestrictedEnvironment():
                    if test_op == Classes.POLYNOMIAL_EQ:
                        num_tests += 1
                        pol1 = p6_polynomial[0]([1, 2, 3, 4, 5, 6])
                        pol2 = p6_polynomial[0]([1, 2, 3, 4, 5, 6])
                        if pol1 == pol2:
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                    elif test_op == Classes.POLYNOMIAL_ADD:
                        pol1 = p6_polynomial[0](x2=3, x0=1)
                        pol2 = p6_polynomial[0](x1=1, x3=0)
                        num_tests += 1
                        if str(pol1+pol2) == "3x^2 + x + 1":
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                        num_tests += 1
                        if str(pol2+pol1) == "3x^2 + x + 1":
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                    elif test_op == Classes.POLYNOMIAL_POW:
                        pol1 = str(p6_polynomial[0]([1, 1, 1]) ** 2)
                        pol2 = str(p6_polynomial[0](x0=-1, x1=1) ** 2)
                        num_tests += 1
                        if pol1 == "x^4 + 2x^3 + 3x^2 + 2x + 1":
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                        num_tests += 1
                        if pol2 == "x^2 - 2x + 1":
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                    elif test_op == Classes.POLYNOMIAL_DERIVATE:
                        pol1 = str(p6_polynomial[0](x2=1).derivative())
                        pol2 = str(p6_polynomial[0](x3=2,x1=3,x0=2).derivative().derivative())
                        pol3 = str(p6_polynomial[0](x0=1, x1=2, x2=3, x3=4).derivative())
                        pol4 = str(p6_polynomial[0](x3=2, x1=3, x0=2).derivative())
                        num_tests += 1
                        if pol1 == "2x":
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                        num_tests += 1
                        if pol2 == "12x":
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                        num_tests += 1
                        if pol3 == "12x^2 + 6x + 2":
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                        num_tests += 1
                        if pol4 == "6x^2 + 3":
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                    elif test_op == Classes.POLYNOMIAL_AT_VALUE:
                        pol1 = p6_polynomial[0](-2, 3, 4, -5).at_value(0)
                        pol2 = p6_polynomial[0](x2=3, x0=-1, x1=-2).at_value(3)
                        pol3 = p6_polynomial[0]([1, 0, -2]).at_value(-2.4)
                        pol4 = p6_polynomial[0]([1, 0, -2]).at_value(-1, 3.6)
                        num_tests += 1
                        if pol1 == -2:
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                        num_tests += 1
                        if pol2 == 20:
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                        num_tests += 1
                        if pol3 == -10.52:
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
                        num_tests += 1
                        if pol4 == -23.92:
                            passed += 1
                        else:
                            comment.append(f"Test case failed: {test_op}.")
            except Exception as e:
                comment.append("Error: " + str(e))



    # ============= Test Polynomial init =============
    run_init_tests(Classes.POLYNOMIAL_TUPLE, lambda x: tuple(map(int, x.split(','))))
    run_init_tests(Classes.POLYNOMIAL_KEY, lambda x: {key.strip(): int(value.strip()) for key, value in (item.split('=') for item in x.split(','))})
    run_init_tests(Classes.POLYNOMIAL_LIST, lambda x: x)

    run_ops_tests(Classes.POLYNOMIAL_EQ)
    run_ops_tests(Classes.POLYNOMIAL_ADD)
    run_ops_tests(Classes.POLYNOMIAL_POW)
    run_ops_tests(Classes.POLYNOMIAL_DERIVATE)
    run_ops_tests(Classes.POLYNOMIAL_AT_VALUE)

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