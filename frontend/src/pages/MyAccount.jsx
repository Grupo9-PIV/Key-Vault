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

  // Função para atualizar a foto de perfil
  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setUser((prevUser) => ({
          ...prevUser,
          profileImage: reader.result,
        }));
      };
      reader.readAsDataURL(file);
    }
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
                <div className="text-center mb-4">
                  <img
                    src={user.profileImage}
                    alt="Foto de Perfil"
                    className="rounded-circle"
                    width="150"
                    height="150"
                  />
                  {isEditing && (
                    <div className="mt-3">
                      <input
                        type="file"
                        accept="image/*"
                        onChange={handleImageChange}
                        className="form-control"
                      />
                    </div>
                  )}
                </div>

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
                      disabled={!isEditing}
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
                      disabled={!isEditing}
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
                      disabled={!isEditing}
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