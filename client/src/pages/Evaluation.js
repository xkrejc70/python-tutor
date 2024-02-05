import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import { useLocation } from 'react-router-dom';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { coy } from 'react-syntax-highlighter/dist/esm/styles/prism';
import "assets/global.css";

/**
 * ExpandableContainer Component
 * @param {Object} props - React component properties.
 * @param {string} props.title - The title of the expandable container.
 * @param {ReactNode} props.children - The content to be displayed within the container.
 * @param {boolean} [props.defaultOpen=false] - Determines whether the container is expanded by default.
 * @param {boolean} [props.useSyntaxHighlighting=false] - Determines whether to apply syntax highlighting (for Python code) to the container.
 * @returns {JSX.Element} - React JSX Element representing the ExpandableContainer.
 */
function ExpandableContainer({ title, children, defaultOpen = false, useSyntaxHighlighting = false }) {
    const [isExpanded, setIsExpanded] = useState(defaultOpen);

    const toggleExpansion = () => {
        setIsExpanded((prev) => !prev);

        const containerContent = document.querySelector(".ps-sidebar-container");
        if (containerContent) {
            console.log(window.innerHeight);
            containerContent.style.height = `${window.innerHeight + 100- containerContent.offsetTop}px`;
        }
        
    };

    return (
        <div className={`expandable-container ${isExpanded ? 'expanded' : 'collapsed'}`}>
            <div className="container-title" onClick={toggleExpansion}>
                {title}
            </div>
            {isExpanded && (
                <div className="container-content">
                {useSyntaxHighlighting ? (
                    <SyntaxHighlighter language="python" style={coy}>
                        {children}
                    </SyntaxHighlighter>
                ) : (
                    <pre>{children}</pre>
                )}
            </div>
            )}
        </div>
    );
}

/**
 * Evaluation Component
 * @returns {JSX.Element} - React JSX Element representing the Evaluation component.
 */
function Evaluation() {
    let location = useLocation();
    // rename
    const uploadData = location.state;
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

    const handleSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    const file_content = uploadData?.test?.file_content;
    const numTests = uploadData?.test?.test_result?.num_tests;
    const passed = uploadData?.test?.test_result?.passed;
    const percentage = numTests > 0 ? ((passed / numTests) * 100).toFixed(2) : 0;
    const comments = uploadData?.test?.test_result?.comment;
    
    const model_response = uploadData?.test?.test_result?.model_response;
    const response_len = model_response ? model_response.length : 0;

    return (
        <div>
            <Sidebar onCollapsedChange={handleSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Vyhodnocení</h1>

                <br />

                <ExpandableContainer title={`Output (ToBeDeleted)`} defaultOpen={true} >
                    {JSON.stringify(uploadData, null, 2)}
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title={`Vyhodnocení testů: ${passed}/${numTests} = ${percentage}%`} >
                    {comments && comments.map((item, index) => (
                        <p key={index}>{item}</p>
                    ))}
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title={`Doporučení: (${response_len})`}>
                    {model_response && model_response.map((item, index) => (
                        <p key={index}>{item}</p>
                    ))}
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title="Tipy na samostudium (1)">
                    <p>Odkaz na sekci k procvičení zde </p>
                    <p>Odkaz na tutorial jinam</p>
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title="Nahraný soubor" defaultOpen={true} useSyntaxHighlighting={true}>
                    {file_content}
                </ExpandableContainer>
            </div>
        </div>
    );
}

export default Evaluation;
