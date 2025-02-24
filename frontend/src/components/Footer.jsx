import React from 'react';
//Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

const Footer = () => {
  return (
    <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <div class="col-md-4 d-flex align-items-center">
      <a href="/" class="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
        <img src="././public/logo.png" alt="logo" width="175" height="auto" class="d-block link-body-emphasis text-decoration-none dropdown-toggle"/>
      </a>
    </div>

    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
      <li class="ms-3"><p class="mb-3 mb-md-0 text-body-secondary">&copy; 2025 Key-Vault. Todos os direitos reservados</p></li>
    </ul>
  </footer>
    //<footer style={footerStyle}>
    //  <p>&copy; 2025 Key-Vault. Todos os direitos reservados.</p>
    //  <p>
    //    <a href="/privacy-policy" style={footerLinkStyle}>Política de Privacidade</a> | 
    //    <a href="/terms" style={footerLinkStyle}>Termos de Uso</a>
    //  </p>
    //</footer>
  );
};

export default Footer;
