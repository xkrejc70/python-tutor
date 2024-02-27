import React, { useState } from 'react';
import axios from 'axios';
import { useAuth } from 'AuthContext';
import Sidebar from "components/Sidebar";
import { useNavigate } from 'react-router-dom';
import "assets/global.css";

function Login() {
    const navigate = useNavigate();
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [status, setStatus] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const { login } = useAuth();

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    const handleLogin = () => {
        // Prepare the data to be sent to the server
        const data = {
            username: username,
            password: password,
        };

        // Send login request to the server
        axios.post('http://localhost:5005/api/admin/login', data)
            .then(response => {
                if (response.status === 200) {
                    setStatus('Logged in successfully!');
                    login();
                    navigate("/admin");
                } else {
                    setStatus(`Error: ${response.data}`);
                }
            })
            .catch(error => {
                if (error.response) {
                    setStatus(`Error: ${error.response.data.error}`);
                    console.error('Response error:', error.response.status, error.response.data);
                } else if (error.request) {
                    setStatus('Error: No response received from the server');
                    console.error('No response received:', error.request);
                } else {
                    setStatus(`Error: ${error.message}`);
                    console.error('Error:', error.message);
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
                    <h2>Login</h2>
                    <div>
                        <label>Username:</label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </div>
                    <div>
                        <label>Password:</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                    <button onClick={handleLogin}>Login</button>
                    {status && <p className={`status`}>{status}</p>}
                </div>
            </div>
        </div>
    );
};

export default Login;
