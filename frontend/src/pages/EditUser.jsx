import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../api/index';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const EditUser = () => {
  const { userId } = useParams(); // Captura o userId da URL
  const navigate = useNavigate();
  const [user, setUser] = useState({
    name: '',
    email: '',
    role: '',
    department: '',
    password: undefined, // Evita sobrescrever senha por acidente
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  console.log('ID do usuário:', userId); // Log para depuração

  useEffect(() => {
    if (!userId) {
      console.error('ID do usuário não encontrado na URL.');
      setError('ID do usuário não encontrado.');
      setLoading(false);
      return;
    }

    const fetchUser = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await api.get(`/users/${userId}`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        setUser({
          name: response.data.name,
          email: response.data.email,
          role: response.data.role,
          department: response.data.department,
          password: undefined, // Mantém undefined para evitar envio de senha vazia
        });
        setLoading(false);
      } catch (error) {
        console.error('Erro ao buscar usuário:', error);
        if (error.response?.status === 401) {
          alert('Sessão expirada, faça login novamente.');
          localStorage.removeItem('token');
          navigate('/login');
        }
        setError('Erro ao carregar os dados do usuário.');
        setLoading(false);
      }
    };

    fetchUser();
  }, [userId, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const updatedUser = {
        name: user.name,
        email: user.email,
        role: user.role,
        department: user.department,
      };
      if (user.password) {
        updatedUser.password = user.password;
      }

      await api.patch(`/users/${userId}`, updatedUser, {
        headers: { Authorization: `Bearer ${token}` },
      });
      alert('Usuário atualizado com sucesso!');
      navigate('/users');
    } catch (error) {
      console.error('Erro ao atualizar usuário:', error);
      if (error.response?.status === 401) {
        alert('Sessão expirada, faça login novamente.');
        localStorage.removeItem('token');
        navigate('/login');
      }
      setError('Erro ao atualizar usuário.');
    }
  };

  const handleChange = (e) => {
    const { id, value } = e.target;
    setUser((prevUser) => ({
      ...prevUser,
      [id]: value,
    }));
  };

  if (loading) return <p>Carregando...</p>;

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Editar Usuário</h2>
        {error && <div className="alert alert-danger">{error}</div>}
        <div className="py-5">
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="name" className="form-label">Nome</label>
              <input type="text" className="form-control" id="name" value={user.name} onChange={handleChange} />
            </div>
            <div className="mb-3">
              <label htmlFor="email" className="form-label">E-mail</label>
              <input type="email" className="form-control" id="email" value={user.email} onChange={handleChange} />
            </div>
            <div className="mb-3">
              <label htmlFor="password" className="form-label">Nova Senha (opcional)</label>
              <input type="password" className="form-control" id="password" value={user.password || ''} onChange={handleChange} />
            </div>
            <div className="mb-3">
              <label htmlFor="role" className="form-label">Função</label>
              <input type="text" className="form-control" id="role" value={user.role} onChange={handleChange} />
            </div>
            <div className="mb-3">
              <label htmlFor="department" className="form-label">Departamento</label>
              <input type="text" className="form-control" id="department" value={user.department} onChange={handleChange} />
            </div>
            <div className="d-flex gap-2">
              <button type="submit" className="btn btn-primary">Salvar</button>
              <button type="button" className="btn btn-secondary" onClick={() => navigate('/users')}>
                Cancelar
              </button>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
}; //commit

export default EditUser;