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
