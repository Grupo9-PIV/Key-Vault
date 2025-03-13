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
          {/* Seção não editável */}
          <div className="mb-5 row">

            <div className="col-md-4 text-center mb-3 mb-md-0">
              <img 
                src="https://github.com/mdo.png" 
                alt="User" 
                className="rounded-circle"
                width="200"
                height="200"
              />
            </div>

            <div className="col-md-8">
              <div className="mb-3">
                <label htmlFor="name" className="form-label">Nome</label>
                <input 
                  type="text" 
                  className="form-control" 
                  id="name" 
                  defaultValue="Ewellyn Almeida" 
                  disabled 
                />
              </div>
              <div className="mb-3">
                <label htmlFor="email" className="form-label">E-mail</label>
                <input 
                  type="email" 
                  className="form-control" 
                  id="email" 
                  defaultValue="lynn@gmail.com" 
                  disabled 
                />
              </div>
            </div>
          </div>

          <form>
            <div className="mb-3">
              <label htmlFor="password" className="form-label">Nova Senha</label>
              <input 
                type="password" 
                className="form-control" 
                id="password" 
                placeholder="Digite a nova senha" 
              />
            </div>
            <div className="mb-3">
              <label htmlFor="role" className="form-label">Função</label>
              <input 
                type="text" 
                className="form-control" 
                id="role" 
                defaultValue="Admin" 
              />
            </div>
            <div className="mb-3">
              <label htmlFor="department" className="form-label">Departamento</label>
              <input 
                type="text" 
                className="form-control" 
                id="department" 
                defaultValue="TI" 
              />
            </div>
            <div className="d-flex gap-2">
              <button type="submit" className="btn btn-primary">Salvar</button>
              <button type="button" className="btn btn-secondary">Cancelar</button>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default EditUser;