import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import Quiz from "components/Quiz";
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { coy } from 'react-syntax-highlighter/dist/esm/styles/prism';
import "assets/global.css";
import scrabbleImg from 'assets/images/scrabble.png'

function Proj4() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [codeLine, setCodeLine] = useState('_____1_____');
    const [tab, setTab] = useState('');

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };

    const handleNext = () => {
        console.log("");
    };

    const handlePrevious = () => {
        console.log("");
    };

    const updateCode = (index) => {
        setCodeLine('set(words).intersection(perms)');
    };

    const TaskExplanation = () => {
        return (
            <div>
                <img src={scrabbleImg} alt={"scrabbleImg"} className="task-image" />
                <h2 className="heading-h2">Task:</h2>
                <p className='practice-task'>
                You are developing a Scrabble helper to assist players in finding valid words that can be formed using any subset of the letters they have on their rack.
                However, the challenge is that the Scrabble dictionary is extensive, containing tens of thousands of words.
                The function needs to handle this vast dictionary efficiently to provide quick and relevant suggestions.
                </p>
                <SyntaxHighlighter language="python" style={coy} className="bordered code-style">
                    {`def scrabble_helper(letters, words):
    """
    Finds valid words that can be formed using any subset of the provided letters.

    Parameters:
    - letters (str): A string representing the available letters.
    - words (list): A list of words to check for validity.

    Returns:
    - set: A set of valid words that can be formed using any subset of the available letters.
    """
    perms = all_permutations_substrings(letters)
    return ${codeLine}`}
                </SyntaxHighlighter>
            </div>
        );
    };

    /*
    try block around detecking
    */

    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <button onClick={handlePrevious}>Previous</button>
                    <h1>Set operations</h1>
                    <button onClick={handleNext}>Next</button>
                </div>
                <br />

                <div>
                    <TaskExplanation />
                    <Quiz updateCode={updateCode} quiz="scrabble" />
                </div>
            </div>
        </div>
    );
}

export default Proj4;
