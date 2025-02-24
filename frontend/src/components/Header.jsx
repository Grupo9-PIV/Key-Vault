import React from 'react';
import { Link } from 'react-router-dom'; 
//Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';


// Definindo o Header como um componente funcional
const Header = () => {
  return (
    <header class="p-3 mb-3 border-bottom">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          
          <Link class="nav-link px-2 link-body-emphasis" to="#">
            <img src="././public/logo.png" alt="Logo" width="130" height="auto" class="d-block link-body-emphasis text-decoration-none dropdown-toggle" />
          </Link>
          <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li><Link class=" nav-link px-2 link-body-emphasis" to="/initial">Home</Link></li>
            <li><Link class="nav-link px-2 link-body-emphasis" to="/users">Usuários</Link></li>
            <li><Link class="nav-link px-2 link-body-emphasis" to="/licenses">Licenças</Link></li>
            <li><Link class="nav-link px-2 link-body-emphasis" to="/renewals">Renovações</Link></li>
          </ul>
          <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li class="me-3">
              <Link class="nav-link px-2 link-body-emphasis position-relative" to="/notifications">
                <img src="././public/sino.png" alt="Sino" width="25" height="25" class="d-block link-body-emphasis text-decoration-none dropdown-toggle" />
                <span class="position-absolute top-0

               start-100 translate-middle badge rounded-pill bg-danger">3
                  <span class="visually-hidden">Notificações não lidas</span>
                </span>
              </Link>
            </li>
            <li>
              <div class="dropdown text-end">
                <a href="#" class="d-block link-body-emphasis text-decoration-none dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                  <img src="https://github.com/mdo.png" alt="mdo" width="32" height="32" class="rounded-circle"/>
                </a>
                <ul class="dropdown-menu text-small">
                  <li><a class="dropdown-item" href="#">Minha conta</a></li>
                  <li><hr class="dropdown-divider"/></li>
                  <li><a class="dropdown-item" href="#">Sair</a></li>
                </ul>
              </div>
            </li>
          </ul>

        </div>
      </div>
    </header>
    //<header style={headerStyle}>
    //  <div style={logoStyle}>
    //    <h1>Logo da Empresa</h1>
    //  </div>
    //  <nav style={navStyle}>
    //    <ul style={navListStyle}>
    //      <li>
    //        <Link style={linkStyle} to="/initial">Home</Link>
    //      </li>
    //      <li>
    //        <Link style={linkStyle} to="/users">Usuários</Link>
    //      </li>
    //      <li>
    //        <Link style={linkStyle} to="/licenses">Licenças</Link>
    //      </li>
    //      <li>
    //        <Link style={linkStyle} to="/renewals">Renovações</Link>
    //      </li>
    //      <li>
    //        <Link style={linkStyle} to="/notifications">Notificações</Link>
    //      </li>
    //    </ul>
    //  </nav>
    //</header>
  );
};

export default Header;
