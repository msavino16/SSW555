import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleRunNotebook = async () => {
    if (!selectedFile) {
      alert('Please select a file');
      return;
    }

    const fileExtension = selectedFile.name.split('.').pop();
    if (fileExtension !== 'fif') {
      alert('Only .fif files are allowed');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://localhost:5000/run-notebook', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      alert(response.data);
    } catch (error) {
      alert('An error occurred while uploading the file');
      console.error(error);
    }
  };

  return (
    <div>
      <div className="container">
        <h1 className="title">EEG Source Imaging</h1>
        <form>
          <label htmlFor="file">File</label>
          <input id="file" type="file" onChange={handleFileChange} />
        </form>
        <button className="generateButton" onClick={handleRunNotebook}>
          Generate Pop-Up Imaging
        </button>
      </div>
    </div>
  );
}

export default App;
