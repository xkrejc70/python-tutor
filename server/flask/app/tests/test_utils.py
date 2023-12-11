import importlib.util
import sys

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

# Functions
class Function:
    CAMEL_TO_SNAKE_CASE = 'camel_to_snake_case'
    NOT_BOTH_TITLES = 'not_both_titles'

# Import function from file
def import_function_from_file(file_path, function_name):
    spec = importlib.util.spec_from_file_location("custom_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if hasattr(module, function_name):
        return getattr(module, function_name), 200
    else:
        return (f"The function '{function_name}' does not exist in the uploaded file."), 500