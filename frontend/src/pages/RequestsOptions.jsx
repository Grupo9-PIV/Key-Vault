import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { useNavigate } from 'react-router-dom'; // Para redirecionamento
import '../styles/style.css';

const RequestsOptions = () => {
  const navigate = useNavigate();
 
  // Funções para redirecionar para as telas correspondentes
  const goToSoftwareRequest = () => {
    navigate('/purchase');
  };

  const goToAccessRequest = () => {
    navigate('/requests'); // Redireciona para a página Requests.jsx
  };

  const goToApprovals = () => {
    navigate('/approval');
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Opções de Solicitações</h2>
        <div className="py-5">
          <div className="d-grid gap-3">
            <button
              className="btn btn-primary btn-lg"
              onClick={goToSoftwareRequest}
            >
              Solicitação de Software
            </button>
            <button
              className="btn btn-primary btn-lg"
              onClick={goToAccessRequest} // Adicionado o onClick aqui
            >
              Solicitação de Acesso
            </button>
            <button
              className="btn btn-primary btn-lg"
              onClick={goToApprovals}
            >
              Aprovações Pendentes
            </button>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default RequestsOptions;