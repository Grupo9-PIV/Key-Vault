import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const AddUser = () => {
  // Estado para o ID do usuário
  const [userId, setUserId] = useState('');

  // Estado para os dados do usuário
  const [user, setUser] = useState({
    id: '',
    name: '',
    email: '',
    department: '',
  });

  // Função para buscar os dados do usuário ao inserir o ID
  const handleUserIdChange = (e) => {
    const id = e.target.value;
    setUserId(id);

    // Simulação de busca de dados do usuário a partir do ID
    if (id === '1') {
      setUser({
        id: id,
        name: 'Ewellyn Almeida',
        email: 'lynn@gmail.com',
        department: 'TI',
      });
    } else if (id === '2') {
      setUser({
        id: id,
        name: 'João Silva',
        email: 'joao@gmail.com',
        department: 'RH',
      });
    } else {
      // Limpa os campos se o ID não for reconhecido
      setUser({
        id: '',
        name: '',
        email: '',
        department: '',
      });
    }
  };

  // Função para adicionar o usuário
  const handleAddUser = (e) => {
    e.preventDefault();
    console.log('Usuário adicionado:', user);
    // Aqui você pode adicionar a lógica para salvar o usuário no backend
  };

  // Função para cancelar a adição de usuário
  const handleCancel = () => {
    console.log('Adição de usuário cancelada');
    // Aqui você pode adicionar a lógica para redirecionar ou limpar o formulário
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Adicionar Usuário</h2>
        <div className="py-5">
          <form onSubmit={handleAddUser}>
            <div className="mb-3">
              <label htmlFor="userId" className="form-label">
                ID do Usuário
              </label>
              <input
                type="text"
                className="form-control"
                id="userId"
                name="userId"
                value={userId}
                onChange={handleUserIdChange}
                required
              />
            </div>
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
                disabled
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
                disabled
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
                disabled
              />
            </div>
            <div className="d-flex gap-2">
              <button type="submit" className="btn btn-primary">
                Adicionar
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={handleCancel}
              >
                Cancelar
              </button>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default AddUser;