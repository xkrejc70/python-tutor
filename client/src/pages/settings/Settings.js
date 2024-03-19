import React, { useState, useEffect } from 'react';
import Sidebar from "components/Sidebar";
import StatusMessage from "components/StatusMessage";
import TestEditor from "components/TestEditor";
import { fetchDataFromAPI, handleCheckboxChange, handleSaveData, handleAddProjectRequest, handleDeleteProjectRequest, getTests } from './settingsUtils';
import { RiErrorWarningFill } from "react-icons/ri";
import { AiFillDelete, AiFillLock } from "react-icons/ai";
import { TbMinusVertical } from "react-icons/tb";
import { FcOk } from "react-icons/fc";

import "assets/global.css";

function Settings() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [items, setItems] = useState([]);
    const [tests, setTests] = useState([]);
    const [selectedItems, setSelectedItems] = useState([]);
    const [status, setStatus] = useState('');
    const [statusTests, setStatusTests] = useState('');
    const [statusAddProject, setStatusAddProject] = useState('');
    const [projectName, setProjectName] = useState('');
    const [projectInfo, setProjectInfo] = useState('');

    const scrollToAddProject = () => {
        window.scrollTo(0, document.body.scrollHeight);
    };

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    useEffect(() => {
        fetchDataFromAPI(setItems, setSelectedItems, setStatus);
        getTests(setTests, setStatusTests);
    }, []);

    const handleCheckboxChangeWrapper = (item) => {
        handleCheckboxChange(item, items, setItems, setSelectedItems);
    };

    const handleSave = () => {
        handleSaveData(selectedItems, setStatus);
    };

    const handleDeleteProject = (item) => {
        handleDeleteProjectRequest(item, setItems, setSelectedItems, setStatus);
        // Update tests state after deleting project
        if (Array.isArray(tests)) {
            const updatedTests = tests.filter(test => test.projectId !== item.id);
            setTests(updatedTests);
        }
    }

    const handleAddProject = () => {
        handleAddProjectRequest(projectName, projectInfo, setStatusAddProject, setItems, setSelectedItems, setStatus, setProjectName, setProjectInfo, setTests, setStatusTests);
    };

    const handleTestsChange = (updatedTests) => {
        // Update the tests state when changes occur in the TestEditor
        setTests(updatedTests);
    };

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className="main-layout" style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Settings</h1>
                <br />

                <div className="settings-container">
                    <h3 className="h3-center">Choose projects for Evaluation</h3>
                    <br />

                    <table className="tests-table">
                        <thead>
                            <tr className='align-l'>
                                <th className='checkbox-td'>Project</th>
                                <th></th>
                                <th>Description</th>
                                <th className='align-r'></th>
                            </tr>
                        </thead>
                        <tbody>
                            {items.map(item => (
                                <tr key={item.id}>
                                    <td className='checkbox-td'><input
                                        className="checkbox-input"
                                        type="checkbox"
                                        checked={item.checked}
                                        onChange={() => handleCheckboxChangeWrapper(item)}
                                    /></td>
                                    <td>{item.name}</td>
                                    <td>{item.info}</td>
                                    <td className='align-r'>
                                        {item.editable ? (
                                            <span>
                                                <span>
                                                    {!item.tests_exist ? (
                                                        <span>No tests <RiErrorWarningFill size={23} /></span>
                                                    ) : (
                                                        <span>Tests ok <FcOk size={23} /></span>
                                                    )}
                                                </span>
                                                <TbMinusVertical size={23} />
                                                <span className="modify-test delete-text" onClick={() => handleDeleteProject(item)}>
                                                    <AiFillDelete size={23} />
                                                </span>
                                            </span>
                                        ) : (
                                            <span className='modify-test-lock'>
                                            {!item.tests_exist && (
                                                <span><AiFillLock size={23} /></span>
                                            )}
                                        </span>
                                        )}
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    <br />


                    <div className='save-button'>
                        <button onClick={handleSave}>Save changes</button>
                        <StatusMessage status={status} className="status-message" />
                    </div>
                </div>

                <div className="settings-container">
                    <h3 className="h3-center">Add new Project</h3>
                    <br />
                    <label>Project name:</label>
                    <input
                        type="projectName"
                        className="input-field"
                        id="projectName"
                        value={projectName}
                        onChange={(e) => setProjectName(e.target.value)}
                    />

                    <label>Project description (optional):</label>
                    <input
                        type="projectInfo"
                        className="input-field"
                        id="projectInfo"
                        value={projectInfo}
                        onChange={(e) => setProjectInfo(e.target.value)}
                    />

                    <div className='save-button'>
                        <button onClick={handleAddProject}>Add Project</button>
                        <StatusMessage status={statusAddProject} className="status-message" />
                    </div>
                </div>

                <h1>Tests</h1>

                <div className="settings-container">
                    <h3 className="h3-center">View and Edit Tests</h3>
                    <br />
                    <TestEditor tests={tests} projs={items} onTestsChange={handleTestsChange} />
                </div>

                <h1>Classification Model</h1>
                <p>todo</p>

                <h1>Tips</h1>
                <p>todo</p>

            </div>
        </div>
    );
}

export default Settings;
