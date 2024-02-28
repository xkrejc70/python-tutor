import React, { useState, useEffect } from 'react';
import Sidebar from "components/Sidebar";
import StatusMessage from "components/StatusMessage";
import { fetchDataFromAPI, handleCheckboxChange, handleSaveData } from './settingsUtils';
import "assets/global.css";

function Settings() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [items, setItems] = useState([]);
    const [selectedItems, setSelectedItems] = useState([]);
    const [status, setStatus] = useState('');

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    useEffect(() => {
        fetchDataFromAPI(setItems, setSelectedItems, setStatus);
    }, []);

    const handleCheckboxChangeWrapper = (item) => {
        handleCheckboxChange(item, items, setItems, setSelectedItems);
    };

    const handleSave = () => {
        handleSaveData(selectedItems, setStatus);
    };

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className="main-layout" style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Settings</h1>
                <br />
                <div className="upload-container">
                    <h3 className="h3-center">Select which projects can be evaluated</h3>
                    <br />
                    <ul className="checkbox-menu">
                        {items.map(item => (
                            <li key={item.id}>
                                <label className="checkbox-label">
                                    <input
                                        className="checkbox-input"
                                        type="checkbox"
                                        checked={item.checked}
                                        onChange={() => handleCheckboxChangeWrapper(item)}
                                    />
                                    {item.name} - {item.info}
                                </label>
                            </li>
                        ))}
                    </ul>
                    <div className='save-button'>
                        <button onClick={handleSave}>Save changes</button>
                        <StatusMessage status={status} className="status-message" />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Settings;
