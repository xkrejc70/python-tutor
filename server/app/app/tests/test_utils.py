import importlib.util

def import_function_from_file(file_path, function_name):
    spec = importlib.util.spec_from_file_location("custom_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if hasattr(module, function_name):
        return getattr(module, function_name)
    else:
        raise AttributeError(f"The function '{function_name}' does not exist in the uploaded file.")