import React, { useState, useEffect } from 'react';
import { updateModelsandSave } from './testEditorUtils';
import { AiFillDelete } from "react-icons/ai";
import { TbMinusVertical } from "react-icons/tb";
import { FaEdit } from "react-icons/fa";
import 'assets/global.css';

const ModelEditor = ({ models, projs, onModelsChange }) => {
    const [selectedProject, setSelectedProject] = useState('');
    const [selectedTranslationIndex, setSelectedTranslationIndex] = useState(null);
    const [keyValuePairs, setKeyValuePairs] = useState({});
    const [key, setKey] = useState('');
    const [translation, setTranslation] = useState('');

    function getNameById(id) {
        const project = projs.find(proj => proj.id === id);
        return project ? project.name : "Project not found";
    }

    // Populate project dropdown options
    const projects = Object.keys(models);

    // Create an object to store the mapping of projX to names
    const idToNameMap = {};

    // Populate the idToNameMap with the corresponding names
    projects.forEach(id => {
        const numericId = parseInt(id.replace("proj", ""), 10);
        const name = getNameById(numericId);
        idToNameMap[id] = name;
    });

    // Update input values when a translation is selected for modification
    useEffect(() => {
        if (selectedTranslationIndex !== null) {
            const selectedTranslation = keyValuePairs[selectedTranslationIndex];
            setKey(selectedTranslationIndex);
            setTranslation(selectedTranslation);
        } else {
            setKey('');
            setTranslation('');
        }
    }, [selectedTranslationIndex, keyValuePairs]);

    // Update key-value pairs when a project is selected
    useEffect(() => {
        if (selectedProject) {
            setKeyValuePairs(models[selectedProject]?.translations || {});
        }
    }, [selectedProject, models]);


    const handleModelUrlChange = () => {
        let defaultModelName = models[selectedProject]?.model_url || '';
        let model_url = prompt('Enter the name of the model in Hugging Face platform (user/model):', defaultModelName);
    
        if (model_url !== null) {
            // Ensure there is a selected project
            if (selectedProject) {
                // Create a copy of the models object
                const updatedModels = { ...models };
    
                // Check if the selected project exists
                if (!updatedModels[selectedProject]) {
                    updatedModels[selectedProject] = { model_url: '', translations: {} };
                }
    
                // Update the model_url in the selected project
                updatedModels[selectedProject].model_url = model_url === null ? '' : model_url;
    
                // Perform any additional actions (e.g., saving to storage)
                updateModelsandSave(updatedModels, onModelsChange);
            } else {
                console.error("No project selected.");
            }
        }
    };
    
    

    // Handle project selection
    const handleProjectChange = (selectedProject) => {
        setSelectedProject(selectedProject, idToNameMap[selectedProject]);
        setKey('')
        setTranslation('')
        setSelectedTranslationIndex(null);
    };

    // Handle deleting a translation entry
    const handleDeleteTranslation = (key) => {
        // Create a copy of the models object
        const updatedModels = { ...models };

        // Check if the selected project exists
        if (updatedModels[selectedProject]) {
            // Check if the translation key exists in the selected project's translations
            if (updatedModels[selectedProject].translations[key]) {
                // Delete the translation from the copied models object
                delete updatedModels[selectedProject].translations[key];

                // Update the state with the modified models object
                const updatedKeyValuePairs = { ...keyValuePairs };
                delete updatedKeyValuePairs[key];
                setKeyValuePairs(updatedKeyValuePairs);

                // Perform any additional actions (e.g., saving to storage)
                updateModelsandSave(updatedModels, onModelsChange);
            } else {
                console.error("Translation key does not exist in selected project.");
            }
        } else {
            console.error("Selected project does not exist in models.");
        }
    };

    // Handle creating a new translation entry
    const handleSaveModels = () => {
        if (key && translation) {
            const updatedModels = { ...models };
            const updatedKeyValuePairs = { ...keyValuePairs };

            // Update the translations in the copied models object
            if (!updatedModels[selectedProject]) {
                updatedModels[selectedProject] = { translations: {} };
            }
            updatedModels[selectedProject].translations[key] = translation;

            // Update the key-value pairs state
            updatedKeyValuePairs[key] = translation;
            setKeyValuePairs(updatedKeyValuePairs);

            // Perform any additional actions (e.g., saving to storage)
            updateModelsandSave(updatedModels, onModelsChange);

            // Reset key and translation inputs
            setKey('');
            setTranslation('');
            setSelectedTranslationIndex(null);
        } else {
            // You can handle empty key or translation here
            console.error("Key or Translation is empty!");
        }
    };

    return (
        <div>
            <div>
                <div className="flex-container">
                    <div className="inline-block">
                        <label>
                            Select Project:
                            <select className="tests-select" value={selectedProject} onChange={(e) => handleProjectChange(e.target.value)}>
                                <option value="">Select Project</option>
                                {projects.map((id) => (
                                    <option key={id} value={id}>{idToNameMap[id]}</option>
                                ))}
                            </select>
                        </label>
                    </div>
                    {selectedProject && (
                        <div className="auto-margin-left">
                            <button className='tests-button' onClick={handleModelUrlChange}>Edit Model Name</button>
                        </div>
                    )}
                </div>
            </div>
            <br />

            {selectedProject && (
                <div>
                    <div>
                        <table className="tests-table">
                            <thead>
                                <tr>
                                    <th>Classification</th>
                                    <th>Translation</th>
                                    <th>Operations</th>
                                </tr>
                            </thead>
                            <tbody>
                                {Object.entries(keyValuePairs).map(([key, value]) => (
                                    <tr key={key}>
                                        <td>{key}</td>
                                        <td>{value}</td>
                                        <td className='align-r'>
                                            <span className="modify-test" onClick={() => setSelectedTranslationIndex(key)}><FaEdit size={23} /></span>
                                            <TbMinusVertical size={23} />
                                            <span className="delete-text" onClick={() => handleDeleteTranslation(key)}><AiFillDelete size={23} /></span>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>

                    <br />
                    <br />
                    <div>
                        <label>Classification:</label>
                        <input className="input-field-tests" type="text" value={key} onChange={(e) => setKey(e.target.value)} />
                        <label>Translation:</label>
                        <input className="input-field-tests" type="text" value={translation} onChange={(e) => setTranslation(e.target.value)} />
                    </div>
                    <div className='save-button'>
                        <button onClick={handleSaveModels}>{selectedTranslationIndex !== null ? 'Save changes' : 'Add new classification'}</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default ModelEditor;
