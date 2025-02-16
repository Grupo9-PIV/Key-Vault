
import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

import Header from "../components/Header";
import Footer from "../components/Footer";

const Initial = () => {

  useEffect(() => {
    document.title = "Home"; 
  }, []);

  return (
    <div>
      <Header />
      <h1>Sistema de Gerenciamento de Licenças</h1>
      <ul>
        <li><Link to="/users">Usuários</Link></li>
        <li><Link to="/licenses">Licenças</Link></li>
        <li><Link to="/notifications">Notificações</Link></li>
        <li><Link to="/renewals">Renovações</Link></li>
        {/* <li><Link to="/crud">Administração Geral (CRUD) - Ajustar caminho depois</Link></li> */}
      </ul>
      <Footer />
    </div>
  );
};

export default Initial;






