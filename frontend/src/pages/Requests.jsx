import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const Requests = () => {
  // Estado para o ID do usuário
  const [userId, setUserId] = useState('');

  // Estado para os dados do usuário
  const [user, setUser] = useState({
    id: '',
    name: '',
    email: '',
    department: '',
  });

  // Estado para o software solicitado
  const [software, setSoftware] = useState('');

  // Estado para a justificativa da solicitação
  const [justification, setJustification] = useState('');

  // Função para buscar os dados do usuário ao inserir o ID
  const handleUserIdChange = (e) => {
    const id = e.target.value;
    setUserId(id);

    // Simulação de busca de dados do usuário a partir do ID
    if (id === '1') {
      setUser({
        id: id,
        name: 'Ewellyn Almeida',
        email: 'lynn@gmail.com',
        department: 'TI',
      });
    } else if (id === '2') {
      setUser({
        id: id,
        name: 'João Silva',
        email: 'joao@gmail.com',
        department: 'RH',
      });
    } else {
      // Limpa os campos se o ID não for reconhecido
      setUser({
        id: '',
        name: '',
        email: '',
        department: '',
      });
    }
  };

  // Função para enviar a solicitação de acesso ao software
  const handleSubmitRequest = (e) => {
    e.preventDefault();
    console.log('Solicitação enviada:', {
      user,
      software,
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
        <h2 className="pb-2 border-bottom">Solicitar Acesso a Software</h2>
        <div className="py-5">
          <form onSubmit={handleSubmitRequest}>
            <div className="mb-3">
              <label htmlFor="userId" className="form-label">
                ID do Usuário
              </label>
              <input
                type="text"
                className="form-control"
                id="userId"
                name="userId"
                value={userId}
                onChange={handleUserIdChange}
                disabled
              />
            </div>
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
                value={user.department}
                disabled
              />
            </div>
            <div className="mb-3">
              <label htmlFor="software" className="form-label">
                Software Solicitado
              </label>
              <input
                type="text"
                className="form-control"
                id="software"
                name="software"
                value={software}
                onChange={(e) => setSoftware(e.target.value)}
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

export default Requests;