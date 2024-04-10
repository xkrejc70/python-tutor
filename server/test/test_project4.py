from flask import jsonify
import test_utils as tu
import requests

# Test Project 4
def test_project4(request):
    data = request.json
    file_path = data.get('file_path')
    test_data = data.get('test_data')
    project = data.get('project')

    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    # ============= Test match_permutations_substrings =============
    p4_match_permutations_substrings = tu.import_function_or_class_from_file(file_path, tu.Function.MATCH_PERMUTATIONS_SUBSTRINGS)
    tests = test_data.get(tu.Project.P4, {}).get(tu.Function.MATCH_PERMUTATIONS_SUBSTRINGS, [])

    if p4_match_permutations_substrings[1] != 200:
        comment.append(f"Function {tu.Function.MATCH_PERMUTATIONS_SUBSTRINGS} not found")
    else:
        for test_case in tests:
            string = test_case.get('string')
            words = test_case.get('words')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with tu.RestrictedEnvironment():
                    result = p4_match_permutations_substrings[0](string, words)
                    all_items = [item for item in result]
                    if sorted(all_items) == sorted(expected_output):
                        passed += 1
                    else:
                        comment.append(f"Test case failed (match_permutations_substrings): {string, words}.\nExpected {expected_output}")
                        #comment.append(f"Test case failed (match_permutations_substrings): {string, words}.\nExpected {expected_output}, but got {all_items}.")
            except Exception as e:
                comment.append("Test failed")

        # Model evaluation
        function_string = tu.clean_function_string(p4_match_permutations_substrings[0])

        if len(function_string) > 3000:
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

    # ============= Test uniq_srt =============
    p4_uniq_srt = tu.import_function_or_class_from_file(file_path, tu.Function.UNIQ_SRT)
    tests = test_data.get(tu.Project.P4, {}).get(tu.Function.UNIQ_SRT, [])

    if p4_uniq_srt[1] != 200:
        comment.append(f"Function {tu.Function.UNIQ_SRT} not found")
    else:
        for test_case in tests:
            input = test_case.get('in')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with tu.RestrictedEnvironment():
                    result = p4_uniq_srt[0](input)
                    all_items = [item for item in result]
                    if sorted(all_items) == sorted(expected_output):
                        passed += 1
                    else:
                        comment.append(f"Test case failed (uniq_srt): {input}.\nExpected {expected_output}")
                        #comment.append(f"Test case failed (uniq_srt): {input}.\nExpected {expected_output}, but got {all_items}.")
            except Exception as e:
                comment.append("Test failed")

        # Model evaluation
        function_string = tu.clean_function_string(p4_uniq_srt[0])

        if len(function_string) > 3000:
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

    # ============= Test uniq_orig_order =============
    p4_uniq_orig_order = tu.import_function_or_class_from_file(file_path, tu.Function.UNIQ_ORIG_ORDER)
    tests = test_data.get(tu.Project.P4, {}).get(tu.Function.UNIQ_ORIG_ORDER, [])

    if p4_uniq_orig_order[1] != 200:
        comment.append(f"Function {tu.Function.UNIQ_ORIG_ORDER} not found")

    else:
        for test_case in tests:
            input = test_case.get('in')
            expected_output = test_case.get('out')

            num_tests += 1
            try:
                with tu.RestrictedEnvironment():
                    result = p4_uniq_orig_order[0](input)
                    all_items = [item for item in result]
                    if sorted(all_items) == sorted(expected_output):
                        passed += 1
                    else:
                        comment.append(f"Test case failed (uniq_orig_order): {input}.\nExpected {expected_output}")
                        #comment.append(f"Test case failed (uniq_orig_order): {input}.\nExpected {expected_output}, but got {all_items}.")
            except Exception as e:
                comment.append("Test failed")

        # Model evaluation
        function_string = tu.clean_function_string(p4_uniq_orig_order[0])

        if len(function_string) > 3000:
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