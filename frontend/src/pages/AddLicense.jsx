import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const CreateLicense = () => {
  // Estado para armazenar os dados da nova licença
  const [license, setLicense] = useState({
    softwareName: '',
    manager: '',
    licenseType: 'assinatura', // Valor padrão
    version: '',
    acquisitionDate: '',
    endDate: '',
    status: 'ativa', // Valor padrão
    key: '',
    userLimit: 0,
    activeUsers: 0,
    plan: '',
    priority: 'média', // Valor padrão
  });

  // Função para atualizar os dados da licença
  const handleChange = (e) => {
    const { name, value } = e.target;
    setLicense((prevLicense) => ({
      ...prevLicense,
      [name]: value,
    }));
  };

  // Função para salvar a nova licença
  const handleSave = (e) => {
    e.preventDefault();
    console.log('Nova licença criada:', license);
    // Aqui você pode adicionar a lógica para enviar os dados ao backend
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Criar Nova Licença</h2>
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
                required
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
                required
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
                required
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
                required
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
                required
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
                required
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
                required
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
                required
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
                required
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
                required
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
                required
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
                required
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
                Criar Licença
              </button>
              <button type="button" className="btn btn-secondary">
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

export default CreateLicense;