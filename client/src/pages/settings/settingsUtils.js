import axios from 'axios';
import api from 'ServerConfig'

export const fetchDataFromAPI = (setData, setSelectedItems, setStatus) => {
    fetch(api.GET_PROJECTS)
        .then(response => response.json())
        .then(data => {
            const updatedItems = data.map(item => ({
                ...item,
                checked: item.checked || false,
            }));
            setData(updatedItems);

            const initiallyCheckedItems = updatedItems.filter(item => item.checked);
            setSelectedItems(initiallyCheckedItems);
        })
        .catch(error => {
            setStatus('Error fetching project data');
        });
};

export const getTests = (setTests, setStatus) => {
    fetch(api.GET_TESTS)
        .then(response => response.json())
        .then(data => {
            setTests(data);
        })
        .catch(error => {
            setStatus('Error fetching test data');
        });
};

export const getModels = (setModels, setStatus) => {
    fetch(api.GET_MODELS)
        .then(response => response.json())
        .then(data => {
            setModels(data);
        })
        .catch(error => {
            setStatus('Error fetching model data');
        });
};

export const handleCheckboxChange = (item, items, setItems, setSelectedItems) => {
    const updatedItems = items.map(i => {
        if (i.id === item.id) {
            return { ...i, checked: !i.checked };
        }
        return i;
    });

    setItems(updatedItems);

    const updatedSelectedItems = updatedItems.filter(i => i.checked);
    setSelectedItems(updatedSelectedItems);
};

export const handleSaveData = (selectedItems, setStatus) => {
    const dataToSend = selectedItems.map(item => ({
        checked: item.checked,
        editable: item.editable,
        id: item.id,
        info: item.info,
        name: item.name,
    }));

    axios.post(api.SAVE_SETTINGS, dataToSend)
        .then(response => {
            if (response.status === 200) {
                setStatus('Settings saved');
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

export const handleAddProjectRequest = (projectName, projectInfo, setStatusAddProject, setItems, setSelectedItems, setStatus, setProjectName, setProjectInfo, setTests, setModels) => {
    if (projectName === "") {
        setStatusAddProject('Project name is required');
        return;
    }

    // Prepare the data to be sent to the server
    const data = {
        projectName: projectName,
        projectInfo: projectInfo,
    };

    axios.post(api.ADD_PROJECT, data)
        .then(response => {
            if (response.status === 200) {
                setStatus('New project added');
                fetchDataFromAPI(setItems, setSelectedItems, setStatus);
                getTests(setTests);
                getModels(setModels);
                setProjectName('');
                setProjectInfo('');
            } else {
                setStatusAddProject(`Error: ${response.data}`);
            }
        })
        .catch(error => {
            if (error.response) {
                setStatusAddProject(`Error: ${error.response.data.error}`);
            } else if (error.request) {
                setStatusAddProject('Error: No response received from the server');
            } else {
                setStatusAddProject(`Error: ${error.message}`);
            }
        });
};

export const handleDeleteProjectRequest = (item, setItems, setSelectedItems, setStatus, setTests, setModels) => {
    // Prepare the data to be sent to the server
    const data = {
        id: item.id,
    };

    // Send login request to the server
    axios.post(api.DELETE_PROJECT, data)
        .then(response => {
            if (response.status === 200) {
                setStatus('Project deleted');
                fetchDataFromAPI(setItems, setSelectedItems, setStatus);
                getTests(setTests);
                getModels(setModels);
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
}