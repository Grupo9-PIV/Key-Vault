import {
  getToken,
  setToken,
  isTokenExpiring,
} from './tokenService';

let isRefreshing = false;
let failedQueue = [];

// Processa a fila de requisições pendentes após o refresh do token
const processQueue = (error, token = null) => {
  failedQueue.forEach((prom) => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });
  failedQueue = [];
};

export const setupInterceptors = (axiosInstance, logoutCallback) => {
  // Interceptor de requisição
  axiosInstance.interceptors.request.use(
    async (config) => {
      const requiresAuth = config.headers.requiresAuth || false;

      delete config.headers.requiresAuth;

      if (!requiresAuth) {
        return config;
      }

      let token = getToken();
      if (token) {
        // Se o token está próximo de expirar, tenta renová-lo
        if (isTokenExpiring(token)) {
          if (!isRefreshing) {
            isRefreshing = true;
            try {
              const response = await axiosInstance.post(
                '/refresh_token',
                {},
                { headers: { Authorization: `Bearer ${token}` } }
              );
              const newToken = response.data.token;
              setToken(newToken);
              token = newToken;
              processQueue(null, newToken);
            } catch (error) {
              processQueue(error, null);
              logoutCallback();
              return Promise.reject(error);
            } finally {
              isRefreshing = false;
            }
          } else {
            // Se já estiver em processo de refresh, coloca esta requisição na fila e aguarda
            return new Promise((resolve, reject) => {
              failedQueue.push({
                resolve: (newToken) => {
                  config.headers.Authorization = `Bearer ${newToken}`;
                  resolve(config);
                },
                reject: (err) => {
                  reject(err);
                },
              });
            });
          }
        }
        // Define o header de autorização com o token (novo ou existente)
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    },
    (error) => Promise.reject(error)
  );

  // Interceptor de resposta
  axiosInstance.interceptors.response.use(
    (response) => response,
    (error) => {
      // Se a resposta for 401 (não autorizado), efetua o logout
      if (error.response && error.response.status === 401) {
        logoutCallback();
      }
      return Promise.reject(error);
    }
  );
};
