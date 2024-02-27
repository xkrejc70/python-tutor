// uploadUtils.js
import axios from 'axios';

export const handleFileUpload = (selectedFile, selectedProject, setStatus, navigate) => {
    if (selectedFile && selectedProject) {
        const formData = new FormData();
        formData.append('file', selectedFile);
        formData.append('project', selectedProject);

        const config = {
            headers: { 'content-type': 'multipart/form-data' }
        }

        axios.post("http://localhost:5005/api/upload", formData, config)
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
    } else {
        setStatus(`Please select a file to upload.`);
    }
};

export const fetchProjectsFromServer = (setProjects, setSelectedProject) => {
    // Fetch projects from Flask API
    axios.get("http://localhost:5005/api/projects")
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
