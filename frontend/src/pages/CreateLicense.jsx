import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import api from '../api/index'; // Importa a API configurada
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const CreateLicense = () => {
  const [assignedToId, setAssignedToId] = useState('');
  const [managerId, setManagerId] = useState('');
  const [softwareName, setSoftwareName] = useState('');
  const [licenseType, setLicenseType] = useState('');
  const [status, setStatus] = useState('');
  const [developedBy, setDevelopedBy] = useState('');
  const [version, setVersion] = useState('');
  const [purchaseDate, setPurchaseDate] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [licenseKey, setLicenseKey] = useState('');
  const [currentUsage, setCurrentUsage] = useState(0);
  const [subscriptionPlan, setSubscriptionPlan] = useState('');
  const [conditions, setConditions] = useState('');
  const [priority, setPriority] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validação dos campos obrigatórios
    if (!softwareName || !licenseType || !status || !developedBy || !purchaseDate || !startDate || !endDate) {
      setError('Por favor, preencha todos os campos obrigatórios.');
      return;
    }

    try {
      // Formata as datas para o formato ISO 8601
      const formattedPurchaseDate = new Date(purchaseDate).toISOString();
      const formattedStartDate = new Date(startDate).toISOString();
      const formattedEndDate = new Date(endDate).toISOString();

      // Envia a requisição com o token de autenticação
      const response = await api.post(
        '/licenses/',
        {
          assigned_to_id: assignedToId ? Number(assignedToId) : null,
          manager_id: managerId ? Number(managerId) : null,
          software_name: softwareName,
          license_type: licenseType,
          status: status,
          developed_by: developedBy,
          version: version || null,
          purchase_date: formattedPurchaseDate,
          start_date: formattedStartDate,
          end_date: formattedEndDate,
          license_key: licenseKey || null,
          current_usage: currentUsage ? Number(currentUsage) : 0,
          subscription_plan: subscriptionPlan || null,
          conditions: conditions || null,
          priority: priority || 'média',
        },
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`, // Adiciona o token de autenticação
          },
        }
      );

      alert('Licença criada com sucesso!');
      navigate('/licenses'); // Redireciona para a lista de licenças
    } catch (err) {
      if (err.response && err.response.data && err.response.data.detail) {
        setError(err.response.data.detail);
      } else {
        setError('Erro ao criar licença. Tente novamente.');
      }

      // Se o erro for de autenticação, redireciona para a tela de login
      if (err.response && err.response.status === 401) {
        navigate('/login');
      }
    }
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container px-4 py-5">
        <h2 className="pb-2 border-bottom">Criar Nova Licença</h2>
        <div className="row g-5 py-5">
          <div className="col">
            <form onSubmit={handleSubmit}>
              {error && <div className="alert alert-danger">{error}</div>}

              {/* Campos obrigatórios */}
              <div className="mb-3">
                <label htmlFor="softwareName" className="form-label">
                  Nome do Software <span className="text-danger">*</span>
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="softwareName"
                  value={softwareName}
                  onChange={(e) => setSoftwareName(e.target.value)}
                  placeholder="Digite o nome do software"
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="licenseType" className="form-label">
                  Tipo de Licença <span className="text-danger">*</span>
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="licenseType"
                  value={licenseType}
                  onChange={(e) => setLicenseType(e.target.value)}
                  placeholder="Digite o tipo de licença"
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="status" className="form-label">
                  Status <span className="text-danger">*</span>
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="status"
                  value={status}
                  onChange={(e) => setStatus(e.target.value)}
                  placeholder="Digite o status da licença"
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="developedBy" className="form-label">
                  Desenvolvido Por <span className="text-danger">*</span>
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="developedBy"
                  value={developedBy}
                  onChange={(e) => setDevelopedBy(e.target.value)}
                  placeholder="Digite quem desenvolveu o software"
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="purchaseDate" className="form-label">
                  Data de Compra <span className="text-danger">*</span>
                </label>
                <input
                  type="datetime-local"
                  className="form-control"
                  id="purchaseDate"
                  value={purchaseDate}
                  onChange={(e) => setPurchaseDate(e.target.value)}
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="startDate" className="form-label">
                  Data de Início <span className="text-danger">*</span>
                </label>
                <input
                  type="datetime-local"
                  className="form-control"
                  id="startDate"
                  value={startDate}
                  onChange={(e) => setStartDate(e.target.value)}
                  required
                />
              </div>
              <div className="mb-3">
                <label htmlFor="endDate" className="form-label">
                  Data de Término <span className="text-danger">*</span>
                </label>
                <input
                  type="datetime-local"
                  className="form-control"
                  id="endDate"
                  value={endDate}
                  onChange={(e) => setEndDate(e.target.value)}
                  required
                />
              </div>

              {/* Campos opcionais */}
              <div className="mb-3">
                <label htmlFor="assignedToId" className="form-label">
                  ID do Usuário Atribuído
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="assignedToId"
                  value={assignedToId}
                  onChange={(e) => setAssignedToId(e.target.value)}
                  placeholder="Digite o ID do usuário atribuído"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="managerId" className="form-label">
                  ID do Gerente
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="managerId"
                  value={managerId}
                  onChange={(e) => setManagerId(e.target.value)}
                  placeholder="Digite o ID do gerente"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="version" className="form-label">
                  Versão
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="version"
                  value={version}
                  onChange={(e) => setVersion(e.target.value)}
                  placeholder="Digite a versão do software"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="licenseKey" className="form-label">
                  Chave da Licença
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="licenseKey"
                  value={licenseKey}
                  onChange={(e) => setLicenseKey(e.target.value)}
                  placeholder="Digite a chave da licença"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="currentUsage" className="form-label">
                  Uso Atual
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="currentUsage"
                  value={currentUsage}
                  onChange={(e) => setCurrentUsage(e.target.value)}
                  placeholder="Digite o uso atual da licença"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="subscriptionPlan" className="form-label">
                  Plano de Assinatura
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="subscriptionPlan"
                  value={subscriptionPlan}
                  onChange={(e) => setSubscriptionPlan(e.target.value)}
                  placeholder="Digite o plano de assinatura"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="conditions" className="form-label">
                  Condições
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="conditions"
                  value={conditions}
                  onChange={(e) => setConditions(e.target.value)}
                  placeholder="Digite as condições da licença"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="priority" className="form-label">
                  Prioridade
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="priority"
                  value={priority}
                  onChange={(e) => setPriority(e.target.value)}
                  placeholder="Digite a prioridade da licença"
                />
              </div>

              <div className="d-flex gap-2">
                <button type="submit" className="btn btn-primary">
                  Criar Licença
                </button>
                <Link to="/licenses" className="btn btn-secondary">
                  Cancelar
                </Link>
              </div>
            </form>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}; //commit

export default CreateLicense;