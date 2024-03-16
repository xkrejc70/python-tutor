const LOCALHOST = 'http://localhost:8084';
const PRODUCTION_API_BASE_URL = 'http://147.229.8.129:8084';
const API_BASE_URL = LOCALHOST;
const API_VERSION = '';

//TODO: add api version
export default {
  API_BASE_URL,
  //PROJECTS_ENDPOINT: `${API_BASE_URL}/api/${API_VERSION}/projects`,
  // Get
  GET_PROJECTS: `${API_BASE_URL}/api/projects`,
  GET_QUESTIONS: `${API_BASE_URL}/api/questions`,
  GET_TESTS: `${API_BASE_URL}/api/admin/test/get`,
  // Post
  UPDATE_TESTS: `${API_BASE_URL}/api/admin/test/update`,
  UPLOAD_PROJECT: `${API_BASE_URL}/api/upload`,
  LOGIN: `${API_BASE_URL}/api/admin/login`,
  ADD_PROJECT: `${API_BASE_URL}/api/admin/project/add`,
  DELETE_PROJECT: `${API_BASE_URL}/api/admin/project/delete`,
  SAVE_SETTINGS: `${API_BASE_URL}/api/admin/save`,
};
