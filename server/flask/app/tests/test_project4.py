from app import app
from app.tests.test_utils import RestrictedEnvironment, Project, Function
from app.tests.test_utils import import_function_or_class_from_file, clean_function_string, load_tips_from_yaml
import requests

# Test project 4
def test_project4(file_path, test_data, project):
    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    # ============= Test match_permutations_substrings =============
    p4_match_permutations_substrings = import_function_or_class_from_file(file_path, Function.MATCH_PERMUTATIONS_SUBSTRINGS)
    tests = test_data.get(Project.P4, {}).get(Function.MATCH_PERMUTATIONS_SUBSTRINGS, [])

    if p4_match_permutations_substrings[1] != 200:
        comment.append(p4_match_permutations_substrings[0])
    else:
        for test_case in tests:
            string = test_case.get('string')
            words = test_case.get('words')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with RestrictedEnvironment():
                    result = p4_match_permutations_substrings[0](string, words)
                    all_items = [item for item in result]
                    if sorted(all_items) == sorted(expected_output):
                        passed += 1
                    else:
                        comment.append(f"Test case failed (match_permutations_substrings): {string, words}. Expected {expected_output}, but got {all_items}.")
            except Exception as e:
                comment.append("Error: " + str(e))

        # Model evaluation
        function_string = clean_function_string(p4_match_permutations_substrings[0])

        if len(function_string) > 3000:
            model_response.append("[ERROR]: Over limit")
        else:
            url = 'http://localhost:5050/' + project
            data = {'input_string': function_string}

            response = requests.post(url, json=data)
            model_response.append('match_permutations_substrings: ' + response.json()['classification'])

    # ============= Test uniq_srt =============
    p4_uniq_srt = import_function_or_class_from_file(file_path, Function.UNIQ_SRT)
    tests = test_data.get(Project.P4, {}).get(Function.UNIQ_SRT, [])

    if p4_uniq_srt[1] != 200:
        comment.append(p4_uniq_srt[0])
    else:
        for test_case in tests:
            input = test_case.get('in')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with RestrictedEnvironment():
                    result = p4_uniq_srt[0](input)
                    all_items = [item for item in result]
                    if sorted(all_items) == sorted(expected_output):
                        passed += 1
                    else:
                        comment.append(f"Test case failed (uniq_srt): {input}. Expected {expected_output}, but got {all_items}.")
            except Exception as e:
                comment.append("Error: " + str(e))

        # Model evaluation
        function_string = clean_function_string(p4_uniq_srt[0])

        if len(function_string) > 3000:
            model_response.append("[ERROR]: Over limit")
        else:
            url = 'http://localhost:5050/' + project
            data = {'input_string': function_string}

            response = requests.post(url, json=data)
            model_response.append('uniq_srt: ' + response.json()['classification'])

    # ============= Test uniq_orig_order =============
    p4_uniq_orig_order = import_function_or_class_from_file(file_path, Function.UNIQ_ORIG_ORDER)
    tests = test_data.get(Project.P4, {}).get(Function.UNIQ_ORIG_ORDER, [])

    if p4_uniq_orig_order[1] != 200:
        comment.append(p4_uniq_orig_order[0])
    else:
        for test_case in tests:
            input = test_case.get('in')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with RestrictedEnvironment():
                    result = p4_uniq_orig_order[0](input)
                    all_items = [item for item in result]
                    if sorted(all_items) == sorted(expected_output):
                        passed += 1
                    else:
                        comment.append(f"Test case failed (uniq_orig_order): {input}. Expected {expected_output}, but got {all_items}.")
            except Exception as e:
                comment.append("Error: " + str(e))

        # Model evaluation
        function_string = clean_function_string(p4_uniq_orig_order[0])

        if len(function_string) > 3000:
            model_response.append("[ERROR]: Over limit")
        else:
            url = 'http://localhost:5050/' + project
            data = {'input_string': function_string}

            response = requests.post(url, json=data)
            model_response.append('uniq_orig_order: ' + response.json()['classification'])

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