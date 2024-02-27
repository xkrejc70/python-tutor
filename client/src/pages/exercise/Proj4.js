import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import Quiz from "components/Quiz";
import TaskExplanation from "components/TaskExplanation";
import "assets/global.css";
import scrabbleImg from 'assets/images/scrabble.png'

function Proj4() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [codeLine, setCodeLine] = useState('_____1_____');

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

    const heading = "Task:";
    const description = `You are developing a Scrabble helper to assist players in finding valid words that can be formed using any subset of the letters they have on their rack.
    However, the challenge is that the Scrabble dictionary is extensive, containing tens of thousands of words.
    The function needs to handle this vast dictionary efficiently to provide quick and relevant suggestions.`;
    const code = `def scrabble_helper(letters, words):
    """
    Finds valid words that can be formed using any subset of the provided letters.

    Parameters:
    - letters (str): A string representing the available letters.
    - words (list): A list of words to check for validity.

    Returns:
    - set: A set of valid words that can be formed using any subset of the available letters.
    """
    perms = all_permutations_substrings(letters)
    return ${codeLine}`;

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
                    <TaskExplanation
                        imgSrc={scrabbleImg}
                        heading={heading}
                        practiceTask={description}
                        code={code}
                    />
                    <Quiz updateCode={updateCode} quiz="scrabble" />
                </div>
            </div>
        </div>
    );
}

export default Proj4;
