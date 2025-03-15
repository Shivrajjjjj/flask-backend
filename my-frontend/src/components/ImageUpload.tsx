// src/components/ImageUpload.tsx
import React, { useState } from 'react';
import { uploadImage } from '../services/api';

interface ImageUploadProps {
  token: string;
}

const ImageUpload: React.FC<ImageUploadProps> = ({ token }) => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (file && token) {
      try {
        await uploadImage(file, token);
        alert('Image uploaded successfully');
      } catch (error) {
        console.error('Upload failed:', error);
      }
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default ImageUpload;