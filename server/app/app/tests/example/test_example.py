from app import app
from app.tests.utils.file_importer import import_function_from_file

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
        evaluation = "success"
    else:
        evaluation = "bad result, try different solution"
    
    return evaluation