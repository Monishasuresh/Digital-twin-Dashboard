import React, { useRef } from 'react';

const ImageUploader = () => {
  const fileInputRef = useRef(null);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    // Do something with the uploaded file
    console.log(file);
  };

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  return (
    <div>
      <input
        type="file"
        accept="image/*"
        ref={fileInputRef}
        style={{ display: 'none' }}
        onChange={handleFileUpload}
      />
      <button onClick={handleButtonClick}>
        Upload Image
      </button>
    </div>
  );
};

export default ImageUploader;
