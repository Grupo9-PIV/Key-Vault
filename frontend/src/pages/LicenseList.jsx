import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const licensesMock = [
  {
    id: 1,
    software_name: 'Adobe Photoshop',
    status: 'Ativa',
    max_users: 10,
    in_use: 4,
    department: 'Design',
    acquisition_date: '2023-01-15',
    expiration_date: '2026-01-15',
  },
  {
    id: 2,
    software_name: 'Microsoft Office',
    status: 'Expirada',
    max_users: 50,
    in_use: 50,
    department: 'Administrativo',
    acquisition_date: '2020-06-10',
    expiration_date: '2023-06-10',
  },
  {
    id: 3,
    software_name: 'AutoCAD',
    status: 'Ativa',
    max_users: 20,
    in_use: 10,
    department: 'Engenharia',
    acquisition_date: '2022-05-20',
    expiration_date: '2025-05-20',
  },
  {
    id: 4,
    software_name: 'Visual Studio',
    status: 'Pendente',
    max_users: 15,
    in_use: 5,
    department: 'TI',
    acquisition_date: '2024-02-01',
    expiration_date: '2027-02-01',
  },
];

const LicenseList = () => {
  const [search, setSearch] = useState('');

  useEffect(() => {
    document.title = 'Lista de Licenças';
  }, []);

  const filteredLicenses = licensesMock
    .filter((license) =>
      license.software_name.toLowerCase().includes(search.toLowerCase())
    )
    .sort((a, b) => a.software_name.localeCompare(b.software_name));

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <header className="d-flex justify-content-between py-3 align-items-center">
          <div>
            <a href="/CreateUser" className="nav-link" aria-current="page">
              <button className="btn btn-dark me-2">Adicionar licença</button>
            </a>
          </div>
          <div>
            <form className="w-100 me-3" role="search">
              <input
                type="search"
                className="form-control ms-2"
                placeholder="Pesquisar licença..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </form>
          </div>
        </header>
      </div>
      <div className="container">
        <h2>Lista de Licenças</h2>
        <div className="table-responsive small">
          <table className="table table-striped table-sm dropdown">
            <thead>
              <tr>
                <th scope="col">Software</th>
                <th scope="col">Status</th>
                <th scope="col">Máx. Usuários</th>
                <th scope="col">Em Uso</th>
                <th scope="col">Departamento</th>
                <th scope="col">Data de Aquisição</th>
                <th scope="col">Data de Vencimento</th>
              </tr>
            </thead>
            <tbody>
              <tr data-bs-toggle="dropdown" aria-expanded="false">
                <td>Visual Studio</td>
                <td>Ativa</td>
                <td>20</td>
                <td>18</td>
                <td>TI</td>
                <td>11/03/2025</td>
                <td>11/03/2030</td>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="#">
                      Editar
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Excluir
                    </a>
                  </li>
                </ul>
              </tr>
              <tr data-bs-toggle="dropdown" aria-expanded="false">
                <td>Visual Studio</td>
                <td>Ativa</td>
                <td>20</td>
                <td>18</td>
                <td>TI</td>
                <td>11/03/2025</td>
                <td>11/03/2030</td>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="#">
                      Editar
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Excluir
                    </a>
                  </li>
                </ul>
              </tr>
              <tr data-bs-toggle="dropdown" aria-expanded="false">
                <td>Visual Studio</td>
                <td>Ativa</td>
                <td>20</td>
                <td>18</td>
                <td>TI</td>
                <td>11/03/2025</td>
                <td>11/03/2030</td>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="#">
                      Editar
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Excluir
                    </a>
                  </li>
                </ul>
              </tr>
              <tr data-bs-toggle="dropdown" aria-expanded="false">
                <td>Visual Studio</td>
                <td>Ativa</td>
                <td>20</td>
                <td>18</td>
                <td>TI</td>
                <td>11/03/2025</td>
                <td>11/03/2030</td>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="#">
                      Editar
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Excluir
                    </a>
                  </li>
                </ul>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      {/*
      <table className="license-table">
        <thead>
          <tr>
            <th>Software</th>
            <th>Status</th>
            <th>Máx. Usuários</th>
            <th>Em Uso</th>
            <th>Departamento</th>
            <th>Data de Aquisição</th>
            <th>Data de Vencimento</th>
          </tr>
        </thead>
        <tbody>
          {filteredLicenses.map((license) => (
            <tr key={license.id}>
              <td>
                <Link to={`/licenses/${license.id}`} className="license-link">
                  {license.software_name}
                </Link>
              </td>
              <td>{license.status}</td>
              <td>{license.max_users}</td>
              <td>{license.in_use}</td>
              <td>{license.department}</td>
              <td>{new Date(license.acquisition_date).toLocaleDateString()}</td>
              <td>{new Date(license.expiration_date).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
      */}
      <Footer />
    </div>
  );
};

export default LicenseList;
