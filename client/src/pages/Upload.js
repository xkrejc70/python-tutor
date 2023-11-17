import React, { useState } from 'react';
import axios from 'axios';
import Sidebar from "components/Sidebar";
// css
import "assets/global.css";

function Upload() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [selectedProject, setSelectedProject] = useState('project1');

    // TODO: move to utils
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

            axios.post("/api/upload", formData, config)
                .then(response => {
                    // Handle success
                    console.log(response.data);
                })
                .catch(error => {
                    // Handle error
                    console.error(error);
                });
        } else {
            // Handle case when no file is selected
            // TODO: set text bellow upload button "please select file"
            console.warn('Please select a file to upload.');
        }
    };

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>
                    Upload
                </h1>
                <br/>
                <div>
                    <input type="file" onChange={onFileChange} />
                    
                    <select value={selectedProject} onChange={handleProjectChange}>
                        <option value="project1">Project 1</option>
                        <option value="project2">Project 2</option>
                    </select>
                    
                    <button onClick={onFileUpload}>
                        Upload!
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Upload;