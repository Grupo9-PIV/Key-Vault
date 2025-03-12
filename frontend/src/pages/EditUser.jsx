import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const EditUser = () => {
  // Estado para os dados do usuário
  const [user, setUser] = useState({
    name: 'Ewellyn Almeida',
    email: 'lynn@gmail.com',
    role: 'Admin',
    department: 'TI',
  });

  // Estado para a lista de licenças do usuário
  const [licenses, setLicenses] = useState([
    {
      id: 1,
      softwareName: 'Software XYZ',
      licenseType: 'assinatura',
      version: '1.0.0',
      status: 'ativa',
      key: 'ABC123-XYZ456',
    },
    {
      id: 2,
      softwareName: 'Software ABC',
      licenseType: 'perpétua',
      version: '2.0.0',
      status: 'expirada',
      key: 'DEF456-GHI789',
    },
  ]);

  // Estado para o formulário de adição de nova licença
  const [newLicense, setNewLicense] = useState({
    softwareName: '', // Único campo editável pelo usuário
    licenseType: '',
    version: '',
    status: '',
    key: '',
  });

  // Função para atualizar os dados do usuário
  const handleUserChange = (e) => {
    const { name, value } = e.target;
    setUser((prevUser) => ({
      ...prevUser,
      [name]: value,
    }));
  };

  // Função para salvar as alterações do usuário
  const handleSaveUser = (e) => {
    e.preventDefault();
    console.log('Dados do usuário salvos:', user);
  };

  // Função para excluir uma licença
  const handleDeleteLicense = (id) => {
    setLicenses(licenses.filter((license) => license.id !== id));
  };

  // Função para adicionar uma nova licença
  const handleAddLicense = (e) => {
    e.preventDefault();
    const newId = licenses.length > 0 ? licenses[licenses.length - 1].id + 1 : 1; // Gera um novo ID
    const licenseToAdd = { ...newLicense, id: newId };
    setLicenses([...licenses, licenseToAdd]);
    setNewLicense({
      softwareName: '',
      licenseType: '',
      version: '',
      status: '',
      key: '',
    });
  };

  // Função para simular a busca de informações da licença ao selecionar o nome do software
  const handleSoftwareNameChange = (e) => {
    const { value } = e.target;
    setNewLicense((prevLicense) => ({
      ...prevLicense,
      softwareName: value,
    }));

    // Simulação de integração com o backend: busca as informações da licença
    if (value === 'Software XYZ') {
      setNewLicense({
        softwareName: value,
        licenseType: 'assinatura',
        version: '1.0.0',
        status: 'ativa',
        key: 'ABC123-XYZ456',
      });
    } else if (value === 'Software ABC') {
      setNewLicense({
        softwareName: value,
        licenseType: 'perpétua',
        version: '2.0.0',
        status: 'expirada',
        key: 'DEF456-GHI789',
      });
    } else {
      // Limpa os campos se o software não for reconhecido
      setNewLicense({
        softwareName: value,
        licenseType: '',
        version: '',
        status: '',
        key: '',
      });
    }
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Editar Usuário</h2>
        <div className="py-5">
          {/* Formulário de edição do usuário */}
          <div className="mb-5">
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
                onChange={handleUserChange}
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
                onChange={handleUserChange}
                disabled
              />
            </div>
            <form onSubmit={handleSaveUser}>
              <div className="mb-3">
                <label htmlFor="password" className="form-label">
                  Nova Senha
                </label>
                <input
                  type="password"
                  className="form-control"
                  id="password"
                  name="password"
                  placeholder="Digite a nova senha"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="role" className="form-label">
                  Função
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="role"
                  name="role"
                  value={user.role}
                  onChange={handleUserChange}
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
                  onChange={handleUserChange}
                />
              </div>
              <div className="d-flex gap-2">
                <button type="submit" className="btn btn-primary">
                  Salvar
                </button>
                <button type="button" className="btn btn-secondary">
                  Cancelar
                </button>
              </div>
            </form>
          </div>

          {/* Lista de Licenças do Usuário */}
          <div className="mt-5">
            <h3 className="pb-2 border-bottom">Licenças Associadas</h3>
            {/* Formulário para adicionar nova licença */}
            <form onSubmit={handleAddLicense} className="mb-4">
              <h4 className="my-3">Adicionar Nova Licença</h4>
              <div className="row g-3">
                <div className="col-md-6">
                  <label htmlFor="softwareName" className="form-label">
                    Nome do Software
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="softwareName"
                    name="softwareName"
                    value={newLicense.softwareName}
                    onChange={handleSoftwareNameChange}
                    required
                  />
                </div>
                <div className="col-md-6">
                  <label htmlFor="licenseType" className="form-label">
                    Tipo de Licença
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="licenseType"
                    name="licenseType"
                    value={newLicense.licenseType}
                    disabled
                  />
                </div>
                <div className="col-md-6">
                  <label htmlFor="version" className="form-label">
                    Versão
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="version"
                    name="version"
                    value={newLicense.version}
                    disabled
                  />
                </div>
                <div className="col-md-6">
                  <label htmlFor="status" className="form-label">
                    Status
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="status"
                    name="status"
                    value={newLicense.status}
                    disabled
                  />
                </div>
                <div className="col-md-6">
                  <label htmlFor="key" className="form-label">
                    Key
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="key"
                    name="key"
                    value={newLicense.key}
                    disabled
                  />
                </div>
                <div className="col-md-12">
                  <button type="submit" className="btn btn-primary">
                    Adicionar Licença
                  </button>
                </div>
              </div>
            </form>

            {/* Tabela de licenças */}
            <table className="table table-striped">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nome do Software</th>
                  <th>Tipo de Licença</th>
                  <th>Versão</th>
                  <th>Status</th>
                  <th>Key</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {licenses.map((license) => (
                  <tr key={license.id}>
                    <td>{license.id}</td>
                    <td>{license.softwareName}</td>
                    <td>{license.licenseType}</td>
                    <td>{license.version}</td>
                    <td>{license.status}</td>
                    <td>{license.key}</td>
                    <td>
                      <button
                        type="button"
                        className="btn btn-danger btn-sm"
                        onClick={() => handleDeleteLicense(license.id)}
                      >
                        Excluir
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default EditUser;