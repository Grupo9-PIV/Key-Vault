import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

const RenewalDetail = () => {
  const { id } = useParams();
  const [renewal, setRenewal] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://localhost:8000/renewal_requests/${id}`)
      .then((response) => response.json())
      .then((data) => {
        setRenewal(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Erro ao buscar detalhes da renovação:", error);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Carregando...</p>;
  if (!renewal) return <p>Renovação não encontrada.</p>;

  return (
    <div>
      <h2>Detalhes da Solicitação de Renovação</h2>
      <p><strong>ID:</strong> {renewal.id}</p>
      <p><strong>Licença:</strong> {renewal.license_name}</p>
      <p><strong>Status:</strong> {renewal.status}</p>
      <p><strong>Data da Solicitação:</strong> {new Date(renewal.created_at).toLocaleString()}</p>
      <p><strong>Motivo:</strong> {renewal.reason}</p>

      <Link to="/renewals">← Voltar para a lista de renovações</Link>
    </div>
  );
};

export default RenewalDetail;
