from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import engine
from src.models.notification import Notification
from datetime import datetime
import random

# Criar a sessão
Session = sessionmaker(bind=engine)
session = Session()

# Dados para criar as notificações
notifications_data = []

# Mensagens predefinidas para as notificações
messages = [
    "Sua licença de software está prestes a expirar.",
    "Solicitação de renovação da licença recebida.",
    "Licença renovada com sucesso.",
    "A ação solicitada foi realizada com sucesso.",
    "Acesso revogado à licença de software.",
    "Licença adicionada ao seu nome.",
    "Aviso de expiração de licença em breve.",
    "A licença de software foi transferida.",
    "Solicitação de renovação rejeitada.",
    "Novo software foi alocado à sua conta."
]

# Supomos que já existem 50 usuários, 20 licenças e 10 solicitações de renovação
user_ids = list(range(1, 51))  # IDs dos usuários
license_ids = list(range(1, 21))  # IDs das licenças
request_ids = list(range(1, 11))  # IDs das solicitações de renovação

# Gerar 50 notificações fictícias
for _ in range(50):
    user_id = random.choice(user_ids)
    license_id = random.choice(license_ids) if random.choice([True, False]) else None  # License opcional
    request_id = random.choice(request_ids) if random.choice([True, False]) else None  # Request opcional
    message = random.choice(messages)  # Mensagem aleatória
    is_read = random.choice([True, False])  # Status de leitura aleatório

    notification = {
        "user_id": user_id,
        "license_id": license_id,
        "request_id": request_id,
        "message": message,
        "is_read": is_read,
        "created_at": datetime.now()
    }

    notifications_data.append(notification)

# Inserir as notificações no banco de dados
for notification_data in notifications_data:
    new_notification = Notification(
        user_id=notification_data['user_id'],
        license_id=notification_data['license_id'],
        request_id=notification_data['request_id'],
        message=notification_data['message'],
        is_read=notification_data['is_read'],
        created_at=notification_data['created_at']
    )
    session.add(new_notification)

# Commit para salvar no banco de dados
session.commit()

print("As 50 notificações foram inseridas no banco de dados com sucesso!")

# Fechar a sessão
session.close()
