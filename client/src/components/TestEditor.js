import React, { useState, useEffect } from 'react';
import { AiFillDelete } from "react-icons/ai";
import { TbMinusVertical } from "react-icons/tb";
import { FaEdit } from "react-icons/fa";
import 'assets/global.css';

const TestEditor = ({ tests, projs, onTestsChange }) => {
    const [selectedProject, setSelectedProject] = useState('');
    const [selectedProjectName, setSelectedProjectName] = useState('');
    const [selectedFunction, setSelectedFunction] = useState('');
    const [selectedTestIndex, setSelectedTestIndex] = useState(null);
    const [inputValue, setInputValue] = useState('');
    const [outputValue, setOutputValue] = useState('');

    function getNameById(id) {
        const project = projs.find(proj => proj.id === id);
        return project ? project.name : "Project not found";
    }

    // Populate project and function dropdown options
    const projects = Object.keys(tests);
    console.log(projects);
    const functions = selectedProject ? Object.keys(tests[selectedProject]) : [];

    // Create an object to store the mapping of projX to names
    const idToNameMap = {};

    // Populate the idToNameMap with the corresponding names
    projects.forEach(id => {
        const numericId = parseInt(id.replace("proj", ""), 10);
        const name = getNameById(numericId);
        idToNameMap[id] = name;
    });

    // Update input and output values when a test is selected
    useEffect(() => {
        if (selectedTestIndex !== null) {
            const selectedTest = tests[selectedProject]?.[selectedFunction]?.[selectedTestIndex];
            setInputValue(selectedTest?.in || '');
            setOutputValue(selectedTest?.out || '');
        } else {
            setInputValue('');
            setOutputValue('');
        }
    }, [selectedTestIndex, tests, selectedProject, selectedFunction]);

    // Handle test modification or addition
    const handleSaveTest = () => {
        const updatedTests = { ...tests };

        if (!updatedTests[selectedProject]) {
            updatedTests[selectedProject] = {};
        }

        if (!updatedTests[selectedProject][selectedFunction]) {
            updatedTests[selectedProject][selectedFunction] = [];
        }

        const test = { in: inputValue, out: outputValue };

        if (selectedTestIndex !== null) {
            updatedTests[selectedProject][selectedFunction][selectedTestIndex] = test;
        } else {
            updatedTests[selectedProject][selectedFunction].push(test);
        }

        onTestsChange(updatedTests);
        setSelectedTestIndex(null);
    };

    // Handle test deletion
    const handleDeleteTest = (index) => {
        if (index !== null) {
            const updatedTests = { ...tests };
            updatedTests[selectedProject][selectedFunction].splice(index, 1);
            onTestsChange(updatedTests);
            setSelectedTestIndex(null);
        }
    };

    // Handle project selection
    const handleProjectChange = (selectedProject) => {
        setSelectedProject(selectedProject, idToNameMap[selectedProject]);
        setSelectedProjectName(idToNameMap[selectedProject]);
        setSelectedFunction('');
        setInputValue('');
        setOutputValue('');
        setSelectedTestIndex(null);
    };

    // Handle function selection
    const handleFunctionChange = (selectedFunction) => {
        setSelectedFunction(selectedFunction);
        setInputValue('');
        setOutputValue('');
        setSelectedTestIndex(null);
    };


    return (
        <div>
            <div>
                <div style={{ display: 'inline-block', marginRight: '20px' }}>
                    <label>
                        Select Project:
                        <select className="tests-select" value={selectedProject} onChange={(e) => handleProjectChange(e.target.value)}>
                            <option value="">Select Project</option>
                            {projects.map((projectId) => (
                                <option key={projectId} value={projectId}>
                                    {idToNameMap[projectId]}
                                </option>
                            ))}
                        </select>
                    </label>
                </div>

                {selectedProject && (
                    <div style={{ display: 'inline-block' }}>
                        <label>
                            Select Function:
                            <select className="tests-select" value={selectedFunction} onChange={(e) => handleFunctionChange(e.target.value)}>
                                <option value="">Select Function</option>
                                {functions.map((func) => (
                                    <option key={func} value={func}>
                                        {func}
                                    </option>
                                ))}
                            </select>
                        </label>
                    </div>
                )}
            </div>


            {selectedFunction && (
                <div>
                    <br />
                    <h3 className="h3-center">Edit Tests for {selectedFunction} in {selectedProjectName}</h3>
                    <br />

                    <table className="tests-table">
                        <thead>
                            <tr className='align-l'>
                                <th>Input</th>
                                <th>Output</th>
                                <th className='align-r'>Operations</th>
                            </tr>
                        </thead>
                        <tbody>
                            {tests[selectedProject][selectedFunction].map((test, index) => (
                                <tr key={index}>
                                    <td>{test.in}</td>
                                    <td>{test.out}</td>
                                    <td className='align-r'>
                                        <span className="modify-test" onClick={() => setSelectedTestIndex(index)}><FaEdit size={23} /></span>
                                        <TbMinusVertical size={23} />
                                        <span className="delete-text" onClick={() => handleDeleteTest(index)}><AiFillDelete size={23} /></span>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    <br />
                    <br />

                    <label>Input:</label>
                    <input className="input-field" type="text" value={inputValue} onChange={(e) => setInputValue(e.target.value)} />

                    <label>Output:</label>
                    <input className="input-field" type="text" value={outputValue} onChange={(e) => setOutputValue(e.target.value)} />
                    <div className='save-button'>
                        <button onClick={handleSaveTest}>{selectedTestIndex !== null ? 'Save test case' : 'Add new Test'}</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default TestEditor;
