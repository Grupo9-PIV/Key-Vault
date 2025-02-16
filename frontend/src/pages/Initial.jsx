
import React from "react";
import { Link } from "react-router-dom";

const Initial = () => {
  return (
    <div>
      <h1>Sistema de Gerenciamento de Licenças</h1>
      <ul>
        <li><Link to="/users">Gerenciar Usuários</Link></li>
        <li><Link to="/licenses">Gerenciar Licenças</Link></li>
        <li><Link to="/notifications">Notificações</Link></li>
        <li><Link to="/renewals">Solicitações de Renovação</Link></li>
        {/* <li><Link to="/crud">Administração Geral (CRUD) - Ajustar caminho depois</Link></li> */}
      </ul>
    </div>
  );
};

export default Initial;






