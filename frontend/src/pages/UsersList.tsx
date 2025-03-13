import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../api/index';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

interface User {
  id: number;
  name: string;
  email: string;
  role: string;
  department: string;
  is_active: boolean;
}

const UserList = () => {
  useEffect(() => {
    document.title = 'Lista de Usuários';
  }, []);

  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchId, setSearchId] = useState('');
  const [error, setError] = useState('');

  const fetchUsers = () => {
    setLoading(true);
    setError('');
    
    let url = '/users/?skip=0&limit=10';
    
    if (searchId) {
      url = `/users/${searchId}`;
    }

    api.get(url, {
      headers: {
        requiresAuth: true,
      },
    })
      .then((response) => {
        if (searchId) {
          // Se estiver buscando por ID, transforma o objeto em um array
          setUsers([response.data]);
        } else {
          setUsers(response.data.users);
        }
        setError('');
      })
      .catch(() => {
        if (searchId) {
          setError('ID de usuário não encontrada.');
          setUsers([]);
        } else {
          setError('Erro ao carregar usuários.');
        }
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    fetchUsers();
  };

  const handleDelete = async (userId: number) => {
    const confirmDelete = window.confirm('Tem certeza que deseja excluir este usuário?');

    if (confirmDelete) {
      try {
        await api.delete(`/users/${userId}`, {
          headers: {
            requiresAuth: true,
          },
        });

        setUsers(users.filter((user) => user.id !== userId));
        alert('Usuário excluído com sucesso!');
      } catch (error) {
        console.error('Erro ao excluir usuário:', error);
        alert('Erro ao excluir usuário.');
      }
    }
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <header className="d-flex justify-content-between py-3 align-items-center">
          <div>
            <Link to="/createuser" className="nav-link">
              <button className="btn btn-dark me-2">Criar usuário</button>
            </Link>
          </div>
          <div>
            <form className="w-100 me-3" onSubmit={handleSearch}>
              <input
                type="text"
                className="form-control ms-2"
                placeholder="Buscar por ID..."
                value={searchId}
                onChange={(e) => setSearchId(e.target.value)}
              />
              <button type="submit" className="btn btn-primary mt-2">Buscar</button>
            </form>
          </div>
        </header>
      </div>

      <div className="container">
        <h2>Lista de Usuários</h2>

        {loading ? (
          <p>Carregando...</p>
        ) : error ? (
          <p style={{ color: 'red' }}>{error}</p>
        ) : (
          <div className="table-responsive small">
            <table className="table table-striped table-sm dropdown">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nome</th>
                  <th>E-mail</th>
                  <th>Papel</th>
                  <th>Departamento</th>
                  <th>Ativo</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {users.map((user) => (
                  <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{user.name}</td>
                    <td>{user.email}</td>
                    <td>{user.role}</td>
                    <td>{user.department}</td>
                    <td>{user.is_active ? 'Sim' : 'Não'}</td>
                    <td>
                      <Link className="btn btn-sm btn-warning me-2" to={`/users/${user.id}/edituser`}>
                        Editar
                      </Link>
                      <button className="btn btn-sm btn-danger" onClick={() => handleDelete(user.id)}>
                        Excluir
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      <Footer />
    </div>
  );
};

export default UserList;
