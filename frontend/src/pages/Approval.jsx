import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const Approval = () => {
  // Estado para simular a lista de solicitações
  const [requests, setRequests] = useState([
    {
      id: 1,
      user: { name: 'João Silva', email: 'joao.silva@example.com', department: 'TI' },
      softwareName: 'Visual Studio Code',
      softwareDescription: 'Editor de código-fonte',
      justification: 'Necessário para desenvolvimento de projetos.',
      status: 'pending', // pending, approved, rejected
    },
    {
      id: 2,
      user: { name: 'Maria Souza', email: 'maria.souza@example.com', department: 'Marketing' },
      softwareName: 'Adobe Photoshop',
      softwareDescription: 'Editor de imagens profissional',
      justification: 'Necessário para criação de materiais gráficos.',
      status: 'pending',
    },
  ]);

  // Função para aprovar uma solicitação
  const handleApprove = (id) => {
    setRequests((prevRequests) =>
      prevRequests.map((request) =>
        request.id === id ? { ...request, status: 'approved' } : request
      )
    );
    console.log(`Solicitação ${id} aprovada.`);
  };

  // Função para recusar uma solicitação
  const handleReject = (id) => {
    setRequests((prevRequests) =>
      prevRequests.map((request) =>
        request.id === id ? { ...request, status: 'rejected' } : request
      )
    );
    console.log(`Solicitação ${id} recusada.`);
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Aprovação de Solicitações de Software</h2>
        <div className="py-5">
          {requests.length === 0 ? (
            <p>Nenhuma solicitação pendente.</p>
          ) : (
            <div className="list-group">
              {requests.map((request) => (
                <div key={request.id} className="list-group-item mb-3">
                  <div className="d-flex justify-content-between align-items-center">
                    <div>
                      <h5>{request.softwareName}</h5>
                      <p><strong>Solicitante:</strong> {request.user.name} ({request.user.email})</p>
                      <p><strong>Departamento:</strong> {request.user.department}</p>
                      <p><strong>Descrição:</strong> {request.softwareDescription}</p>
                      <p><strong>Justificativa:</strong> {request.justification}</p>
                      <p>
                        <strong>Status:</strong>{' '}
                        <span
                          className={`badge ${
                            request.status === 'pending'
                              ? 'bg-warning text-dark'
                              : request.status === 'approved'
                              ? 'bg-success'
                              : 'bg-danger'
                          }`}
                        >
                          {request.status === 'pending'
                            ? 'Pendente'
                            : request.status === 'approved'
                            ? 'Aprovado'
                            : 'Recusado'}
                        </span>
                      </p>
                    </div>
                    <div>
                      {request.status === 'pending' && (
                        <>
                          <button
                            className="btn btn-success me-2"
                            onClick={() => handleApprove(request.id)}
                          >
                            Aprovar
                          </button>
                          <button
                            className="btn btn-danger"
                            onClick={() => handleReject(request.id)}
                          >
                            Recusar
                          </button>
                        </>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Approval;