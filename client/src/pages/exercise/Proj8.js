import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import Quiz from "components/Quiz";
import TaskExplanation from "components/TaskExplanation";
import "assets/global.css";
import emailImg from 'assets/images/email.png'

function Proj8() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [uniqueCategoriesVariable, setUniqueCategoriesVariable] = useState('_____1_____');
    const [uniqueCategoriesHash, setUniqueCategoriesHash] = useState('_____2_____');
    const [uniqueCategoriesYield, setUniqueCategoriesYield] = useState('_____3_____');
    const [addToSet, setAddToSet] = useState('add_item(unique_categories, compact_category)');
    const [tryBlock, setTryBlock] = useState('');
    const [exceptBlock, setExceptBlock] = useState('');
    const [tab, setTab] = useState('');

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    const updateCode = (index) => {
        switch (index) {
            case 0:
                setUniqueCategoriesVariable("set()");
                setAddToSet('unique_categories.add(compact_category)');
                break;
            case 2:
                setUniqueCategoriesHash("hash");
                break;
            case 3:
                setTryBlock(`
        try:`)
                setTab("    ")
                setExceptBlock(`
        except Exception as e:
            print(f"Error processing email: {e}")
            continue`);
                break;
            case 4:
                setUniqueCategoriesYield("yield category_name_with_long_description");
                break;
            default:
                break;
        }
    };

    const heading = "Task:";
    const description = `Your goal is to develope a spam detection system for processing a continuous stream of emails.
    The system needs to identify unique categories of spam without storing individual email addresses due to the potentially infinite queue.`;
    const code = `def unique_spam_categories(email_queue):
    """Generate unique spam categories from a potentially infinite email queue."""
    unique_categories = ${uniqueCategoriesVariable}
    while True:
        email = email_queue.get_next()
        if email is None:
            break${tryBlock}
        ${tab}category_name_with_long_description = detect_spam(email)
        ${tab}compact_category = ${uniqueCategoriesHash}(category_name_with_description)${exceptBlock}
        if compact_category not in unique_categories:
            ${addToSet}
            ${uniqueCategoriesYield}`;

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Exercise Project 8</h1>
                <br />

                <div>
                    <TaskExplanation
                        imgSrc={emailImg}
                        heading={heading}
                        practiceTask={description}
                        code={code}
                    />
                    <Quiz updateCode={updateCode} quiz="proj8" />
                </div>
            </div>
        </div>
    );
}

export default Proj8;