import importlib.util
import sys
import inspect
import re

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

# Import function or class from file
def import_function_or_class_from_file(file_path, identifier_name):
    spec = importlib.util.spec_from_file_location("custom_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if hasattr(module, identifier_name):
        imported_class = getattr(module, identifier_name)
        return imported_class, 200
    else:
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

    return function_string