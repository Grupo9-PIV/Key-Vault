import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

const UserList = () => {
  useEffect(() => {
    document.title = 'Lista de Usuários';
  }, []);

  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/users')
      .then((response) => response.json())
      .then((data) => {
        setUsers(data.users);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Erro ao buscar usuários:', error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Carregando...</p>;

  return (
    <div className="page-container">
      <Header />
      <div className="container">
        <header className="d-flex justify-content-between py-3 align-items-center">
          <div>
            <a href="/createuser" className="nav-link" aria-current="page">
              <button className="btn btn-dark me-2">Criar usuário</button>
            </a>
          </div>
          <div>
            <form className="w-100 me-3" role="search">
              <input
                type="search"
                className="form-control ms-2"
                placeholder="Search..."
                aria-label="Search"
              />
            </form>
          </div>
        </header>
      </div>
      <div className="container">
        <h2>Lista de Usuários</h2>
        <div className="table-responsive small">
          <table className="table table-striped table-sm dropdown">
            <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Nome</th>
                <th scope="col">E-mail</th>
                <th scope="col">Papel</th>
                <th scope="col">Departamento</th>
                <th scope="col">1º Login</th>
                <th scope="col">Criação</th>
              </tr>
            </thead>
            <tbody>
              <tr data-bs-toggle="dropdown" aria-expanded="false">
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
                <td>54858</td>
                <td>Ewellyn Almeida</td>
                <td>lynn@gmail.com</td>
                <td>Admin</td>
                <td>TI</td>
                <td>Não</td>
                <td>25/02/2025</td>
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
          <h2>Lista de Usuários</h2>*
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
                <th>Função</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user) => (
                <tr key={user.id}>
                  <td>{user.id}</td>
                  <td>
                    <a href={`/users/${user.id}`}>{user.name}</a>
                  </td>
                  <td>{user.email}</td>
                  <td>{user.role}</td>
                </tr>
              ))}
            </tbody>
          </table>
        */}
      <Footer />
    </div>
  );
};

export default UserList;
