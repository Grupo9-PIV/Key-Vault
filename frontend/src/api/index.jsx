import axios from 'axios';
import { setupInterceptors } from './interceptors';
import { clearToken } from './tokenService';

const baseURL = import.meta.env.VITE_API_BASE_URL;

const api = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Função para efetuar logout – limpa o token e redireciona o usuário para a tela de login
const logoutUser = () => {
  clearToken();
  window.location.href = '/login';
};

// Configura os interceptors passando a função de logout
setupInterceptors(api, logoutUser);

export default api;
