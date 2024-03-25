from app import app
from app.tests.test_utils import RestrictedEnvironment, Project, Function, Model
from app.tests.test_utils import import_function_or_class_from_file, clean_function_string, load_tips_from_yaml
from copy import deepcopy
import inspect
import builtins
import re
import requests

# Test project 5
def test_project5(file_path, test_data, project):
    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    # ============= Test first_with_given_key =============
    p5_gen_quiz = import_function_or_class_from_file(file_path, Function.GEN_QUIZ)

    if p5_gen_quiz[1] != 200:
        comment.append(p5_gen_quiz[0])
    else:
        question_pool = [("Q1", ["A1", "A2", "A3"]), ("Q2", ["A1", "A2", "A3"]), ("Q3", ["A1", "A2", "A3"]), ("Q4", ["A1", "A2", "A3"]), ("Q5", ["A1", "A2", "A3"]),
                        ("Q6", ["A1", "A2", "A3", "A4"]), ("Q7", ["A1", "A2", "A3", "A4"]), ("Q8", ["A1", "A2", "A3", "A4", "A5"]),
                        ("Q9", ["A1", "A2", "A3", "A4", "A5"]),
                        ("Q10", ["A1", "A2", "A3", "A4", "A5", "A6"])]
        array_char_codes = ["1", "2", "3", "4", "5", "6"]
        string_number_codes = "123456"
        string_char_codes = "ABCDEF"
        
        # Indexes
        indexes1 = [0, 1, 2]
        indexes2 = [0, 1, 4]
        indexes3 = [-1, 2, -2]
        indexes4 = [1, 2, 9]
        indexes5 = [-9, 1, -2]
        indexes6 = [0, 0, 0]
        indexes7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        indexes8 = [1, 5, 7, -5, -2, 3]
        indexes9 = [9, -9]
        indexes10 = [1, -1]   

        existing_quiz_1 = [("EQ1", ["A1", "A2", "A3"]), ("EQ2", ["A1", "A2", "A3"]), ("EQ3", ["A1", "A2", "A3"])]
        existing_quiz_nummbers_1 = [("EQ1", ["1: A1", "2: A2", "3: A3"]), ("EQ2", ["1: A1", "2: A2", "3: A3"]), ("EQ3", ["1: A1", "2: A2", "3: A3"])]
        existing_quiz_indexes_1 = [("EQ1", ["A: A1", "B: A2", "C: A3"]), ("EQ2", ["A: A1", "B: A2", "C: A3"]), ("EQ3", ["A: A1", "B: A2", "C: A3"])]
    
        # Quiz
        quiz1 = [("Q1", ["1: A1", "2: A2", "3: A3"]), ("Q2", ["1: A1", "2: A2", "3: A3"]), ("Q3", ["1: A1", "2: A2", "3: A3"])]  # indexes1 + array_char_codes
        quiz2 = existing_quiz_nummbers_1 + [("Q1", ["1: A1", "2: A2", "3: A3"]), ("Q2", ["1: A1", "2: A2", "3: A3"]), ("Q5", ["1: A1", "2: A2", "3: A3"])]  # indexes2 + array_char_codes
        quiz3 = [("Q10", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5", "F: A6"]), ("Q3", ["A: A1", "B: A2", "C: A3"]), ("Q9", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5"])]  # indexes3 + string_char_codes
        quiz4 = [("Q2", ["1: A1", "2: A2", "3: A3"]), ("Q3", ["1: A1", "2: A2", "3: A3"]), ("Q10", ["1: A1", "2: A2", "3: A3", "4: A4", "5: A5", "6: A6"])]  # indexes4 + string_number_codes
        quiz5 = [("Q2", ["A: A1", "B: A2", "C: A3"]), ("Q2", ["A: A1", "B: A2", "C: A3"]), ("Q9", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5"])]  # indexes5 + string_char_codes
        quiz6 = existing_quiz_indexes_1 + [("Q1", ["A: A1", "B: A2", "C: A3"]), ("Q1", ["A: A1", "B: A2", "C: A3"]), ("Q1", ["A: A1", "B: A2", "C: A3"])]  # indexes6 + string_char_codes
        quiz7 = [("Q2", ["A: A1", "B: A2", "C: A3"]), ("Q3", ["A: A1", "B: A2", "C: A3"]), ("Q4", ["A: A1", "B: A2", "C: A3"]), ("Q5", ["A: A1", "B: A2", "C: A3"]),
                ("Q6", ["A: A1", "B: A2", "C: A3", "D: A4"]), ("Q7", ["A: A1", "B: A2", "C: A3", "D: A4"]), ("Q8", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5"]),
                ("Q9", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5"]), ("Q10", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5", "F: A6"])]  # indexes7 + string_char_codes
        quiz8 = [("Q2", ["A: A1", "B: A2", "C: A3"]), ("Q6", ["A: A1", "B: A2", "C: A3", "D: A4"]), ("Q8", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5"]),
                ("Q6", ["A: A1", "B: A2", "C: A3", "D: A4"]), ("Q9", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5"]), ("Q4", ["A: A1", "B: A2", "C: A3"])]  # indexes8 + string_char_codes
        quiz9 = [("Q10", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5", "F: A6"]), ("Q2", ["A: A1", "B: A2", "C: A3"])]  # indexes9 + string_char_codes
        quiz10 = [("Q2", ["A: A1", "B: A2", "C: A3"]), ("Q10", ["A: A1", "B: A2", "C: A3", "D: A4", "E: A5", "F: A6"])]  # indexes10 + string_char_codes
        
        try:
            with RestrictedEnvironment():

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes1, altcodes=array_char_codes)
                if result == quiz1:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes2, altcodes=array_char_codes, quiz=existing_quiz_nummbers_1)
                if result == quiz2:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes3, altcodes=string_char_codes)
                if result == quiz3:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes4, altcodes=string_number_codes)
                if result == quiz4:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes5, altcodes=string_char_codes)
                if result == quiz5:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes6, altcodes=string_char_codes, quiz=existing_quiz_indexes_1)
                if result == quiz6:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes7, altcodes=string_char_codes)
                if result == quiz7:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes8, altcodes=string_char_codes)
                if result == quiz8:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes9, altcodes=string_char_codes)
                if result == quiz9:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

                num_tests += 1
                result = p5_gen_quiz[0](deepcopy(question_pool), *indexes10, altcodes=string_char_codes)
                if result == quiz10:
                    passed += 1
                else:
                    comment.append(f"Test case failed: question_pool: {question_pool}, indexes: {indexes1}, altcodes: {string_char_codes}.\nExpected {quiz1}, but got {result}.")

        except Exception as e:
            comment.append("Error: " + str(e))

        # Model evaluation
        function_string = clean_function_string(p5_gen_quiz[0])

        if len(function_string) > 1000:
            model_response.append("[ERROR]: Over limit")
        else:
            url = Model.URL + '/model/' + project
            data = {'input_string': function_string}

            app.logger.debug('Calling model for ' + project)

            response = requests.post(url, json=data)
            response_json = response.json()
            if 'classification' in response_json:
                model_response.append(response_json['classification'])
            else:
                model_response = []

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