// Upload.js
import React, { useState, useEffect } from 'react';
import Sidebar from "components/Sidebar";
import StatusMessage from "components/StatusMessage";
import { useNavigate } from 'react-router-dom';
import { handleFileUpload, fetchProjectsFromServer } from './uploadUtils';
import "assets/global.css";

function Upload() {
    const navigate = useNavigate();

    const [selectedFile, setSelectedFile] = useState(null);
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [projects, setProjects] = useState([]);
    const [selectedProject, setSelectedProject] = useState('');
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
        handleFileUpload(selectedFile, selectedProject, setStatus, navigate);
    };

    // Load projects from server settings
    useEffect(() => {
        fetchProjectsFromServer(setProjects, setSelectedProject);
    }, []);

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Project Submission</h1>
                <br />
                <div className="upload-container">
                    <h3 className='h3-center'>Upload your project</h3>
                    <br />
                    <StatusMessage status={status} />
                    <div className="upload-form">
                        <input type="file" onChange={onFileChange} />
                        <select value={selectedProject} onChange={handleProjectChange}>
                            {projects.map(project => (
                                <option key={project.id} value={'proj' + project.id.toString()}>{project.name}</option>
                            ))}
                        </select>
                        <button onClick={onFileUpload}>Upload</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Upload;
