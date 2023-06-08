import React, { useState } from 'react';
import axios from 'axios';

const MyComponent = () => {
  const [image, setImage] = useState(null);
  const [results, setResults] = useState([]);
  
  const handleFileUpload = (event) => {
    const uploadedFile = event.target.files[0];
    setImage(uploadedFile);
  };

  const handleSubmit = () => {
    if (image) {
      const formData = new FormData();
      formData.append('image', image);

      axios.post('/api/upload', formData)
        .then((response) => {
          const { imagePath } = response.data;
          runPythonScript(imagePath);
        })
        .catch((error) => {
          console.error('Error uploading image:', error);
        });
    }
  };

  const runPythonScript = (imagePath) => {
    axios.post('/api/python', { imagePath })
      .then((response) => {
        const { results } = response.data;
        setResults(results);
      })
      .catch((error) => {
        console.error('Error running Python script:', error);
      });
  };

  return (
    <div>
      <input type="file" onChange={handleFileUpload} />
      <button onClick={handleSubmit}>Upload and Run Python Script</button>
      {results.map((result, index) => (
        <p key={index}>{result}</p>
      ))}
      {image && <img src={URL.createObjectURL(image)} alt="Uploaded" />}
    </div>
  );
};


export default MyComponent;
