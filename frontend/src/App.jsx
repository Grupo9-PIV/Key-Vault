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
        const response = await api.get('/');
        setMessage(response.data.message);
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
      {/* Sistema de rotas */}
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
