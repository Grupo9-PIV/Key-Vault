import React from 'react';
//Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

const Footer = () => {
  return (
    <footer class="border-top">
      <div className="container d-flex flex-wrap justify-content-between align-items-center">
        <div class="col-md-4 d-flex align-items-center">
          <a href="/" class="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
            <img src="././public/logo.png" alt="logo" width="175" height="auto" class="d-block link-body-emphasis text-decoration-none dropdown-toggle"/>
          </a>
        </div>
        <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
          <li class="ms-3">
            <p class="mb-3 mb-md-0 text-body-secondary">&copy; 2025 Key-Vault. Todos os direitos reservados</p>
          </li>
        </ul>
      </div>
    </footer>
  );
};

export default Footer;
