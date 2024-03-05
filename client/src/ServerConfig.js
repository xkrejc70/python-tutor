const LOCALHOST = 'http://localhost:8084';
const PRODUCTION_API_BASE_URL = 'http://147.229.8.129:8084';
const API_BASE_URL = PRODUCTION_API_BASE_URL;
const API_VERSION = '';

//TODO: add api version
export default {
  API_BASE_URL,
  //PROJECTS_ENDPOINT: `${API_BASE_URL}/api/${API_VERSION}/projects`,
  // Get
  GET_PROJECTS: `${API_BASE_URL}/api/projects`,
  GET_QUESTIONS: `${API_BASE_URL}/api/questions`,
  // Post
  UPLOAD_PROJECT: `${API_BASE_URL}/api/upload`,
  LOGIN: `${API_BASE_URL}/api/admin/login`,
  SAVE_SETTINGS: `${API_BASE_URL}/api/admin/save`,
};