import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const EditLicense = () => {
  const [license, setLicense] = useState({
    softwareName: 'Software XYZ',
    manager: 'Gerente ABC',
    licenseType: 'assinatura',
    version: '1.0.0',
    acquisitionDate: '2023-01-01',
    endDate: '2024-01-01',
    status: 'ativa',
    key: 'ABC123-XYZ456',
    userLimit: 100,
    activeUsers: 50,
    plan: 'Plano Premium',
    priority: 'alta',
  });

  const [users, setUsers] = useState([
    { id: 1, name: 'Usuário 1', email: 'usuario1@empresa.com', department: 'TI' },
    { id: 2, name: 'Usuário 2', email: 'usuario2@empresa.com', department: 'RH' },
    { id: 3, name: 'Usuário 3', email: 'usuario3@empresa.com', department: 'Vendas' },
  ]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setLicense((prevLicense) => ({
      ...prevLicense,
      [name]: value,
    }));
  };

  const handleSave = (e) => {
    e.preventDefault();
    console.log('Licença salva:', license);
  };

  // Função para adicionar um novo usuário (simulação)
  const handleAddUser = () => {
    const newUser = {
      id: users.length + 1, // Simula um novo ID
      name: `Usuário ${users.length + 1}`,
      email: `usuario${users.length + 1}@empresa.com`,
      department: 'Novo Departamento', // Valor padrão para o departamento
    };
    setUsers([...users, newUser]);
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Editar Licença</h2>
        <div className="py-5">
          <form onSubmit={handleSave}>
            {/* Nome do Software */}
            <div className="mb-3">
              <label htmlFor="softwareName" className="form-label">
                Nome do Software
              </label>
              <input
                type="text"
                className="form-control"
                id="softwareName"
                name="softwareName"
                value={license.softwareName}
                onChange={handleChange}
              />
            </div>

            {/* Gerente */}
            <div className="mb-3">
              <label htmlFor="manager" className="form-label">
                Gerente
              </label>
              <input
                type="text"
                className="form-control"
                id="manager"
                name="manager"
                value={license.manager}
                onChange={handleChange}
              />
            </div>

            {/* Tipo de Licença */}
            <div className="mb-3">
              <label htmlFor="licenseType" className="form-label">
                Tipo de Licença
              </label>
              <select
                className="form-select"
                id="licenseType"
                name="licenseType"
                value={license.licenseType}
                onChange={handleChange}
              >
                <option value="assinatura">Assinatura</option>
                <option value="perpétua">Perpétua</option>
                <option value="trial">Trial</option>
                <option value="educacional">Educacional</option>
                <option value="corporativa">Corporativa</option>
                <option value="open source">Open Source</option>
                <option value="freemium">Freemium</option>
                <option value="pay per use">Pay per Use</option>
              </select>
            </div>

            {/* Versão */}
            <div className="mb-3">
              <label htmlFor="version" className="form-label">
                Versão
              </label>
              <input
                type="text"
                className="form-control"
                id="version"
                name="version"
                value={license.version}
                onChange={handleChange}
              />
            </div>

            {/* Data de Aquisição */}
            <div className="mb-3">
              <label htmlFor="acquisitionDate" className="form-label">
                Data de Aquisição
              </label>
              <input
                type="date"
                className="form-control"
                id="acquisitionDate"
                name="acquisitionDate"
                value={license.acquisitionDate}
                onChange={handleChange}
              />
            </div>

            {/* Data de Término */}
            <div className="mb-3">
              <label htmlFor="endDate" className="form-label">
                Data de Término
              </label>
              <input
                type="date"
                className="form-control"
                id="endDate"
                name="endDate"
                value={license.endDate}
                onChange={handleChange}
              />
            </div>

            {/* Status */}
            <div className="mb-3">
              <label htmlFor="status" className="form-label">
                Status
              </label>
              <select
                className="form-select"
                id="status"
                name="status"
                value={license.status}
                onChange={handleChange}
              >
                <option value="ativa">Ativa</option>
                <option value="expirada">Expirada</option>
                <option value="pendente">Pendente</option>
                <option value="desativada">Desativada</option>
                <option value="inválida">Inválida</option>
              </select>
            </div>

            {/* Key */}
            <div className="mb-3">
              <label htmlFor="key" className="form-label">
                Key
              </label>
              <input
                type="text"
                className="form-control"
                id="key"
                name="key"
                value={license.key}
                onChange={handleChange}
              />
            </div>

            {/* Limite de Usuários */}
            <div className="mb-3">
              <label htmlFor="userLimit" className="form-label">
                Limite de Usuários
              </label>
              <input
                type="number"
                className="form-control"
                id="userLimit"
                name="userLimit"
                value={license.userLimit}
                onChange={handleChange}
              />
            </div>

            {/* Usuários Ativos */}
            <div className="mb-3">
              <label htmlFor="activeUsers" className="form-label">
                Usuários Ativos
              </label>
              <input
                type="number"
                className="form-control"
                id="activeUsers"
                name="activeUsers"
                value={license.activeUsers}
                onChange={handleChange}
              />
            </div>

            {/* Plano */}
            <div className="mb-3">
              <label htmlFor="plan" className="form-label">
                Plano
              </label>
              <input
                type="text"
                className="form-control"
                id="plan"
                name="plan"
                value={license.plan}
                onChange={handleChange}
              />
            </div>

            {/* Prioridade */}
            <div className="mb-3">
              <label htmlFor="priority" className="form-label">
                Prioridade
              </label>
              <select
                className="form-select"
                id="priority"
                name="priority"
                value={license.priority}
                onChange={handleChange}
              >
                <option value="crítica">Crítica</option>
                <option value="alta">Alta</option>
                <option value="média">Média</option>
                <option value="baixa">Baixa</option>
              </select>
            </div>

            {/* Botões de Ação */}
            <div className="d-flex gap-2">
              <button type="submit" className="btn btn-primary">
                Salvar
              </button>
              <button type="button" className="btn btn-secondary">
                Cancelar
              </button>
            </div>
          </form>

          {/* Tabela de Usuários */}
          <div className="mt-5">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h3 className="pb-2 border-bottom">Usuários Associados</h3>
              <button
                type="button"
                className="btn btn-primary btn-sm"
              >
                Adicionar Usuário
              </button>
            </div>
            <table className="table table-striped table-sm">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nome</th>
                  <th>E-mail</th>
                  <th>Departamento</th>
                </tr>
              </thead>
              <tbody>
                {users.map((user) => (
                  <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{user.name}</td>
                    <td>{user.email}</td>
                    <td>{user.department}</td>
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

export default EditLicense;
