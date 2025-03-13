import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom'; // Importe o Link do react-router-dom
import Footer from '../components/Footer';
import '../styles/style.css';
import api from '../api/index';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      console.log('Dados enviados:', { username, password }); // Log dos dados enviados

      const response = await api.post(
        '/auth/token',
        {
          username: username,
          password: password,
          grant_type: 'password',
          client_id: 'string',
          client_secret: 'string',
        },
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        }
      );

      console.log('Resposta do backend:', response.data); // Log da resposta

      if (response.data && response.data.access_token) {
        localStorage.setItem('token', response.data.access_token);
        localStorage.setItem('user_id', response.data.user_id);
        const isFirstLogin = false; // 
        if (isFirstLogin) {
          navigate('/ChangePassword');
        } else {
          navigate('/Initial');
        }
      } else {
        alert('Usuário ou senha incorretos');
      }
    } catch (error) {
      console.error('Erro completo:', error); // Log do erro completo
      console.error('Resposta de erro:', error.response); // Log da resposta de erro
      alert('Erro ao fazer login. Verifique suas credenciais e tente novamente.');
    }
  };

  return (
    <div className="page-container d-flex flex-column min-vh-100">
      <div className="container align-items-center px-4 py-5">
        <div className="form-signin m-auto my-5">
          <form onSubmit={handleLogin}>
            <div className="text-center">
              <img className="mb-4" width="200" height="auto" src="assets/logo.png" alt="Logo" />
            </div>
            <div className="text-center align-center">
              <h1 className="h3 mb-3 fw-normal">Login</h1>
              <div className="form-floating form-w mx-auto">
                <input
                  type="email"
                  className="form-control"
                  id="floatingInput"
                  placeholder="name@example.com"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
                <label htmlFor="floatingInput">E-mail</label>
              </div>
              <div className="form-floating form-w mx-auto mt-3">
                <input
                  type="password"
                  className="form-control"
                  id="floatingPassword"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
                <label htmlFor="floatingPassword">Senha</label>
              </div>
              <div className="form-check mx-auto mt-3 text-start" style={{ maxWidth: '280px' }}>
                <input
                  className="form-check-input"
                  type="checkbox"
                  value="remember-me"
                  id="flexCheckDefault"
                />
                <label className="form-check-label" htmlFor="flexCheckDefault">
                  Manter conectado
                </label>
              </div>
              <button className="btn btn-primary form-w mt-3" type="submit">
                Conectar
              </button>

              {/* Link para "Esqueceu sua senha?" */}
              <div className="mt-3">
                <Link to="/changepassword" className="text-decoration-none">
                  Esqueceu sua senha?
                </Link>
              </div>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
}; //commit

export default Login;