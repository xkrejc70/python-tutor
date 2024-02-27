// Admin.js
import React, { useState, useEffect } from 'react';
import Sidebar from "components/Sidebar";
import StatusMessage from "components/StatusMessage";
import { fetchDataFromAPI, handleCheckboxChange, handleSaveData } from './adminUtils';
import "assets/global.css";

function Admin() {
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
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Project Submission</h1>
                <br />
                <div className="upload-container">
                    <h3 className='h3-center'>Upload your project</h3>
                    <br />
                    <ul>
                        {items.map(item => (
                            <li key={item.id}>
                                <label>
                                    <input
                                        type="checkbox"
                                        checked={item.checked}
                                        onChange={() => handleCheckboxChangeWrapper(item)}
                                    />
                                    {item.name} - {item.info}
                                </label>
                            </li>
                        ))}
                    </ul>
                    <button onClick={handleSave}>Save</button>
                    <StatusMessage status={status} />
                </div>
            </div>
        </div>
    );
}

export default Admin;
