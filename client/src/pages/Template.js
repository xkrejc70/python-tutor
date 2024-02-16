import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import "assets/global.css";

function Upload() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Practice</h1>
                <br />
                
            </div>
        </div>
    );
}

export default Upload;
