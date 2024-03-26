import React from 'react';
import Sidebar from "components/Sidebar";
import { useLocation, Navigate } from 'react-router-dom';
import "assets/global.css";
import { ExpandableContainer } from './evaluationUtils';
import { FaCheckSquare, FaCode, FaCommentAlt } from "react-icons/fa";
import { FaSquareXmark } from "react-icons/fa6";
import { MdTipsAndUpdates } from "react-icons/md";
import { BsFillFileEarmarkFill } from "react-icons/bs";


function Evaluation() {
    let location = useLocation();
    const uploadData = location.state;
    const [sidebarCollapsed, setSidebarCollapsed] = React.useState(false);

    const handleSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    if (!uploadData || uploadData == null) {
        return <Navigate to="/upload" />;
    }

    const file_content = uploadData?.test?.file_content;
    const filename = uploadData?.test?.filename;
    const numTests = uploadData?.test?.test_result?.num_tests;
    const passed = uploadData?.test?.test_result?.passed;
    const percentage = numTests > 0 ? ((passed / numTests) * 100).toFixed(2) : 0;
    const comments = uploadData?.test?.test_result?.comment;
    const practice_tips = uploadData?.test?.test_result?.practice_tips?.length ?? 0;
    const external_tips = uploadData?.test?.test_result?.external_tips?.length ?? 0;
    const tips_num = practice_tips + external_tips;

    const model_response = uploadData?.test?.test_result?.model_response;
    const response_len = model_response ? model_response.length : 0;

    const analysis_result = uploadData?.test?.analysis_result;

    return (
        <div>
            <Sidebar onCollapsedChange={handleSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Evaluation</h1>

                <br />

                {/* Display test results */}
                <ExpandableContainer className="expandable-container feedback-title" title={
                    <div>
                        {percentage > 99 ? <FaCheckSquare size={22} className="test-passed feedback-icon" /> : <FaSquareXmark size={23} className="test-failed feedback-icon" />}
                        {`${passed}/${numTests} tests passed (${percentage}%)`}
                    </div>
                }>
                    {comments && comments.map((item, index) => (
                        <p key={index}>{item}</p>
                    ))}
                </ExpandableContainer>

                <hr className="container-divider" />

                {/* Display model feedback */}
                {model_response && model_response.length > 0 && (
                    <>
                        <ExpandableContainer title={
                            <div>
                                {<FaCommentAlt size={20} className="feedback-icon" />}
                                {`Feedback: (${response_len})`}
                            </div>
                        }>
                            {model_response.map((item, index) => (
                                <p key={index}>{item}</p>
                            ))}
                        </ExpandableContainer>
                        <hr className="container-divider" />
                    </>
                )}

                {/* Display practice and external tips */}
                {tips_num > 0 && (
                    <>
                        <ExpandableContainer title={
                            <div>
                                {<MdTipsAndUpdates size={23} className="feedback-icon" />}
                                {`Python Practice & Tutorials (${tips_num})`}
                            </div>
                        }>
                            {uploadData.test && uploadData.test.test_result && (
                                <div>
                                    {uploadData.test.test_result.practice_tips && (
                                        <div>
                                            <h3 className="tips-title">Practice:</h3>
                                            <ul className="tips-list">
                                                {uploadData.test.test_result.practice_tips.map((tip, index) => (
                                                    <li key={index} className="tip-item">
                                                        <a href={tip.url} target="_blank" rel="noopener noreferrer" className="tip-link">
                                                            {tip.text}
                                                        </a>
                                                    </li>
                                                ))}
                                            </ul>
                                        </div>
                                    )}

                                    {uploadData.test.test_result.external_tips && (
                                        <div>
                                            <h3 className="tips-title">External:</h3>
                                            <ul className="tips-list">
                                                {uploadData.test.test_result.external_tips.map((tip, index) => (
                                                    <li key={index} className="tip-item">
                                                        <a href={tip.url} target="_blank" rel="noopener noreferrer" className="tip-link">
                                                            {tip.text}
                                                        </a>
                                                    </li>
                                                ))}
                                            </ul>
                                        </div>
                                    )}
                                </div>
                            )}
                        </ExpandableContainer>
                        <hr className="container-divider" />
                    </>
                )}

                {/* Display analysis results */}
                {analysis_result && (
                    <>
                        <ExpandableContainer title={
                            <div>
                                {<FaCode size={23} className="feedback-icon" />}
                                {`Static Code Analysis`}
                            </div>
                        } useSyntaxHighlighting={true} lang='json'>
                            {analysis_result.stdout}
                        </ExpandableContainer>
                        <hr className="container-divider" />
                    </>
                )}

                {/* Display uploaded file */}
                <ExpandableContainer defaultOpen={true} title={
                    <div>
                        {<BsFillFileEarmarkFill size={20} className="feedback-icon" />}
                        {`Uploaded file (${filename})`}
                    </div>
                } useSyntaxHighlighting={true} lang='python'>
                    {file_content}
                </ExpandableContainer>



                { /*<ExpandableContainer title={`Output (ToBeDeleted)`} defaultOpen={true} >
                    {JSON.stringify(uploadData, null, 2)}
            </ExpandableContainer>*/ }
            </div>
        </div>
    );
}

export default Evaluation;
