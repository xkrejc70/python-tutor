from app import app

from app.tests.proj1.test_proj1 import test_proj1

def test(file_path, project):

    function_name = f"test_{project}"

    if function_name in globals() and callable(globals()[function_name]):
        function_to_call = globals()[function_name]
        return function_to_call(file_path)
    else:
        return "No function found for project"