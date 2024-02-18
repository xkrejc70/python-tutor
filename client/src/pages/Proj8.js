import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import Quiz from "components/Quiz";
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { coy } from 'react-syntax-highlighter/dist/esm/styles/prism';
import "assets/global.css";

function Proj8() {


    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [uniqueCategoriesVariable, setUniqueCategoriesVariable] = useState('_____1_____');
    const [uniqueCategoriesHash, setUniqueCategoriesHash] = useState('_____2_____');
    const [uniqueCategoriesYield, setUniqueCategoriesYield] = useState('_____3_____');

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    const updateCode = (index) => {
        switch (index) {
            case 0:
                setUniqueCategoriesVariable("set()");
                break;
            case 2:
                setUniqueCategoriesHash("hash");
                break;
            case 3:
                setUniqueCategoriesYield("yield category_name_with_long_description");
                break;
            default:
                // Handle invalid category type
                break;
        }
    };

    const TaskExplanation = () => {
        return (
            <div>
                <h2 className="heading-h2">Task:</h2>
                <p className='practice-task'>
                    You're tasked with developing a spam detection system for processing a continuous stream of emails.
                    The system needs to identify unique categories of spam without storing individual email addresses due to the potentially infinite queue.
                </p>
                <SyntaxHighlighter language="python" style={coy} className="bordered-code">
                    {`def unique_spam_categories(email_queue):
    """Generate unique spam categories from a potentially infinite email queue."""
    unique_categories = ${uniqueCategoriesVariable}
    while True:
        email = email_queue.get_next()
        if email is None:
            break
        category_name_with_long_description = detect_spam(email)
        compact_category = ${uniqueCategoriesHash}(category_name_with_description)
        if compact_category not in unique_categories:
            add_item(unique_categories, compact_category)
            ${uniqueCategoriesYield}`}
                </SyntaxHighlighter>
            </div>
        );
    };

    /*
    variable type
    hash to compress long string
    try block around detecking
    yeild is more efficient than returning var
    */

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Practice</h1>
                <br />

                <div>
                    <TaskExplanation />
                    <Quiz updateCode={updateCode} />
                </div>
            </div>
        </div>
    );
}

export default Proj8;
