import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api/index'; // Importe a API configurada
import Header from '../components/Header';
import Footer from '../components/Footer';

const UsersDetail = () => {
  const { userId } = useParams(); // Pega o ID do usuário da URL
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log('Token:', localStorage.getItem('token')); // Log do token

    // Busca os detalhes do usuário
    api.get(`/users/${userId}`, { 
      headers: {
        requiresAuth: true, // Adiciona o token de autenticação
      },
    })
      .then((response) => {
        console.log('Dados recebidos:', response.data); // Log da resposta
        setUser(response.data); 
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
    <div className="page-container">
      <Header />
      <div className="container">
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
          <strong>Ativo:</strong> {user.is_active ? 'Sim' : 'Não'}
        </p>
      </div>
      <Footer />
    </div>
  );
}; // commit

export default UsersDetail;