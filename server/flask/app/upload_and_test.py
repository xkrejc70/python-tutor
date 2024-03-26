from app import app
from flask import jsonify
from app.uploads.upload_handler import upload_handler
from app.tests.test_handler import test

# Upload project and test it
def upload_and_test(request):
    upload_result = upload_handler(request)

    if upload_result[1] == 200:
        # File uploaded successfully

        file_path = upload_result[0]["file_path"]
        project = upload_result[0]["project"]
        file_content = upload_result[0]["file_content"]
        filename = upload_result[0]["filename"]

        try:
            # Test
            (test_result, analysis_result) = test(file_path, project)
            response_data = {
                "test_result": test_result,
                "analysis_result": analysis_result,
                "file_content": file_content,
                "filename": filename,
                "project": project
            }
            return jsonify(response_data), 200
      
        except Exception as e:
            app.logger.error(f"Error during test: {str(e)}")
            return jsonify({"error": f"An error occurred during test: {str(e)}"}), 500
    else:
        return upload_result