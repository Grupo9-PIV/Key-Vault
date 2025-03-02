import { useState, useEffect } from 'react';
import './App.css';
import api from './api';
import AppRoutes from './routes';

function App() {
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Rota pública – não precisa enviar o token
        const response = await api.get('/', {
          headers: { requiresAuth: false },
        });
        const title = response.data.message;
        setMessage(response.data.message);
        document.title = title;
        setError('');
      } catch (err) {
        setError('Erro ao carregar mensagem da API');
        console.error('Detalhes do erro:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <AppRoutes />

      <div
        style={{ margin: '20px', padding: '15px', borderTop: '1px solid #ccc' }}
      >
        <h2>Status da API:</h2>
        {loading ? (
          <p>Verificando API...</p>
        ) : error ? (
          <p style={{ color: 'red' }}>{error}</p>
        ) : (
          <p>{message}</p>
        )}
      </div>
    </div>
  );
}

export default App;
