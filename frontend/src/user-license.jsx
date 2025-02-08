import React from 'react';
import './user-license.css'; 

{/*Rascunho inicial da tela, quando tiver o banco de dados e o backend precisa ajusar para puxar dados de usuários e etc. */}

const UserLicense = () => {
    return (
      <div className="container"> {/* Container principal para centralizar tudo */}
        
        {/* Título */}
        <div className="banner">
          Licenças de usuários
        </div>

        {/* Container do formulário */}
        <div className="form-container">

          {/* Seção para seleção de departamento */}
          <div>
            <div className="label-box">Departamento</div> {/* Rótulo da caixa */}
            <select id="department" className="select-box"> {/* Dropdown */}
              <option value="">Selecione um departamento</option>
            </select>
          </div>

          {/* Seção para seleção de usuário */}
          <div>
            <div className="label-box">Usuário</div> {/* Rótulo da caixa */}
            <select id="user" className="select-box"> {/* Dropdown */}
              <option value="">Selecione um usuário</option>
            </select>
          </div>

          {/* Seção para seleção do tipo de licença */}
          <div>
            <div className="label-box">Tipo de licença</div> {/* Rótulo da caixa */}
            <select id="license-type" className="select-box"> {/* Dropdown */}
              <option value="">Selecione um tipo de licença</option>
            </select>
          </div>

          {/* Seção para seleção de chave */}
          <div>
            <div className="label-box">Selecionar chave</div> {/* Rótulo da caixa */}
            <select id="key" className="select-box"> {/* Dropdown */}
              <option value="">Selecione uma chave</option>
            </select>
          </div>

          {/* Botão para atribuir/remover licença */}
          <button className="button" disabled>
            Atribuir/Remover
          </button>

        </div>
      </div>
    );
};

export default UserLicense; // Exporta o componente para ser usado em outros arquivos
