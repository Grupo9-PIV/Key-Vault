import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import Header from '../components/Header';
import Footer from '../components/Footer';

const LicenseDetail = () => {
  useEffect(() => {
    document.title = 'Detalhes das Licenças';
  }, []);

  const { id } = useParams();

  return (
    <div>
      <Header />
      <h2>Detalhes da Licença</h2>
      <p>ID da Licença: {id}</p>
      {/* Aqui podemos adicionar mais informações futuramente */}
      <Footer />
    </div>
  );
};

export default LicenseDetail;
