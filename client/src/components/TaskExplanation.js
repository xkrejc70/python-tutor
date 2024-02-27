import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { coy } from 'react-syntax-highlighter/dist/esm/styles/prism';

function TaskExplanation({ imgSrc, heading, practiceTask, code }) {
    return (
        <div>
            <img src={imgSrc} alt={"taskImg"} className="task-image" />
            <h2 className="heading-h2">{heading}</h2>
            <p className='practice-task'>{practiceTask}</p>
            <SyntaxHighlighter language="python" style={coy} className="bordered code-style">
                {code}
            </SyntaxHighlighter>
        </div>
    );
}

export default TaskExplanation;
