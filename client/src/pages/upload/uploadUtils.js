import axios from 'axios';
import api from 'ServerConfig'

export const handleFileUpload = (selectedFile, selectedProject, setStatus, navigate, projects) => {
    if (selectedFile && selectedProject) {
        // Find the project object based on the selected project ID
        const selectedProjectObj = projects.find(project => 'proj' + project.id.toString() === selectedProject);

        if (selectedProjectObj) {
            const projectName = selectedProjectObj.name;

            const formData = new FormData();
            formData.append('file', selectedFile);
            formData.append('project', selectedProject);
            formData.append('projectName', projectName);

            const config = {
                headers: { 'content-type': 'multipart/form-data' }
            }

            axios.post(api.UPLOAD_PROJECT, formData, config)
                .then(response => {
                    if (response.status === 200) {
                        setStatus('File uploaded successfully!');
                        navigate("/evaluation", { state: { test: response.data } });
                    } else {
                        setStatus(`Error: ${response.data}`);
                    }
                })
                .catch(error => {
                    if (error.response) {
                        setStatus(`Error: ${error.response.data.error}`);
                    } else {
                        setStatus(`Error: ${error.response.data}`);
                    }
                });
        }
    } else {
        setStatus(`Please select a file to upload.`);
    }
};

export const fetchProjectsFromServer = (setProjects, setSelectedProject) => {
    // Fetch projects from Flask API
    axios.get(api.GET_PROJECTS)
        .then(response => {
            const checkedProjects = response.data.filter(project => project.checked === true);
            setProjects(checkedProjects);

            if (checkedProjects.length > 0) {
                setSelectedProject('proj' + checkedProjects[0].id.toString());
            }
        })
        .catch(error => {
            console.error('Error fetching projects:', error);
        });
};
