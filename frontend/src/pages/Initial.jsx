
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document</title>
</head>
<body>
  
</body>
</html>
import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

import Header from "../components/Header";
import Footer from "../components/Footer";
import '../styles/style.css'

const Initial = () => {

  useEffect(() => {
    document.title = "Home"; 
  }, []);

  return (
    <div class="page-container">
      <Header />
      <div class="container px-4 py-5">
        <h2 class="pb-2 border-bottom">Sistema de Gerenciamento de Licenças</h2>
        <div class="row align-items-md-center g-5 py-5">
          <div class="col">
            <div class="row row-cols-1 row-cols-sm-2 g-4">
              <Link to="/users">
                <div class="align-items-center col d-flex flex-column gap-2">
                  <div class="dashboard-item feature-icon-small d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-4 rounded-3">
                    <img class="p-5" src="././public/usuarios.png" alt="Usuários" />
                  </div>
                  <h4 class="fw-semibold mb-0 text-body-emphasis">Usuários</h4>
                </div>
              </Link>
              <Link to="/licenses">
                <div class="align-items-center col d-flex flex-column gap-2">
                  <div class="dashboard-item feature-icon-small d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-4 rounded-3">
                    <img class="p-5"  src="././public/licencas.png" alt="Licenças" />
                  </div>
                  <h4 class="fw-semibold mb-0 text-body-emphasis">Licenças</h4>
                </div>
              </Link>
              <Link to="/notifications">
                <div class="align-items-center col d-flex flex-column gap-2">
                  <div class="dashboard-item feature-icon-small d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-4 rounded-3">
                  <img class="p-5"  src="././public/notificacoes.png" alt="Notificações" />
                  </div>
                  <h4 class="fw-semibold mb-0 text-body-emphasis">Notificações</h4>
                </div>
              </Link>
              <Link to="/renewals">
                <div class="align-items-center col d-flex flex-column gap-2">
                  <div class="dashboard-item feature-icon-small d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-4 rounded-3">
                  <img class="p-5"  src="././public/renovacoes.png" alt="Renovações" />
                  </div>
                  <h4 class="fw-semibold mb-0 text-body-emphasis">Renovações</h4>
                </div>
              </Link>
              {/* <Link to="/crud">Administração Geral (CRUD) - Ajustar caminho depois</Link> */}
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Initial;






