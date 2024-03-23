import axios from 'axios';
import api from 'ServerConfig';

export const updateTestsAndSave = (updatedTests, onTestsChange) => {
    // Update tests and save to server
    onTestsChange(updatedTests);

    // Send data to the server API
    axios.post(api.UPDATE_TESTS, {
        tests: updatedTests
    })
    .then(response => {
        console.log('Data updated successfully:', response.data);
    })
    .catch(error => {
        console.error('Error updating data:', error);
    });
};

export const updateModelsandSave = (updatedModels, onModelsChange) => {
    // Update tests and save to server
    onModelsChange(updatedModels);

    // Send data to the server API
    axios.post(api.UPDATE_MODELS, {
        models: updatedModels
    })
    .then(response => {
        console.log('Data updated successfully:', response.data);
    })
    .catch(error => {
        console.error('Error updating data:', error);
    });
};
