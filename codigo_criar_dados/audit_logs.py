from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from src.database import engine
from src.models.audit_log import AuditLog
from src.models.user import User
from src.models.license import License

# Criando a sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criar dados dos audit logs (logs de auditoria)
audit_logs_data = [
    {"performed_by_id": 1, "entity_id": 1, "entity": "license", "action": "Status Atualizado para Ativo", "timestamp": "2023-02-15 10:00:00"},
    {"performed_by_id": 2, "entity_id": 2, "entity": "license", "action": "Licença Expirada", "timestamp": "2023-02-15 10:05:00"},
    {"performed_by_id": 3, "entity_id": 3, "entity": "license", "action": "Status Atualizado para Expirado", "timestamp": "2023-02-15 10:10:00"},
    {"performed_by_id": 4, "entity_id": 4, "entity": "license", "action": "Renovação da Licença", "timestamp": "2023-02-15 10:15:00"},
    {"performed_by_id": 1, "entity_id": 5, "entity": "license", "action": "Status Atualizado para Pendente", "timestamp": "2023-02-15 10:20:00"},
    {"performed_by_id": 2, "entity_id": 6, "entity": "license", "action": "Status Atualizado para Ativo", "timestamp": "2023-02-15 10:25:00"},
    {"performed_by_id": 3, "entity_id": 7, "entity": "license", "action": "Licença Expirada", "timestamp": "2023-02-15 10:30:00"},
    {"performed_by_id": 4, "entity_id": 8, "entity": "license", "action": "Renovação da Licença", "timestamp": "2023-02-15 10:35:00"},
    {"performed_by_id": 1, "entity_id": 9, "entity": "license", "action": "Status Atualizado para Ativo", "timestamp": "2023-02-15 10:40:00"},
    {"performed_by_id": 2, "entity_id": 10, "entity": "license", "action": "Status Atualizado para Expirado", "timestamp": "2023-02-15 10:45:00"},
]

# Inserir os audit logs no banco de dados
for log_data in audit_logs_data:
    # Ação realizada
    new_audit_log = AuditLog(
        performed_by_id=log_data['performed_by_id'],
        entity_id=log_data['entity_id'],
        entity=log_data['entity'],
        action=log_data['action'],
        timestamp=datetime.strptime(log_data['timestamp'], "%Y-%m-%d %H:%M:%S")
    )
    session.add(new_audit_log)

# Commit para salvar no banco de dados
session.commit()

print("Os logs de auditoria foram inseridos no banco de dados com sucesso!")

# Fechar a sessão
session.close()
