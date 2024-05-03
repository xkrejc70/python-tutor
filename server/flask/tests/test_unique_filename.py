import unittest
import os
from app.uploads.upload_utils import generate_unique_filename

class TestGenerateUniqueFilename(unittest.TestCase):
    def test_unique_filename(self):
        # Create a temporary directory for testing
        test_dir = "test_files"
        os.makedirs(test_dir, exist_ok=True)

        # Create a test file
        with open(os.path.join(test_dir, "test_file.txt"), "w") as f:
            f.write("Test file")

        # Generate unique filenames
        unique_filename_1 = generate_unique_filename(test_dir, "test_file.txt")
        unique_filename_2 = generate_unique_filename(test_dir, "test_file.txt")
        
        # Test that generated filenames are unique
        self.assertNotEqual(unique_filename_1, unique_filename_2)

        # Cleanup: Remove the temporary directory
        os.remove(os.path.join(test_dir, "test_file.txt"))
        os.rmdir(test_dir)

    def test_filename_format(self):
        test_dir = "test_files"
        os.makedirs(test_dir, exist_ok=True)

        # Generate a unique filename
        unique_filename = generate_unique_filename(test_dir, "test_file.txt")

        # Check that the filename has correct format
        self.assertTrue(unique_filename.startswith("test_file_"))

        # Cleanup: Remove the temporary directory
        os.remove(os.path.join(test_dir, unique_filename))
        os.rmdir(test_dir)

if __name__ == '__main__':
    unittest.main()
