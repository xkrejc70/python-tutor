const LOCALHOST = 'http://localhost:8084';
const PRODUCTION_API_BASE_URL = 'http://147.229.8.129:8084';
const API_BASE_URL = LOCALHOST;
const API_VERSION = 'v1';

export default {
  API_BASE_URL,
  // Get
  GET_PROJECTS: `${API_BASE_URL}/api/${API_VERSION}/projects`,
  GET_QUESTIONS: `${API_BASE_URL}/api/${API_VERSION}/questions`,
  GET_TESTS: `${API_BASE_URL}/api/${API_VERSION}/admin/test/get`,
  GET_MODELS: `${API_BASE_URL}/api/${API_VERSION}/admin/model/get`,
  // Post
  UPDATE_TESTS: `${API_BASE_URL}/api/${API_VERSION}/admin/test/update`,
  UPDATE_MODELS: `${API_BASE_URL}/api/${API_VERSION}/admin/model/update`,
  UPLOAD_PROJECT: `${API_BASE_URL}/api/${API_VERSION}/upload`,
  LOGIN: `${API_BASE_URL}/api/${API_VERSION}/admin/login`,
  ADD_PROJECT: `${API_BASE_URL}/api/${API_VERSION}/admin/project/add`,
  DELETE_PROJECT: `${API_BASE_URL}/api/${API_VERSION}/admin/project/delete`,
  SAVE_SETTINGS: `${API_BASE_URL}/api/${API_VERSION}/admin/save`,
};
