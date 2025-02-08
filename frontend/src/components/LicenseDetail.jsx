import { useParams } from "react-router-dom";

const LicenseDetail = () => {
  const { id } = useParams();

  return (
    <div>
      <h2>Detalhes da Licença</h2>
      <p>ID da Licença: {id}</p>
      {/* Aqui podemos adicionar mais informações futuramente */}
    </div>
  );
};

export default LicenseDetail;
