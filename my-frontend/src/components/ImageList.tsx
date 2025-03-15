// src/components/ImageList.tsx
import React, { useState, useEffect } from 'react';
import { getImageList } from '../services/api';

interface ImageListProps {
  token: string;
}

const ImageList: React.FC<ImageListProps> = ({ token }) => {
  const [images, setImages] = useState<any[]>([]);

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const data = await getImageList(token);
        setImages(data.images);
      } catch (error) {
        console.error('Failed to fetch images:', error);
      }
    };
    fetchImages();
  }, [token]);

  return (
    <div>
      {images.map((image) => (
        <div key={image.file_name}>
          <p>{image.file_name}</p>
        </div>
      ))}
    </div>
  );
};

export default ImageList;