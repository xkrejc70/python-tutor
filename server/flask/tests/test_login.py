import unittest
import json
import os
from unittest.mock import patch, MagicMock
from flask import Flask, request, jsonify
from app import app, load_credentials, authenticate

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.test_credentials = {
            'username': 'test_user',
            'password': 'test_password'
        }
        self.test_config_data = {'credentials': self.test_credentials}
        self.test_file_p = 'test_admin_config.json'

    def tearDown(self):
        if os.path.exists(self.test_file_p):
            os.remove(self.test_file_p)

    def test_load_credentials(self):
        # Create a test admin_config.json file with test credentials
        with open(self.test_file_p, 'w') as json_file:
            json.dump(self.test_config_data, json_file)

        # Call the load_credentials function
        credentials = load_credentials(self.test_file_p)

        # Check if the loaded credentials match the test credentials
        self.assertEqual(credentials, self.test_credentials)

    def test_authenticate_successful(self):
        # Mock the request object
        request.json = MagicMock(return_value={'username': 'test_user', 'password': 'test_password'})

        # Mock the load_credentials function to return test credentials
        with patch('app.load_credentials') as mock_load_credentials:
            mock_load_credentials.return_value = self.test_credentials

            # Call the authenticate function with mocked request
            response = authenticate(request)

            # Check if authentication was successful
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"message": "Login successful"})

    def test_authenticate_invalid_credentials(self):
        # Mock the request object
        request.json = MagicMock(return_value={'username': 'wrong_user', 'password': 'wrong_password'})

        # Mock the load_credentials function to return test credentials
        with patch('app.load_credentials') as mock_load_credentials:
            mock_load_credentials.return_value = self.test_credentials

            # Call the authenticate function with mocked request
            response = authenticate(request)

            # Check if authentication failed due to invalid credentials
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {"error": "Invalid username or password"})

if __name__ == '__main__':
    unittest.main()
