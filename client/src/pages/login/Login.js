// Login.js
import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import StatusMessage from "components/StatusMessage";
import { useNavigate } from 'react-router-dom';
import { useAuth } from 'AuthContext';
import { handleLoginRequest } from './loginUtils';
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
        handleLoginRequest(username, password, setStatus, login, navigate);
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
                    <StatusMessage status={status} />
                </div>
            </div>
        </div>
    );
};

export default Login;
