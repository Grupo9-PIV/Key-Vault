import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/index'; // Importe a API
import Footer from '../components/Footer';
import '../styles/style.css';

const ChangePassword = () => {
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChangePassword = async (e) => {
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

    try {
      const token = localStorage.getItem('token');
      const userId = localStorage.getItem('user_id'); // Obtém o ID do usuário logado

      // Envia a nova senha para o backend
      const response = await api.patch(
        `/users/${userId}`,
        { password: newPassword },
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      if (response.status === 200) {
        alert('Senha alterada com sucesso!');
        navigate('/login'); // Redireciona para a tela de login após a alteração
      } else {
        setError('Erro ao alterar a senha. Tente novamente.');
      }
    } catch (error) {
      console.error('Erro ao alterar a senha:', error);
      if (error.response?.status === 401) {
        alert('Sessão expirada, faça login novamente.');
        localStorage.removeItem('token');
        navigate('/login');
      }
      setError('Erro ao alterar a senha. Verifique sua conexão e tente novamente.');
    }
  };

  const handleCancel = () => {
    navigate('/login'); // Redireciona para a tela de login ao cancelar
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
              <div className="d-flex gap-2 justify-content-center mt-3">
                <button className="btn btn-primary form-w" type="submit">
                  Alterar Senha
                </button>
                <button
                  className="btn btn-secondary form-w"
                  type="button"
                  onClick={handleCancel}
                >
                  Cancelar
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default ChangePassword;