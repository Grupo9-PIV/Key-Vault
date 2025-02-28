import React, { useEffect, useState } from 'react';

import Header from '../components/Header';
import Footer from '../components/Footer';

const UsersDetail = () => {
  useEffect(() => {
    document.title = 'Detalhes dos Usuários';
  }, []);

  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Pegando o ID da URL
  const userId = window.location.pathname.split('/').pop();

  useEffect(() => {
    if (!userId) return;

    fetch(`http://localhost:8000/users/${userId}`)
      .then((response) => response.json())
      .then((data) => {
        setUser(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Erro ao buscar usuário:', error);
        setLoading(false);
      });
  }, [userId]);

  if (loading) return <p>Carregando...</p>;
  if (!user) return <p>Usuário não encontrado.</p>;

  return (
    <div>
      <Header />
      <h2>Detalhes do Usuário</h2>
      <p>
        <strong>ID:</strong> {user.id}
      </p>
      <p>
        <strong>Nome:</strong> {user.name}
      </p>
      <p>
        <strong>Email:</strong> {user.email}
      </p>
      <p>
        <strong>Função:</strong> {user.role}
      </p>
      <p>
        <strong>Departamento:</strong> {user.department || 'Não informado'}
      </p>
      <p>
        <strong>Conta criada em:</strong>{' '}
        {new Date(user.created_at).toLocaleDateString()}
      </p>

      {/* Link para a página CRUD (substituir # pelo caminho correto depois) */}
      <p>
        <a href="#">Gerenciar Usuário (CRUD)</a>
      </p>
      <Footer />
    </div>
  );
};

export default UsersDetail;
