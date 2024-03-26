import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { coy } from 'react-syntax-highlighter/dist/esm/styles/prism';
import "assets/global.css";

export const ExpandableContainer = ({ title, children, defaultOpen = false, lang = 'python', useSyntaxHighlighting = false }) => {
    const [isExpanded, setIsExpanded] = React.useState(defaultOpen);

    const toggleExpansion = () => {
        setIsExpanded((prev) => !prev);

        const containerContent = document.querySelector(".ps-sidebar-container");
        if (containerContent) {
            containerContent.style.height = `${window.innerHeight + 100 - containerContent.offsetTop}px`;
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
                        <SyntaxHighlighter language={lang} style={coy} className="code-style" showLineNumbers>
                            {children}
                        </SyntaxHighlighter>
                    ) : (
                        <pre>{children}</pre>
                    )}
                    {lang === "json" &&
                        <p><i>Results from <a href="https://pypi.org/project/pylint/" target="_blank" rel="noreferrer">pylint</a>'s static code analysis are provided for informational purposes and should be considered alongside project-specific requirements and coding standards.</i></p>
                    }
                </div>
            )}
        </div>
    );
};
