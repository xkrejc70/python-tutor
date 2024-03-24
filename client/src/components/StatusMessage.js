import React from 'react';

function StatusMessage({ status }) {
    let className = 'default';
    
    if (status === 'Settings saved' || status === 'New project added' || status === 'Project deleted') {
        className = 'status status-success';
    } else if (status === 'Uploading...') {
        className = 'status black';
    } else {
        className = 'status';
    }
    return status && <p className={`status ${className}`}>{status}</p>;
}

export default StatusMessage;
