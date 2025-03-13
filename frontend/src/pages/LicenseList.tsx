import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../api/index';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

interface License {
  id: number;
  software_name: string;
  license_type: string;
  status: string;
  developed_by: string;
  version: string;
  purchase_date: string;
  start_date: string;
  end_date: string;
  license_key: string;
  current_usage: number;
  subscription_plan: string;
  conditions: string;
  priority: string;
  assigned_to_id: number;
  manager_id: number;
  created_at: string;
  updated_at: string;
}

const LicenseList = () => {
  const [licenses, setLicenses] = useState<License[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchId, setSearchId] = useState('');
  const [error, setError] = useState('');

  const fetchLicenses = () => {
    setLoading(true);
    setError('');

    let url = '/licenses/?skip=0&limit=10';

    if (searchId) {
      url = `/licenses/${searchId}`;
    }

    api
      .get(url, {
        headers: {
          requiresAuth: true, // Adiciona o token de autenticação
        },
      })
      .then((response) => {
        if (searchId) {
          // Se estiver buscando por ID, transforma o objeto em um array
          setLicenses([response.data]);
        } else {
          setLicenses(response.data);
        }
        setError('');
      })
      .catch(() => {
        if (searchId) {
          setError('ID de licença não encontrado.');
          setLicenses([]);
        } else {
          setError('Erro ao carregar licenças.');
        }
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchLicenses();
  }, []);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    fetchLicenses();
  };

  const handleDelete = async (licenseId: number) => {
    const confirmDelete = window.confirm('Tem certeza que deseja excluir esta licença?');

    if (confirmDelete) {
      try {
        await api.delete(`/licenses/${licenseId}`, {
          headers: {
            requiresAuth: true,
          },
        });

        setLicenses(licenses.filter((license) => license.id !== licenseId));
        alert('Licença excluída com sucesso!');
      } catch (error) {
        console.error('Erro ao excluir licença:', error);
        alert('Erro ao excluir licença.');
      }
    }
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <header className="d-flex justify-content-between py-3 align-items-center">
          <div>
            {/* Botão "Criar Licença" ajustado */}
            <Link to="/licenses/create" className="btn btn-dark me-2">
              Criar Licença
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
              <button type="submit" className="btn btn-primary mt-2">
                Buscar
              </button>
            </form>
          </div>
        </header>

        <h2>Lista de Licenças</h2>

        {loading ? (
          <p>Carregando...</p>
        ) : error ? (
          <p style={{ color: 'red' }}>{error}</p>
        ) : (
          <div className="table-responsive small">
            <table className="table table-striped table-sm dropdown">
              <thead>
                <tr>
                  <th>Id</th>
                  <th>Software</th>
                  <th>Tipo</th>
                  <th>Status</th>
                  <th>Desenvolvido por</th>
                  <th>Versão</th>
                  <th>Data de Compra</th>
                  <th>Data de Início</th>
                  <th>Data de Término</th>
                  <th>Chave</th>
                  <th>Uso Atual</th>
                  <th>Plano</th>
                  <th>Condições</th>
                  <th>Prioridade</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {licenses.map((license) => (
                  <tr key={license.id}>
                    <td>{license.id}</td>
                    <td>{license.software_name}</td>
                    <td>{license.license_type}</td>
                    <td>{license.status}</td>
                    <td>{license.developed_by}</td>
                    <td>{license.version}</td>
                    <td>{new Date(license.purchase_date).toLocaleDateString()}</td>
                    <td>{new Date(license.start_date).toLocaleDateString()}</td>
                    <td>{new Date(license.end_date).toLocaleDateString()}</td>
                    <td>{license.license_key}</td>
                    <td>{license.current_usage}</td>
                    <td>{license.subscription_plan}</td>
                    <td>{license.conditions}</td>
                    <td>{license.priority}</td>
                    <td>
                      <Link className="btn btn-sm btn-warning me-2" to={`/licenses/edit/${license.id}`}>
                        Editar
                      </Link>
                      <button className="btn btn-sm btn-danger" onClick={() => handleDelete(license.id)}>
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
}; //commit

export default LicenseList;