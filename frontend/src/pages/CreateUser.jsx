import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const CreateUser = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [role, setRole] = useState('');
  const [department, setDepartment] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validação simples dos campos
    if (!name || !email || !password) {
      setError('Por favor, preencha todos os campos.');
      return;
    }

    // Simulação de envio de dados para o backend
    try {
      // Aqui você faria uma requisição HTTP para o backend
      // Exemplo com fetch:
      // const response = await fetch('/api/users', {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json' },
      //   body: JSON.stringify({ name, email, password }),
      // });
      // const data = await response.json();

      // Simulação de sucesso
      console.log('Usuário criado com sucesso:', { name, email, password });
      setError('');
      alert('Usuário criado com sucesso!');
      navigate('/users'); // Redireciona para a lista de usuários
    } catch (err) {
      setError('Erro ao criar usuário. Tente novamente.');
      console.error(err);
    }
  };

  return (
    <div className="page-container">
      <Header />
      <div className="container px-4 py-5">
        <h2 className="pb-2 border-bottom">Criar Novo Usuário</h2>
        <div className="row g-5 py-5">
          <div className="col">
            <form onSubmit={handleSubmit}>
              {error && <div className="alert alert-danger">{error}</div>}
              <div className="mb-3">
                <label htmlFor="name" className="form-label">
                  Nome
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Digite o nome do usuário"
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
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Digite o e-mail do usuário"
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
                  value={role}
                  onChange={(e) => setRole(e.target.value)}
                  placeholder="Digite a função do usuário"
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
                  value={department}
                  onChange={(e) => setDepartment(e.target.value)}
                  placeholder="Digite o departamento do usuário"
                />
              </div>
              <div className="d-flex gap-2">
                <button type="submit" className="btn btn-primary">
                  Criar Usuário
                </button>
                <Link to="/users" className="btn btn-secondary">
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
};

export default CreateUser;