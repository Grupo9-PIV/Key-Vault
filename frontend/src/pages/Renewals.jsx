import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";


import Header from "../components/Header";
import Footer from "../components/Footer";



const Renewals = () => {

  useEffect(() => {
      document.title = "Lista de Renovações"; 
    }, []);

  const [renewals, setRenewals] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/renewal_requests")
      .then((response) => response.json())
      .then((data) => {
        setRenewals(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Erro ao buscar renovações:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Carregando...</p>;
  if (renewals.length === 0) return <p>Nenhuma solicitação de renovação encontrada.</p>;

  return (
    <div>
      <Header />
      <h2>Solicitações de Renovação</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Licença</th>
            <th>Status</th>
            <th>Data da Solicitação</th>
          </tr>
        </thead>
        <tbody>
          {renewals.map((renewal) => (
            <tr key={renewal.id}>
              <td>
                <Link to={`/renewals/${renewal.id}`}>{renewal.id}</Link>
              </td>
              <td>{renewal.license_name}</td>
              <td>{renewal.status}</td>
              <td>{new Date(renewal.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <Footer />
    </div>
  );
};

export default Renewals;
