import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { coy } from 'react-syntax-highlighter/dist/esm/styles/prism';
import "assets/global.css";

export const ExpandableContainer = ({ title, children, defaultOpen = false, useSyntaxHighlighting = false }) => {
    const [isExpanded, setIsExpanded] = React.useState(defaultOpen);

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
                    <SyntaxHighlighter language="python" style={coy} className="code-style">
                        {children}
                    </SyntaxHighlighter>
                ) : (
                    <pre>{children}</pre>
                )}
            </div>
            )}
        </div>
    );
};
