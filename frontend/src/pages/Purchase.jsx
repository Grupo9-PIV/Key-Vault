import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const Purchase = ({ loggedInUser }) => {
  // Estado para o nome do software
  const [softwareName, setSoftwareName] = useState('');

  // Estado para a descrição do software
  const [softwareDescription, setSoftwareDescription] = useState('');

  // Estado para a justificativa da solicitação
  const [justification, setJustification] = useState('');

  // Verifique se o loggedInUser está sendo passado corretamente
  useEffect(() => {
    console.log('loggedInUser:', loggedInUser);
  }, [loggedInUser]);

  // Função para enviar a solicitação de compra/assinatura do software
  const handleSubmitRequest = (e) => {
    e.preventDefault();
    console.log('Solicitação de compra/assinatura enviada:', {
      user: loggedInUser, // Usuário logado
      softwareName,
      softwareDescription,
      justification,
    });
    // Aqui você pode adicionar a lógica para enviar a solicitação ao backend
  };

  // Função para cancelar a solicitação
  const handleCancel = () => {
    console.log('Solicitação cancelada');
    // Aqui você pode adicionar a lógica para redirecionar ou limpar o formulário
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <h2 className="pb-2 border-bottom">Solicitar Compra/Assinatura de Software</h2>
        <div className="py-5">
          <form onSubmit={handleSubmitRequest}>
            <div className="mb-3">
              <label htmlFor="name" className="form-label">
                Nome
              </label>
              <input
                type="text"
                className="form-control"
                id="name"
                name="name"
                value={loggedInUser ? loggedInUser.name : ''}
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
                value={loggedInUser ? loggedInUser.email : ''}
                disabled
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
                value={loggedInUser ? loggedInUser.department : ''}
                disabled
              />
            </div>
            <div className="mb-3">
              <label htmlFor="softwareName" className="form-label">
                Nome do Software
              </label>
              <input
                type="text"
                className="form-control"
                id="softwareName"
                name="softwareName"
                value={softwareName}
                onChange={(e) => setSoftwareName(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="softwareDescription" className="form-label">
                Descrição do Software
              </label>
              <textarea
                className="form-control"
                id="softwareDescription"
                name="softwareDescription"
                value={softwareDescription}
                onChange={(e) => setSoftwareDescription(e.target.value)}
                rows="4"
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="justification" className="form-label">
                Justificativa
              </label>
              <textarea
                className="form-control"
                id="justification"
                name="justification"
                value={justification}
                onChange={(e) => setJustification(e.target.value)}
                rows="4"
                required
              />
            </div>
            <div className="d-flex gap-2">
              <button type="submit" className="btn btn-primary">
                Enviar Solicitação
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={handleCancel}
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

export default Purchase;