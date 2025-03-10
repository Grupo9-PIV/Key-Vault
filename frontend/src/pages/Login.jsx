import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Footer from '../components/Footer';
import '../styles/style.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();

    // Simulação de autenticação
    if (username === 'admin' && password === 'admin') {
      // Verifica se é o primeiro login
      const isFirstLogin = localStorage.getItem('isFirstLogin') === 'true';

      if (isFirstLogin) {
        navigate('/ChangePassword'); // Redireciona para a tela de mudança de senha
      } else {
        navigate('/Initial'); // Redireciona para a página inicial
      }

      // Marca o usuário como autenticado
      localStorage.setItem('isAuthenticated', 'true');
    } else {
      alert('Usuário ou senha incorretos');
    }
  };

  return (
    <div className="page-container d-flex flex-column min-vh-100">
      <div className="container align-items-center px-4 py-5">
        <div className="form-signin m-auto my-5">
          <form>
            <div className="text-center">
              <img className="mb-4" width="200" height="auto" src="assets/logo.png" alt="Logo"/>
            </div>
            <div className="text-center align-center">
              <h1 className="h3 mb-3 fw-normal">Login</h1>
              <div className="form-floating form-w mx-auto">
                <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com"/>
                <label for="floatingInput">E-mail</label>
              </div>
              <div class="form-floating form-w mx-auto mt-3">
                <input type="password" className="form-control" id="floatingPassword" placeholder="Password"/>
                <label for="floatingPassword">Senha</label>
              </div>
              <div className="form-check mx-auto mt-3 text-start" style={{ maxWidth: '280px' }}>
                <input className="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault"/>
                <label className="form-check-label" htmlFor="flexCheckDefault">
                  Manter conectado
                </label>
              </div>
              <button className="btn btn-primary form-w mt-3" type="submit">
                Conectar
              </button>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
};


export default Login;