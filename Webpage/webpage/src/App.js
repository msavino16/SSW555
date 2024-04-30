import React from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const handleRunNotebook = async () => {
    const response = await axios.post('http://localhost:5000/run-notebook');
    alert(response.data);
  };

  return (
    <div>
      <div className="container">
      <h1 className="title">EEG Source Imaging</h1>
      <form>
      <label for="file">File</label>
      <input id="file" type="file" />
      <input type="submit"/>
      </form>
      <button className="generateButton" onClick={handleRunNotebook}>
        Generate Pop-Up Imaging
      </button>
    </div>
    </div>
  );
}

export default App;

