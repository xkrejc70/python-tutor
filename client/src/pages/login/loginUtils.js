import axios from 'axios';
import api from 'ServerConfig'

export const handleLoginRequest = (username, password, setStatus, login, navigate) => {
    // Prepare the data to be sent to the server
    const data = {
        username: username,
        password: password,
    };

    // Send login request to the server
    axios.post(api.LOGIN, data)
        .then(response => {
            if (response.status === 200) {
                setStatus('Logged in successfully!');
                login();
                navigate("/settings");
            } else {
                setStatus(`Error: ${response.data}`);
            }
        })
        .catch(error => {
            if (error.response) {
                setStatus(`Error: ${error.response.data.error}`);
            } else if (error.request) {
                setStatus('Error: No response received from the server');
            } else {
                setStatus(`Error: ${error.message}`);
            }
        });
};
