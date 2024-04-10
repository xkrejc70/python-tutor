from app import app
import json
import requests
from app.tests.test_utils import Url, load_tips_from_yaml

def test_project(file_path, test_data, project):
    passed = 0
    num_tests = 0
    comment = []
    model_response = []

    data = {
        "file_path": file_path,
        "test_data": test_data,
        "project": project
    }

    app.logger.debug(f"Calling test for {project}.")

    response = requests.post(Url.TEST + '/test', json=data)
    result = response.json()

    # Extract values from the result
    comment = result.get("comment", [])
    model_response = result.get("model_response", [])
    num_tests = result.get("num_tests", 0)
    passed = result.get("passed", 0)

    app.logger.debug(f"Test results: {comment}, {model_response}, {passed}/{num_tests}.")

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
    
    return evaluation
