import React, { useState } from 'react';
import axios from 'axios';
import Sidebar from "components/Sidebar";
import { useNavigate } from 'react-router-dom';
import "assets/global.css";

function Upload() {
    const navigate = useNavigate();

    const [selectedFile, setSelectedFile] = useState(null);
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [selectedProject, setSelectedProject] = useState('proj1');
    const [status, setStatus] = useState('');

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    const handleProjectChange = (event) => {
        setSelectedProject(event.target.value);
    };

    const onFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const onFileUpload = () => {
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

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Project Submission</h1>
                <br />
                <div className="upload-container">
                    <h3 className='h3-center'>Upload your project</h3>
                    <br />
                    {status && <p className={`status`}>{status}</p>}
                    <div className="upload-form">
                        <input type="file" onChange={onFileChange} />
                        <select value={selectedProject} onChange={handleProjectChange}>
                            <option value="proj1">Project 1</option>
                            <option value="proj4">Project 4</option>
                            <option value="proj6">Project 6</option>
                            <option value="proj8">Project 8</option>
                        </select>
                        <button onClick={onFileUpload}>Upload</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Upload;
