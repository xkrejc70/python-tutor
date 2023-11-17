import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
// css
import "assets/global.css";

function Home() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

    const handleSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    return (
        <div>
            <Sidebar onCollapsedChange={handleSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>
                    Home
                </h1>
                <p>asdf</p>
            </div>
        </div>
    );
}

export default Home;