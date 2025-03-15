// src/pages/Login.tsx
import { useState } from "react";
import LoginForm from '../components/LoginForm';

const Login = () => {
  const [token, setToken] = useState<string | null>(null);

  const handleLoginSuccess = (token: string) => {
    setToken(token);
    localStorage.setItem('token', token);
  };

  return (
    <div>
      {token ? <p>Logged in!</p> : <LoginForm onLoginSuccess={handleLoginSuccess} />}
    </div>
  );
};

export default Login;