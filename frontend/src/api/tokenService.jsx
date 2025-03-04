import * as jwtDecodeImport from 'jwt-decode';

// Caso o pacote exporte a função no default, usa-a; caso contrário, usa o objeto importado
const jwtDecode = jwtDecodeImport.default || jwtDecodeImport;

export const getToken = () => localStorage.getItem('token');

export const setToken = (token) => localStorage.setItem('token', token);

export const clearToken = () => localStorage.removeItem('token');

/**
Verifica se o token está próximo de expirar (menos de 5 minutos)
**/
export const isTokenExpiring = (token) => {
  try {
    const decoded = jwtDecode(token);
    if (!decoded.exp) return false;
    const currentTime = Date.now() / 1000;
    const buffer = 300; // 5 minutos
    return decoded.exp - currentTime < buffer;
  } catch (error) {
    return false;
  }
};
