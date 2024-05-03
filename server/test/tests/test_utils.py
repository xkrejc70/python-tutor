import unittest
from unittest.mock import patch
import test_utils as tu

class TestImportFunctionOrClassFromFile(unittest.TestCase):
    def test_import_function_or_class_from_file_success(self):
        # Mocking spec_from_file_location
        with patch('importlib.util.spec_from_file_location') as mock_spec:
            # Mocking exec_module
            mock_module = mock_spec.return_value.loader.exec_module = unittest.mock.MagicMock()
            # Mocking getattr
            mock_getattr = unittest.mock.MagicMock(return_value=unittest.mock.MagicMock())
            
            # Call the function
            result = tu.import_function_or_class_from_file('file_path', 'identifier_name')
            
            # Assertions
            self.assertEqual(result[1], 200)
            mock_getattr.assert_called_once_with(mock_module, 'identifier_name')

    def test_import_function_or_class_from_file_failure(self):
        # Mocking spec_from_file_location
        with patch('importlib.util.spec_from_file_location') as mock_spec:
            # Mocking exec_module
            mock_module = mock_spec.return_value.loader.exec_module = unittest.mock.MagicMock()
            # Mocking getattr
            mock_getattr = unittest.mock.MagicMock(return_value=None)
            
            # Call the function
            result = tu.import_function_or_class_from_file('file_path', 'identifier_name')
            
            # Assertions
            self.assertEqual(result[1], 500)
            mock_getattr.assert_called_once_with(mock_module, 'identifier_name')

class TestCleanFunctionString(unittest.TestCase):
    def test_clean_function_string(self):
        # Test input function with comments, empty lines, and trailing whitespaces
        input_function = """
        def test_function():
            # This is a comment
            return True

        """
        expected_output = "return True"
        
        # Call the function
        result = tu.clean_function_string(input_function)
        
        # Assertion
        self.assertEqual(result.strip(), expected_output)

class TestConvertData(unittest.TestCase):
    def test_convert_data_string(self):
        # Test input string data
        data = "test"
        data_type = "string"
        expected_output = "test"
        
        # Call the function
        result = tu.convert_data(data, data_type)
        
        # Assertion
        self.assertEqual(result, expected_output)

    # Add more test cases for other data types

if __name__ == '__main__':
    unittest.main()
