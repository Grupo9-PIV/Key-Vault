import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/style.css';

const EditUser = () => {
  return (
    <div className="page-container">
      <Header />
      <div className="container">
      <h2 className="pb-2 border-bottom">Editar Usuário</h2>
      <div className="py-5">
        <form>
          <div className="mb-3">
            <label htmlFor="name" className="form-label">Nome</label>
            <input type="text" className="form-control" id="name" defaultValue="Ewellyn Almeida" />
          </div>
          <div className="mb-3">
            <label htmlFor="email" className="form-label">E-mail</label>
            <input type="email" className="form-control" id="email" defaultValue="lynn@gmail.com" />
          </div>
          <div className="mb-3">
            <label htmlFor="role" className="form-label">Função</label>
            <input type="text" className="form-control" id="role" defaultValue="Admin" />
          </div>
          <div className="mb-3">
            <label htmlFor="role" className="form-label">Departamento</label>
            <input type="text" className="form-control" id="depatment" defaultValue="TI" />
          </div>
          <div className="d-flex gap-2">
            <button type="submit" className="btn btn-primary">Salvar</button>
            <button type="submit" className="btn btn-secondary">Cancelar</button>
          </div>
        </form>
      </div>

      </div>
      <Footer />
    </div>
  );
};

export default EditUser;