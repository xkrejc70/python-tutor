from app import app
from flask import request
from app.upload_and_test import upload_and_test
from app.admin.settings import load_settings, save_settings, add_project, delete_project, get_tests, update_tests, get_model_config, update_models
from app.admin.login import authenticate
from app.questions.questions import get_questions

# Define API version
API_VERSION = 'v1'
API_BASE_URL = f'/api/{API_VERSION}'


############ API ENDPOINTS ############

@app.route(f'{API_BASE_URL}/questions/<string:project>', methods=['GET'])
def get_questions_route(project):
    return get_questions(project)

@app.route(f'{API_BASE_URL}/upload', methods=['GET', 'POST'])
def upload():
    return upload_and_test(request)

@app.route(f'{API_BASE_URL}/projects', methods=['GET'])
def get_items():
    return load_settings()

# todo: secure admin requests
@app.route(f'{API_BASE_URL}/admin/test/get', methods=['GET'])
def admin_test_get():
    return get_tests()

@app.route(f'{API_BASE_URL}/admin/test/update', methods=['POST'])
def admin_test_update():
    return update_tests(request)

@app.route(f'{API_BASE_URL}/admin/save', methods=['POST'])
def admin_save():
    return save_settings(request)

@app.route(f'{API_BASE_URL}/admin/login', methods=['POST'])
def admin_login():
    return authenticate(request)

@app.route(f'{API_BASE_URL}/admin/project/add', methods=['POST'])
def admin_project_add():
    return add_project(request)

@app.route(f'{API_BASE_URL}/admin/project/delete', methods=['POST'])
def admin_project_delete():
    return delete_project(request)

@app.route(f'{API_BASE_URL}/admin/model/get', methods=['GET'])
def admin_model_get():
    return get_model_config(request)

@app.route(f'{API_BASE_URL}/admin/model/update', methods=['POST'])
def admin_model_update():
    return update_models(request)
