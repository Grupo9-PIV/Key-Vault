import React from 'react';
import { Link } from 'react-router-dom';
//Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

// Definindo o Header como um componente funcional
const Header = () => {
  return (
    <header className="p-3 mb-3 border-bottom">
      <div className="container">
        <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <Link className="nav-link px-2 link-body-emphasis" to="#">
            <img
              src="././public/assets/logo.png"
              alt="Logo"
              width="130"
              height="auto"
              className="d-block link-body-emphasis text-decoration-none dropdown-toggle"
            />
          </Link>
          <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li>
              <Link className=" nav-link px-2 link-body-emphasis" to="/initial">
                Home
              </Link>
            </li>
            <li>
              <Link className="nav-link px-2 link-body-emphasis" to="/users">
                Usuários
              </Link>
            </li>
            <li>
              <Link className="nav-link px-2 link-body-emphasis" to="/licenses">
                Licenças
              </Link>
            </li>
            <li>
              <Link className="nav-link px-2 link-body-emphasis" to="/renewals">
                Renovações
              </Link>
            </li>
          </ul>
          <ul className="nav col-12 col-lg-auto mb-2 justify-content-center mb-md-0">
            <li className="me-3">
              <Link
                className="nav-link px-2 link-body-emphasis position-relative"
                to="/notifications"
              >
                <img
                  src="././public/assets/sino.png"
                  alt="Sino"
                  width="25"
                  height="25"
                  className="d-block link-body-emphasis text-decoration-none dropdown-toggle"
                />
                <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                  3
                  <span className="visually-hidden">
                    Notificações não lidas
                  </span>
                </span>
              </Link>
            </li>
            <li>
              <div className="dropdown text-end">
                <a
                  href="#"
                  class="d-block link-body-emphasis text-decoration-none dropdown-toggle"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  <img
                    src="https://github.com/mdo.png"
                    alt="mdo"
                    width="32"
                    height="32"
                    className="rounded-circle"
                  />
                </a>
                <ul className="dropdown-menu text-small">
                  <li>
                    <a className="dropdown-item" href="#">
                      Minha conta
                    </a>
                  </li>
                  <li>
                    <hr className="dropdown-divider" />
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Sair
                    </a>
                  </li>
                </ul>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </header>
  );
};

export default Header;
