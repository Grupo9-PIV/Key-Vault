import React from 'react';

const Footer = () => {
  return (
    <footer style={footerStyle}>
      <p>&copy; 2025 Key-Vault. Todos os direitos reservados.</p>
      <p>
        <a href="/privacy-policy" style={footerLinkStyle}>Política de Privacidade</a> | 
        <a href="/terms" style={footerLinkStyle}>Termos de Uso</a>
      </p>
    </footer>
  );
};

// Estilos para o Footer
const footerStyle = {
  backgroundColor: '#34495e',
  color: '#fff',
  padding: '10px 0',
  textAlign: 'center',
};

const footerLinkStyle = {
  color: '#fff',
  textDecoration: 'none',
  margin: '0 5px',
};

export default Footer;
