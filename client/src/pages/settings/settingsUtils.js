import axios from 'axios';

export const fetchDataFromAPI = (setData, setSelectedItems, setStatus) => {
    fetch('http://localhost:5005/api/projects')
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
            console.error('Error fetching data:', error);
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

    axios.post('http://localhost:5005/api/admin/save', dataToSend)
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
            } else {
                setStatus(`Error: ${error.response.data}`);
            }
        });
};
