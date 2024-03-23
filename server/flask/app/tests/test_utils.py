from app import app
import importlib.util
import sys
import inspect
import re
import yaml
import os

MODELS = 'tips.yaml'
CONFIG = 'config'

# Restricted execution environment by temporarily clearing and restoring sys.modules
class RestrictedEnvironment:
    def __enter__(self):
        # Backup sys.modules to avoid polluting the global namespace
        self.original_modules = dict(sys.modules)
        sys.modules.clear()

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore the original sys.modules
        sys.modules.clear()
        sys.modules.update(self.original_modules)

# Projects
class Project:
    P1 = 'proj1'
    P2 = 'proj2'
    P3 = 'proj3'
    P4 = 'proj4'
    P5 = 'proj5'
    P6 = 'proj6'
    P7 = 'proj7'
    P8 = 'proj8'

# Classes
class Classes:
    POLYNOMIAL = 'Polynomial'
    POLYNOMIAL_TUPLE = 'Polynomial_init_tuple'
    POLYNOMIAL_KEY = 'Polynomial_init_key'
    POLYNOMIAL_LIST = 'Polynomial_init_list'
    POLYNOMIAL_EQ = 'Polynomial_eq'
    POLYNOMIAL_ADD = 'Polynomial_add'
    POLYNOMIAL_POW = 'Polynomial_pow'
    POLYNOMIAL_DERIVATE = 'Polynomial_derivate'
    POLYNOMIAL_AT_VALUE = 'Polynomial_at_value'

# Functions
class Function:
    CAMEL_TO_SNAKE_CASE = 'camel_to_snake_case'
    NOT_BOTH_TITLES = 'not_both_titles'
    # proj4
    MATCH_PERMUTATIONS_SUBSTRINGS = 'match_permutations_substrings'
    UNIQ_SRT = 'uniq_srt'
    UNIQ_ORIG_ORDER = 'uniq_orig_order'
    # proj8
    FIRST_WITH_GIVEN_KEY = 'first_with_given_key'

# Model
class Model:
    URL = 'http://localhost:5050'

# Import function or class from file
def import_function_or_class_from_file(file_path, identifier_name):
    spec = importlib.util.spec_from_file_location("custom_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if hasattr(module, identifier_name):
        imported_class = getattr(module, identifier_name)
        return imported_class, 200
    else:
        app.logger.debug('The function or class ' +identifier_name + ' does not exist in the uploaded file.')
        return (f"The function or class '{identifier_name}' does not exist in the uploaded file."), 500
    
# Clean the source code of a given function by removing comments, empty lines, and trailing whitespaces.
def clean_function_string(func):
    # Get the source code of the function
    function_string = inspect.getsource(func)

    # Remove single-line comments
    function_string = re.sub(r'#.*', '', function_string)

    # Remove multi-line comments (enclosed in triple double-quotes)
    function_string = re.sub(r'(""".*?""")', '', function_string, flags=re.DOTALL)

    # Remove trailing whitespaces at the end of each line
    function_string = re.sub(r'\s+$', '', function_string, flags=re.MULTILINE)

    # Remove empty lines
    function_string = re.sub(r'\n\s*\n', '\n', function_string)

    # Remove the first line (function definition)
    function_string = '\n'.join(function_string.split('\n')[1:])

    return function_string

def load_tips_from_yaml(project, category):
    file_p = os.path.join(CONFIG, MODELS)
    with open(file_p, 'r') as file:
        tips_data = yaml.safe_load(file)
    
    # Check if the project and category exist in the loaded data
    if project in tips_data and category in tips_data[project]:
        return tips_data[project][category]
    
    return None

def convert_data(data, data_type):
    if data_type == "string":
        return data
    elif data_type == "list":
        return eval(data)
    elif data_type == "integer":
        return int(data)
    elif data_type == "float":
        return float(data)
    elif data_type == "tuple":
        # Assuming data is provided as a string representation of a tuple, e.g., "(1, 2, 3)"
        return tuple(map(int, data.strip('()').split(',')))
    elif data_type == "dictionary":
        # Assuming data is provided as a JSON string representing a dictionary
        return data
    elif data_type == "boolean":
        if data.lower() in ['true', 'false']:
            return data.lower() == 'true'
        else:
            raise ValueError("Invalid boolean value")
    else:
        raise ValueError("Unsupported data type")