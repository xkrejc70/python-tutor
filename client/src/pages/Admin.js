import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Sidebar from "components/Sidebar";
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
        // Fetch data from the Flask API
        fetch('http://localhost:5005/api/admin/projects')
            .then(response => response.json())
            .then(data => {
                // Update the 'checked' property based on the items array
                const updatedItems = data.map(item => ({
                    ...item,
                    checked: item.checked || false,
                }));
                setItems(updatedItems);

                // Initialize selectedItems with initially checked items
                const initiallyCheckedItems = updatedItems.filter(item => item.checked);
                setSelectedItems(initiallyCheckedItems);
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    const handleCheckboxChange = (item) => {
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

    const handleSave = () => {
        // Prepare the data to be sent to the API
        const dataToSend = selectedItems.map(item => ({
            checked: item.checked,
            id: item.id,
            info: item.info,
            name: item.name,
        }));
    
        // Send data to your API
        axios.post('http://localhost:5005/api/admin/save', dataToSend)
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
                } else {
                    setStatus(`Error: ${error.response.data}`);
                }
            });
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
                                        onChange={() => handleCheckboxChange(item)}
                                    />
                                    {item.name} - {item.info}
                                </label>
                            </li>
                        ))}
                    </ul>
                    <button onClick={handleSave}>Save</button>
                    {status && <p className={`status`}>{status}</p>}
                </div>
            </div>
        </div>
    );
}

export default Admin;
