import React from 'react';
import Sidebar from "components/Sidebar";
import { useLocation } from 'react-router-dom';
import "assets/global.css";
import { ExpandableContainer } from './evaluationUtils';

function Evaluation() {
    let location = useLocation();
    const uploadData = location.state;
    const [sidebarCollapsed, setSidebarCollapsed] = React.useState(false);

    const handleSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    const file_content = uploadData?.test?.file_content;
    const filename = uploadData?.test?.filename;
    const numTests = uploadData?.test?.test_result?.num_tests;
    const passed = uploadData?.test?.test_result?.passed;
    const percentage = numTests > 0 ? ((passed / numTests) * 100).toFixed(2) : 0;
    const comments = uploadData?.test?.test_result?.comment;
    const tips_num = uploadData?.test?.test_result?.tips?.length ?? 0;
    
    const model_response = uploadData?.test?.test_result?.model_response;
    const response_len = model_response ? model_response.length : 0;

    return (
        <div>
            <Sidebar onCollapsedChange={handleSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Evaluation</h1>

                <br />

                <ExpandableContainer title={`${passed}/${numTests} tests passed (${percentage}%)`} >
                    {comments && comments.map((item, index) => (
                        <p key={index}>{item}</p>
                    ))}
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title={`Recommendations: (${response_len})`}>
                    {model_response && model_response.map((item, index) => (
                        <p key={index}>{item}</p>
                    ))}
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title={`Tips for self-study (${tips_num})`}>
                    {uploadData.test && uploadData.test.test_result && uploadData.test.test_result.tips && (
                        <ul className="tips-list">
                            {uploadData.test.test_result.tips.map((tip, index) => (
                                <li key={index} className="tip-item">
                                    <a href={tip.url} target="_blank" rel="noopener noreferrer" className="tip-link">
                                        {tip.text}
                                    </a>
                                </li>
                            ))}
                        </ul>
                    )}
                </ExpandableContainer>

                <hr className="container-divider" />

                <ExpandableContainer title={`Uploaded file (${filename})`} defaultOpen={true} useSyntaxHighlighting={true}>
                    {file_content}
                </ExpandableContainer>

                <hr className="container-divider" />
                <hr className="container-divider" />
                <hr className="container-divider" />

                <ExpandableContainer title={`Output (ToBeDeleted)`} defaultOpen={true} >
                    {JSON.stringify(uploadData, null, 2)}
                </ExpandableContainer>
            </div>
        </div>
    );
}

export default Evaluation;
