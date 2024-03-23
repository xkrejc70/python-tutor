import React, { useState, useEffect, useMemo } from 'react';
import { updateTestsAndSave } from './testEditorUtils';
import { AiFillDelete } from "react-icons/ai";
import { TbMinusVertical } from "react-icons/tb";
import { FaEdit } from "react-icons/fa";
import 'assets/global.css';

const TestEditor = ({ tests, projs, onTestsChange }) => {
    const [selectedProject, setSelectedProject] = useState('');
    const [selectedFunction, setSelectedFunction] = useState('');
    const [selectedTestIndex, setSelectedTestIndex] = useState(null);
    const [inputValue, setInputValue] = useState('');
    const [inputType, setInputType] = useState('string');
    const [outputValue, setOutputValue] = useState('');
    const [outputType, setOutputType] = useState('string');

    function getNameById(id) {
        const project = projs.find(proj => proj.id === id);
        return project ? project.name : "Project not found";
    }

    function isProjectEditable(id) {
        const project = projs.find(proj => proj.id === id);
        return project ? project.editable : false;
    }

    // Populate project and function dropdown options
    const projects = Object.keys(tests);
    const functions = useMemo(() => selectedProject ? Object.keys(tests[selectedProject]) : [], [selectedProject, tests]);

    // Create an object to store the mapping of projX to names
    const idToNameMap = {};
    const isEditable = {};

    // Populate the idToNameMap with the corresponding names
    projects.forEach(id => {
        const numericId = parseInt(id.replace("proj", ""), 10);
        const name = getNameById(numericId);
        idToNameMap[id] = name;

        isEditable[id] = isProjectEditable(numericId);
    });

    // Update input and output values when a test is selected
    useEffect(() => {
        if (selectedTestIndex !== null) {
            const selectedTest = tests[selectedProject]?.[selectedFunction]?.[selectedTestIndex];
            setInputValue(selectedTest?.in || '');
            setOutputValue(selectedTest?.out || '');
            setInputType(selectedTest?.inputType || 'string');
            setOutputType(selectedTest?.outputType || 'string');
        } else {
            setInputValue('');
            setOutputValue('');
            setInputType('string');
            setOutputType('string');
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

        const test = {
            in: inputValue,
            out: outputValue,
            inputType,
            outputType
        };

        if (selectedTestIndex !== null) {
            updatedTests[selectedProject][selectedFunction][selectedTestIndex] = test;
        } else {
            updatedTests[selectedProject][selectedFunction].push(test);
        }

        updateTestsAndSave(updatedTests, onTestsChange);
        setSelectedTestIndex(null);
    };

    // Handle test deletion
    const handleDeleteTest = (index) => {
        if (index !== null) {
            const updatedTests = { ...tests };
            updatedTests[selectedProject][selectedFunction].splice(index, 1);
            updateTestsAndSave(updatedTests, onTestsChange);
            setSelectedTestIndex(null);
        }
    };

    // Handle project selection
    const handleProjectChange = (selectedProject) => {
        setSelectedProject(selectedProject, idToNameMap[selectedProject]);
        setSelectedFunction('');
        setInputValue('');
        setOutputValue('');
        setInputType('string');
        setOutputType('string');
        setSelectedTestIndex(null);
    };

    // Handle function selection
    const handleFunctionChange = (selectedFunction) => {
        setSelectedFunction(selectedFunction);
        setInputValue('');
        setOutputValue('');
        setInputType('string');
        setOutputType('string');
        setSelectedTestIndex(null);
    };

    // Handle creating a new function
    const handleCreateNewFunction = () => {
        let newFunctionName = prompt('Enter the name for the new function:', 'function_name');

        if (newFunctionName) {
            // Regular expression to match valid Python function names
            const validFunctionNameRegex = /^[a-zA-Z_]\w*$/;

            if (!validFunctionNameRegex.test(newFunctionName)) {
                alert('Invalid function name! Function names must start with a letter or underscore and can only contain letters, digits, or underscores.');
                return;
            }

            const updatedTests = { ...tests };

            if (!updatedTests[selectedProject]) {
                updatedTests[selectedProject] = {};
            }

            // Check if the function name already exists
            if (updatedTests[selectedProject][newFunctionName]) {
                alert(`Function "${newFunctionName}" already exists! Please enter a different name.`);
                return;
            }

            updatedTests[selectedProject][newFunctionName] = [];
            updateTestsAndSave(updatedTests, onTestsChange);

            setSelectedFunction(newFunctionName);
        }
    };


    // Update selected function when tests or selected project change
    useEffect(() => {
        // Check if the selected function exists in the current project
        if (selectedProject && !functions.includes(selectedFunction)) {
            setSelectedFunction('');
        }
    }, [tests, selectedProject, selectedFunction, functions]);

    // Handle deleting selected function with confirmation
    const handleDeleteFunction = () => {
        if (window.confirm(`Are you sure you want to delete the function "${selectedFunction}" and all its tests?`)) {
            const updatedTests = { ...tests };
            delete updatedTests[selectedProject][selectedFunction];
            updateTestsAndSave(updatedTests, onTestsChange);
            setSelectedFunction('');
        }
    };

    return (
        <div>
            <div>
                <div className='test-editor'>
                    <label>
                        Select Project:
                        <select className="tests-select" value={selectedProject} onChange={(e) => handleProjectChange(e.target.value)}>
                            <option value="">Select Project</option>
                            {projects
                                .sort((a, b) => idToNameMap[a].localeCompare(idToNameMap[b])) // Sort by project name
                                .map(projectId => (
                                    <option key={projectId} value={projectId}>
                                        {idToNameMap[projectId]}
                                    </option>
                                ))
                            }
                        </select>

                    </label>
                </div>

                {selectedProject && (
                    <div className="flex-container">
                        <div className="inline-block">
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
                        <div className="auto-margin-left">
                            {selectedFunction && <button className='tests-button tests-button-delete' onClick={handleDeleteFunction}>Delete Function</button>}
                            <button className='tests-button' onClick={handleCreateNewFunction}>Add New Function</button>
                        </div>
                    </div>
                )}

            </div>


            {selectedFunction && (
                <div>
                    <br />
                    <h3 className="h3-center">Test cases</h3>
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
                    <input className="input-field-tests" type="text" value={inputValue} onChange={(e) => setInputValue(e.target.value)} />
                    <select className="tests-select" value={inputType} onChange={(e) => setInputType(e.target.value)}>
                        <option value="string">String</option>
                        <option value="integer">Integer</option>
                        <option value="float">Float</option>
                        <option value="list">List</option>
                        <option value="dictionary">Dictionary</option>
                        <option value="tuple">Tuple</option>
                        <option value="boolean">Boolean</option>
                        {/* Add other data types as needed */}
                    </select>

                    <label>Output:</label>
                    <input className="input-field-tests" type="text" value={outputValue} onChange={(e) => setOutputValue(e.target.value)} />
                    <select className="tests-select" value={outputType} onChange={(e) => setOutputType(e.target.value)}>
                        <option value="string">String</option>
                        <option value="integer">Integer</option>
                        <option value="float">Float</option>
                        <option value="list">List</option>
                        <option value="dictionary">Dictionary</option>
                        <option value="tuple">Tuple</option>
                        <option value="boolean">Boolean</option>
                        {/* Add other data types as needed */}
                    </select>
                    <div className='save-button'>
                        <button onClick={handleSaveTest}>{selectedTestIndex !== null ? 'Save changes' : 'Add new Test'}</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default TestEditor;
