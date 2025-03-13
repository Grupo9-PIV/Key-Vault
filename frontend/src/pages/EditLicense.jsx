import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../api/index';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const EditLicense = () => {
  const { licenseId } = useParams(); // Captura o licenseId da URL
  const navigate = useNavigate();
  const [license, setLicense] = useState({
    software_name: '',
    license_type: '',
    status: '',
    developed_by: '',
    version: '',
    purchase_date: '',
    start_date: '',
    end_date: '',
    license_key: '',
    current_usage: 0,
    subscription_plan: '',
    conditions: '',
    priority: '',
    assigned_to_id: 0,
    manager_id: 0,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!licenseId) {
      console.error('ID da licença não encontrado na URL.');
      setError('ID da licença não encontrado.');
      setLoading(false);
      return;
    }

    const fetchLicense = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await api.get(`/licenses/${licenseId}`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        setLicense(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Erro ao buscar licença:', error);
        if (error.response?.status === 401) {
          alert('Sessão expirada, faça login novamente.');
          localStorage.removeItem('token');
          navigate('/login');
        }
        setError('Erro ao carregar os dados da licença.');
        setLoading(false);
      }
    };

    fetchLicense();
  }, [licenseId, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const updatedLicense = { ...license };

      await api.patch(`/licenses/${licenseId}`, updatedLicense, {
        headers: { Authorization: `Bearer ${token}` },
      });
      alert('Licença atualizada com sucesso!');
      navigate('/licenses');
    } catch (error) {
      console.error('Erro ao atualizar licença:', error);
      if (error.response?.status === 401) {
        alert('Sessão expirada, faça login novamente.');
        localStorage.removeItem('token');
        navigate('/login');
      }
      setError('Erro ao atualizar licença.');
    }
  };

  const handleChange = (e) => {
    const { id, value } = e.target;
    setLicense((prevLicense) => ({
      ...prevLicense,
      [id]: value,
    }));
  };

  if (loading) return <p>Carregando...</p>;

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Editar Licença</h2>
        {error && <div className="alert alert-danger">{error}</div>}
        <div className="py-5">
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="software_name" className="form-label">Nome do Software</label>
              <input
                type="text"
                className="form-control"
                id="software_name"
                value={license.software_name}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="license_type" className="form-label">Tipo de Licença</label>
              <input
                type="text"
                className="form-control"
                id="license_type"
                value={license.license_type}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="status" className="form-label">Status</label>
              <input
                type="text"
                className="form-control"
                id="status"
                value={license.status}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="developed_by" className="form-label">Desenvolvido por</label>
              <input
                type="text"
                className="form-control"
                id="developed_by"
                value={license.developed_by}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="version" className="form-label">Versão</label>
              <input
                type="text"
                className="form-control"
                id="version"
                value={license.version}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="purchase_date" className="form-label">Data de Compra</label>
              <input
                type="date"
                className="form-control"
                id="purchase_date"
                value={license.purchase_date}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="start_date" className="form-label">Data de Início</label>
              <input
                type="date"
                className="form-control"
                id="start_date"
                value={license.start_date}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="end_date" className="form-label">Data de Término</label>
              <input
                type="date"
                className="form-control"
                id="end_date"
                value={license.end_date}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="license_key" className="form-label">Chave de Licença</label>
              <input
                type="text"
                className="form-control"
                id="license_key"
                value={license.license_key}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="current_usage" className="form-label">Uso Atual</label>
              <input
                type="number"
                className="form-control"
                id="current_usage"
                value={license.current_usage}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="subscription_plan" className="form-label">Plano de Assinatura</label>
              <input
                type="text"
                className="form-control"
                id="subscription_plan"
                value={license.subscription_plan}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="conditions" className="form-label">Condições</label>
              <input
                type="text"
                className="form-control"
                id="conditions"
                value={license.conditions}
                onChange={handleChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="priority" className="form-label">Prioridade</label>
              <input
                type="text"
                className="form-control"
                id="priority"
                value={license.priority}
                onChange={handleChange}
              />
            </div>
            <div className="d-flex gap-2">
              <button type="submit" className="btn btn-primary">Salvar</button>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => navigate('/licenses')}
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

export default EditLicense;
