import React, { useState } from 'react';
import { Link } from 'react-router-dom';

import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const MyAccount = () => {
  // Estado para armazenar os dados do usuário
  const [user, setUser] = useState({
    name: 'User Teste',
    email: 'user.teste@empresa.com',
    department: 'TI',
    password: '', // Adicionando campo de senha
    profileImage: 'https://github.com/mdo.png', // URL da imagem de perfil
  });

  // Estado para controlar a edição
  const [isEditing, setIsEditing] = useState(false);

  // Função para salvar as alterações
  const handleSave = () => {
    setIsEditing(false);
    // Aqui você pode adicionar lógica para salvar os dados no backend
    console.log('Dados salvos:', user);
  };

  // Função para atualizar o estado do usuário
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
};

export default MyAccount;