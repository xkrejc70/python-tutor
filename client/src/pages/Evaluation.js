import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import { useLocation } from 'react-router-dom';
import "assets/global.css";

function ExpandableContainer({ title, children }) {
    const [isExpanded, setIsExpanded] = useState(false);

    const toggleExpansion = () => {
        setIsExpanded((prev) => !prev);
    };

    return (
        <div className={`expandable-container ${isExpanded ? 'expanded' : 'collapsed'}`}>
            <div className="container-title" onClick={toggleExpansion}>
                {title}
            </div>
            {isExpanded && (
                <div className="container-content">
                    {children}
                </div>
            )}
        </div>
    );
}

function Evaluation() {
    let location = useLocation();
    // rename
    const uploadData = location.state;
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

    const handleSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    return (
        <div>
            <Sidebar onCollapsedChange={handleSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Evaluation</h1>

                <br />

                <ExpandableContainer title="Výsledky testů (4/5)">
                    <pre>{JSON.stringify(uploadData, null, 2)}</pre>
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title="Doporučení (3)">
                    <p>Content for Container 2</p>
                    <p>Content for Container 2</p>
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title="Tipy na samostudium (1)">
                    <p>Odkaz na sekci zde </p>
                    <p>Odkaz na tutorial jinde</p>
                </ExpandableContainer>
            </div>
        </div>
    );
}

export default Evaluation;
