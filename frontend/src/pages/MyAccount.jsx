import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/index';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const MyAccount = () => {
  const navigate = useNavigate();
  const [user, setUser] = useState({
    name: 'User Teste',
    email: 'user.teste@empresa.com',
    department: 'TI',
    password: '', // Adicionando campo de senha
    profileImage: 'https://github.com/mdo.png', // URL da imagem de perfil
  });
  const [isEditing, setIsEditing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchUserData = async () => {
      const userId = localStorage.getItem('user_id'); // Obtém o ID do usuário logado
      if (!userId) {
        setError('Usuário não autenticado.');
        setLoading(false);
        navigate('/login'); 
        return;
      }

      try {
        const token = localStorage.getItem('token');
        const response = await api.get(`/users/${userId}`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        setUser({
          name: response.data.name,
          email: response.data.email,
          department: response.data.department,
        });
        setLoading(false);
      } catch (error) {
        console.error('Erro ao buscar dados do usuário:', error);
        setError('Erro ao carregar dados do usuário.');
        setLoading(false);
        if (error.response?.status === 401) {
          alert('Sessão expirada, faça login novamente.');
          localStorage.removeItem('token');
          localStorage.removeItem('user_id');
          navigate('/login');
        }
      }
    };

    fetchUserData();
  }, [navigate]);

  const handleSave = async () => {
    const userId = localStorage.getItem('user_id');
    if (!userId) {
      setError('Usuário não autenticado.');
      return;
    }

    try {
      const token = localStorage.getItem('token');
      const updatedUser = {
        name: user.name,
        email: user.email,
        department: user.department,
      };

      await api.patch(`/users/${userId}`, updatedUser, {
        headers: { Authorization: `Bearer ${token}` },
      });

      setIsEditing(false);
      alert('Dados atualizados com sucesso!');
    } catch (error) {
      console.error('Erro ao atualizar dados do usuário:', error);
      setError('Erro ao atualizar dados do usuário.');
      if (error.response?.status === 401) {
        alert('Sessão expirada, faça login novamente.');
        localStorage.removeItem('token');
        localStorage.removeItem('user_id');
        navigate('/login');
      }
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUser((prevUser) => ({
      ...prevUser,
      [name]: value,
    }));
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-md-8">
            <div className="card">
              <div className="card-header">
                <h3 className="card-title">Minha Conta</h3>
              </div>
              <div className="card-body">
                <form>
                  <div className="mb-3">
                    <label htmlFor="name" className="form-label">
                      Nome
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      id="name"
                      name="name"
                      value={user.name}
                      onChange={handleChange}
                      disabled={!isEditing} // Editável apenas quando isEditing for true
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="email" className="form-label">
                      E-mail
                    </label>
                    <input
                      type="email"
                      className="form-control"
                      id="email"
                      name="email"
                      value={user.email}
                      onChange={handleChange}
                      disabled // Sempre desabilitado
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="department" className="form-label">
                      Departamento
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      id="department"
                      name="department"
                      value={user.department}
                      onChange={handleChange}
                      disabled // Sempre desabilitado
                    />
                  </div>

                  <div className="mb-3">
                    <label htmlFor="password" className="form-label">
                      Senha
                    </label>
                    <input
                      type="password"
                      className="form-control"
                      id="password"
                      name="password"
                      value={user.password}
                      onChange={handleChange}
                      disabled={!isEditing} // Editável apenas quando isEditing for true
                    />
                  </div>

                  <div className="d-flex justify-content-end">
                    {isEditing ? (
                      <>
                        <button
                          type="button"
                          className="btn btn-secondary me-2"
                          onClick={() => setIsEditing(false)}
                        >
                          Cancelar
                        </button>
                        <button
                          type="button"
                          className="btn btn-primary"
                          onClick={handleSave}
                        >
                          Salvar
                        </button>
                      </>
                    ) : (
                      <button
                        type="button"
                        className="btn btn-primary"
                        onClick={() => setIsEditing(true)}
                      >
                        Editar
                      </button>
                    )}
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}; //commit

export default MyAccount;