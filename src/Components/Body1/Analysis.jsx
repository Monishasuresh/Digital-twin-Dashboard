import React, { useState } from 'react';

const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [imagePath, setImagePath] = useState('');
  const [results, setResults] = useState([]);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (selectedFile) {
      const formData = new FormData();
      formData.append('image', selectedFile);

      try {
        const response = await fetch('http://127.0.0.1:5000/api/upload-image', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const data = await response.json();
          setUploadStatus('Image uploaded successfully');
          setImagePath(data.imagePath);
          fetchResults(data.imagePath);
          console.log(response)
        } else {
          setUploadStatus('Failed to upload image');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
  };

  const fetchResults = async (imagePath) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/process-image', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ imagePath }),
      });

      if (response.ok) {
        const data = await response.json();
        setResults(data.results);
      } else {
        console.log('Failed to fetch results');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {uploadStatus && <p>{uploadStatus}</p>}
      {selectedFile && <img src={URL.createObjectURL(selectedFile)} alt="Uploaded" />}
      {/* {imagePath && (
        <div>

          <img src={imagePath} alt="Uploaded" />
          {results.length > 0 && (
            <ul>
              {results.map((result, index) => (
                <li key={index}>{result}</li>
              ))}
            </ul>
          )}
        </div>
      )} */}
    </div>
  );
};

export default ImageUpload;