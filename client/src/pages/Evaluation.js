import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
// css
import "assets/global.css";

function Evaluate() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

    const handleSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    return (
        <div>
            <Sidebar onCollapsedChange={handleSidebarCollapsedChange} />
            <div class="main-layout" style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>
                    Home
                </h1>
                <p>asdf</p>
            </div>
        </div>
    );
}

export default Evaluate;