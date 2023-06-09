import React, { useState } from 'react';
import '../Image/image.css'

const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [imagePath, setImagePath] = useState('');
  const [results, setResults] = useState([]);
  const [Growth, setGrowth] = useState([]);
  const [soil, setSoil] = useState([]);
  const [health, setHealth] = useState([]);
  

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
        console.log("data: ",data)
        console.log("results:" ,data.results)
        // setResults(data.results);
        setSoil(data.results[0]);
        setGrowth(data.results[1]);
        setHealth(data.results[2]);
      } else {
        console.log('Failed to fetch results');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className='topdiv'>
      <form onSubmit={handleSubmit} >
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit" className='upload-img'>Upload</button>
        <button type='button' className='upload'
            onClick={(e) => {
            e.preventDefault();
            if (typeof window !== 'undefined') {
                window.location.href = "http://192.168.90.239/";
            }
            }}>Live Stream
        </button>
      </form>
      {uploadStatus && <p style={{color:'green', fontSize:'bold'}}>{uploadStatus}</p>}
      <div className='imageview'>
    {selectedFile && <img src={URL.createObjectURL(selectedFile)} alt="Uploaded" style={{maxWidth:'100%'} {maxHeight:100}} />}

      </div >
      <div className='predict'>
        {soil && <p className='soil'>  {soil}</p>}
        {Growth && <p className='growth'> {Growth}</p>}
      </div>
      {/* {results && <p>{results}</p>} */}
      {/* {health && <p>Health of plant: {health}</p>} */}
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