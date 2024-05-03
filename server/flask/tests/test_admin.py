import unittest
from app import app
from unittest.mock import MagicMock, patch
import json

class TestAdminFunctions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.open')  # Patch the open function to mock file operations
    def test_load_settings(self, mock_open):
        # Mock the return value of open function
        mock_open.side_effect = [
            MagicMock(return_value=json.dumps([{"id": 1, "name": "Project 1"}])),
            MagicMock(return_value=json.dumps({"proj1": {}}))
        ]

        response = self.app.get('/api/v1/projects')
        self.assertEqual(response.status_code, 200)

    @patch('app.open')  # Patch the open function to mock file operations
    def test_save_settings(self, mock_open):
        # Mock the return value of open function
        mock_open.side_effect = [
            MagicMock(return_value=json.dumps([{"id": 1, "name": "Project 1"}])),
            MagicMock(return_value=None)
        ]

        data = {"id": 1, "name": "Project 1"}
        response = self.app.post('/api/v1/admin/save', json=data)
        self.assertEqual(response.status_code, 200)

    @patch('app.open')  # Patch the open function to mock file operations
    def test_add_project(self, mock_open):
        # Mock the return value of open function
        mock_open.side_effect = [
            MagicMock(return_value=json.dumps([{"id": 1, "name": "Project 1"}])),
            MagicMock(return_value=None),
            MagicMock(return_value=json.dumps({})),
            MagicMock(return_value=None),
            MagicMock(return_value=json.dumps({})),
            MagicMock(return_value=None)
        ]

        data = {"projectName": "New Project", "projectInfo": "Info"}
        response = self.app.post('/api/v1/admin/project/add', json=data)
        self.assertEqual(response.status_code, 200)

    @patch('app.open')  # Patch the open function to mock file operations
    def test_delete_project(self, mock_open):
        # Mock the return value of open function
        mock_open.side_effect = [
            MagicMock(return_value=json.dumps([{"id": 1, "name": "Project 1"}])),
            MagicMock(return_value=None),
            MagicMock(return_value=json.dumps({})),
            MagicMock(return_value=None),
            MagicMock(return_value=json.dumps({})),
            MagicMock(return_value=None)
        ]

        data = {"id": 1}
        response = self.app.post('/api/v1/admin/project/delete', json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
