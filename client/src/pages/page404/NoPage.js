import React, { useState } from 'react';
import Sidebar from "components/Sidebar";

function Home() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>
                    404 - Page not found
                </h1>
            </div>
        </div>
    );
}

export default Home;