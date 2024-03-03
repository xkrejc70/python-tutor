import axios from 'axios';
import api from 'ServerConfig'

export const fetchDataFromAPI = (setData, setSelectedItems, setStatus) => {
    fetch(api.GET_PROJECTS)
        .then(response => response.json())
        .then(data => {
            const updatedItems = data.map(item => ({
                ...item,
                checked: item.checked || false,
            }));
            setData(updatedItems);

            const initiallyCheckedItems = updatedItems.filter(item => item.checked);
            setSelectedItems(initiallyCheckedItems);
        })
        .catch(error => {
            setStatus('Error fetching data');
        });
};

export const handleCheckboxChange = (item, items, setItems, setSelectedItems) => {
    const updatedItems = items.map(i => {
        if (i.id === item.id) {
            return { ...i, checked: !i.checked };
        }
        return i;
    });

    setItems(updatedItems);

    const updatedSelectedItems = updatedItems.filter(i => i.checked);
    setSelectedItems(updatedSelectedItems);
};

export const handleSaveData = (selectedItems, setStatus) => {
    const dataToSend = selectedItems.map(item => ({
        checked: item.checked,
        id: item.id,
        info: item.info,
        name: item.name,
    }));

    axios.post(api.SAVE_SETTINGS, dataToSend)
        .then(response => {
            if (response.status === 200) {
                setStatus('Settings saved');
            } else {
                setStatus(`Error: ${response.data}`);
            }
        })
        .catch(error => {
            if (error.response) {
                setStatus(`Error: ${error.response.data.error}`);
            } else if (error.request) {
                setStatus('Error: No response received from the server');
            } else {
                setStatus(`Error: ${error.message}`);
            }
        });
};
