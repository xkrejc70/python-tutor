import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import { FaExclamation } from "react-icons/fa";
import "assets/global.css";

function About() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>About Python Tutor</h1>
                <br />
                <p className='text-about'>Python Tutor is an interactive platform where students can upload their projects for evaluation with feedback and practice exercises on various Python programming topics.</p>
                <br />
                <p className='text-about'>In case of any issues or feedback, contact <a href="mailto:pytutor.isj@gmail.com">pytutor.isj@gmail.com</a>.</p>
                <br />
                <p className='text-about'><FaExclamation size={20}/><b>Disclaimer: </b>The platform serves as a supplementary tool, test cases may not align with official course grading criteria.</p>
            </div>
        </div>
    );
}

export default About;
