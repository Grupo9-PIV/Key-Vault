import React, { useEffect, useState } from "react";

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/notifications")
      .then((response) => response.json())
      .then((data) => {
        setNotifications(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Erro ao buscar notificações:", error);
        setLoading(false);
      });
  }, []);

  const markAsRead = (id) => {
    fetch(`http://localhost:8000/notifications/${id}/read`, {
      method: "PATCH",
    })
      .then((response) => response.json())
      .then((updatedNotification) => {
        setNotifications((prev) =>
          prev.map((notif) => (notif.id === id ? updatedNotification : notif))
        );
      })
      .catch((error) => console.error("Erro ao marcar como lida:", error));
  };

  if (loading) return <p>Carregando...</p>;
  if (notifications.length === 0) return <p>Nenhuma notificação encontrada.</p>;

  return (
    <div>
      <h2>Notificações</h2>
      <ul>
        {notifications.map((notif) => (
          <li key={notif.id} style={{ background: notif.is_read ? "#ddd" : "#fff" }}>
            <p><strong>Mensagem:</strong> {notif.message}</p>
            <p><strong>Data:</strong> {new Date(notif.created_at).toLocaleString()}</p>
            {!notif.is_read && (
              <button onClick={() => markAsRead(notif.id)}>Marcar como lida</button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
