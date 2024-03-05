import React, { useState } from 'react';
import Sidebar from "components/Sidebar";
import Quiz from "components/Quiz";
import TaskExplanation from "components/TaskExplanation";
import "assets/global.css";
import scrabbleImg from 'assets/images/scrabble.png'

function Proj4() {
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [intersection, setIntersection] = useState('_____1_____');
    const [sorted, setSorted] = useState('_____2_____');

    const onSidebarCollapsedChange = (collapsed) => {
        setSidebarCollapsed(collapsed);
    };
    
    const updateCode = (index) => {
        switch (index) {
            case 0:
                setIntersection('set(words).intersection(perms)');
                break;
            case 1:
                setSorted("sorted(valid_words, key=word_value)");
                break;
            default:
                break;
        }
    };

    const heading = "Task:";
    const description = `You are developing a Scrabble helper to assist players in finding valid words that can be formed using any subset of the letters they have on their rack.
    However, the challenge is that the Scrabble dictionary is extensive, containing tens of thousands of words.
    The function needs to handle this vast dictionary efficiently to provide quick and relevant suggestions.
    Additionally, the Scrabble helper should prioritize words based on their total point value, enhancing the player's ability to choose words that yield the highest scores.`;
    const code = `def scrabble_helper(letters, words):
    """
    Efficiently identifies and sorts valid Scrabble words based on their total point value.
    Parameters:
    - letters (str): A string representing the available letters.
    - words (list): A list of words to check for validity.
    Returns:
    - set: A sorted list of valid words based on their total point value in Scrabble.
    """
    perms = all_permutations_substrings(letters)
    valid_words = ${intersection}
    return ${sorted}`;


    return (
        <div>
            <Sidebar onCollapsedChange={onSidebarCollapsedChange} />
            <div className={"main-layout"} style={{ marginLeft: sidebarCollapsed ? "80px" : "250px" }}>
                <h1>Set operations</h1>
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
