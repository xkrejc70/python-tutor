from app import app
from app.tests.test_utils import import_function_from_file

# TODO: load function name, inputs and output from test_example_config.py
# TODO: delete
# Example foo testing
def test_example(file_path):
    # Import functions for tests
    function_name = 'foo'
    evaluation = ""
    foo_function = import_function_from_file(file_path, function_name)

    # Test
    result = foo_function(7)
    app.logger.debug(f"Result of foo(14) from uploaded file: {result}")

    if result == 14:
        evaluation = {
            "comment": "some comment",
            "failed": 1,
            "passed": 4,
            "total": 5
        }
    else:
        evaluation = "bad result, try different solution"
    
    return evaluation