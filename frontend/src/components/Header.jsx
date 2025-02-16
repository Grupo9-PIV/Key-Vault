import React from 'react';
import { Link } from 'react-router-dom'; 

// Definindo o Header como um componente funcional
const Header = () => {
  return (
    <header style={headerStyle}>
      <div style={logoStyle}>
        <h1>Logo da Empresa</h1>
      </div>
      <nav style={navStyle}>
        <ul style={navListStyle}>
          <li>
            <Link style={linkStyle} to="/initial">Home</Link>
          </li>
          <li>
            <Link style={linkStyle} to="/users">Usuários</Link>
          </li>
          <li>
            <Link style={linkStyle} to="/licenses">Licenças</Link>
          </li>
          <li>
            <Link style={linkStyle} to="/renewals">Renovações</Link>
          </li>
          <li>
            <Link style={linkStyle} to="/notifications">Notificações</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

// Estilos simples para o Header (você pode personalizar)
const headerStyle = {
  backgroundColor: '#2c3e50',
  color: '#fff',
  padding: '10px 0',
  textAlign: 'center',
};

const logoStyle = {
  fontSize: '24px',
  fontWeight: 'bold',
};

const navStyle = {
  marginTop: '10px',
};

const navListStyle = {
  listStyleType: 'none',
  padding: 0,
};

const linkStyle = {
  color: '#fff',
  textDecoration: 'none',
  margin: '0 15px',
};

export default Header;
