// src/pages/Upload.tsx
import ImageUpload from '../components/ImageUpload';
import ImageList from '../components/ImageList';

const Upload = () => {
  const token = localStorage.getItem('token');
  if (!token) {
    return <p>Please login to upload images.</p>;
  }

  return (
    <div>
      <ImageUpload token={token} />
      <ImageList token={token} />
    </div>
  );
};

export default Upload;