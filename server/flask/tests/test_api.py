import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_questions_route(self):
        response = self.app.get('/api/v1/questions/project_name')
        self.assertEqual(response.status_code, 200)

    def test_upload_route(self):
        # Mock a file upload
        data = {'file': (open('test_file.txt', 'rb'), 'test_file.txt')}
        response = self.app.post('/api/v1/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)

    def test_get_items_route(self):
        response = self.app.get('/api/v1/projects')
        self.assertEqual(response.status_code, 200)

    # Add tests for other API endpoints similarly

if __name__ == '__main__':
    unittest.main()
