import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Footer from '../components/Footer';
import '../styles/style.css';

const ChangePassword = () => {
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChangePassword = (e) => {
    e.preventDefault();

    // Validação básica
    if (newPassword !== confirmPassword) {
      setError('As senhas não coincidem.');
      return;
    }

    if (newPassword.length < 6) {
      setError('A senha deve ter pelo menos 6 caracteres.');
      return;
    }

    // Simulação de atualização de senha
    // Aqui você pode adicionar a lógica para atualizar a senha no backend
    console.log('Nova senha:', newPassword);

    // Marca que o primeiro login foi concluído
    localStorage.setItem('isFirstLogin', 'false');

    // Redireciona para a página inicial
    navigate('/Initial');
  };

  return (
    <div className="page-container d-flex flex-column min-vh-100">
      <div className="container align-items-center px-4 py-5">
        <div className="form-signin m-auto my-5">
          <form onSubmit={handleChangePassword}>
            <div className="text-center">
              <img className="mb-4" width="200" height="auto" src="assets/logo.png" alt="Logo" />
            </div>
            <div className="text-center align-center">
              <h1 className="h3 mb-3 fw-normal">Mudar Senha</h1>
              {error && <div className="alert alert-danger">{error}</div>}
              <div className="form-floating form-w mx-auto">
                <input
                  type="password"
                  className="form-control"
                  id="newPassword"
                  placeholder="Nova Senha"
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  required
                />
                <label htmlFor="newPassword">Nova Senha</label>
              </div>
              <div className="form-floating form-w mx-auto mt-3">
                <input
                  type="password"
                  className="form-control"
                  id="confirmPassword"
                  placeholder="Confirmar Senha"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  required
                />
                <label htmlFor="confirmPassword">Confirmar Senha</label>
              </div>
              <button className="btn btn-primary form-w mt-3" type="submit">
                Alterar Senha
              </button>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default ChangePassword;