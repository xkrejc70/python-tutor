import React from 'react';

function StatusMessage({ status }) {
    return status && <p className={`status`}>{status}</p>;
}

export default StatusMessage;
