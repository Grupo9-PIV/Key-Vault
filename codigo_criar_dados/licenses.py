from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from src.database import engine
from src.models.license import License
from src.models.user import User

# Criando a sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criar dados das 20 licenças
licenses_data = [
    {"software_name": "Microsoft Office", "license_type": "Perpétua", "status": "Ativa", "developed_by": "Microsoft", "version": "v1.0", "start_date": "2023-01-01", "end_date": "2025-01-01", "license_key": "MICOFF12345", "current_usage": 50, "subscription_plan": None, "priority": "Alta"},
    {"software_name": "Adobe Photoshop", "license_type": "Assinatura", "status": "Ativa", "developed_by": "Adobe", "version": None, "start_date": "2023-03-15", "end_date": "2024-03-15", "license_key": "ADOBE54321", "current_usage": 30, "subscription_plan": "Anual", "priority": "Média"},
    {"software_name": "Autocad", "license_type": "Perpétua", "status": "Expirada", "developed_by": "Autodesk", "version": "v2.3", "start_date": "2020-05-10", "end_date": "2023-05-10", "license_key": "AUTOCAD98765", "current_usage": 10, "subscription_plan": None, "priority": "Alta"},
    {"software_name": "Slack", "license_type": "Assinatura", "status": "Ativa", "developed_by": "Slack Technologies", "version": None, "start_date": "2022-07-01", "end_date": "2023-07-01", "license_key": "SLACK87654", "current_usage": 120, "subscription_plan": "Mensal", "priority": "Baixa"},
    {"software_name": "Zoom", "license_type": "Assinatura", "status": "Pendente", "developed_by": "Zoom Video Communications", "version": None, "start_date": "2023-06-01", "end_date": "2024-06-01", "license_key": "ZOOM11223", "current_usage": 70, "subscription_plan": "Anual", "priority": "Média"},
    {"software_name": "IntelliJ IDEA", "license_type": "Perpétua", "status": "Ativa", "developed_by": "JetBrains", "version": "v3.5", "start_date": "2022-10-10", "end_date": "2027-10-10", "license_key": "IDEA99887", "current_usage": 15, "subscription_plan": None, "priority": "Alta"},
    {"software_name": "Visual Studio", "license_type": "Perpétua", "status": "Ativa", "developed_by": "Microsoft", "version": "v4.0", "start_date": "2021-11-01", "end_date": "2026-11-01", "license_key": "VSTUDIO66789", "current_usage": 80, "subscription_plan": None, "priority": "Média"},
    {"software_name": "Python", "license_type": "Perpétua", "status": "Ativa", "developed_by": "Python Software Foundation", "version": "v3.10", "start_date": "2020-12-12", "end_date": "2025-12-12", "license_key": "PYTHON23456", "current_usage": 300, "subscription_plan": None, "priority": "Baixa"},
    {"software_name": "Docker", "license_type": "Perpétua", "status": "Ativa", "developed_by": "Docker, Inc.", "version": "v20.10", "start_date": "2021-01-01", "end_date": "2026-01-01", "license_key": "DOCKER90876", "current_usage": 60, "subscription_plan": None, "priority": "Alta"},
    {"software_name": "Jira", "license_type": "Assinatura", "status": "Ativa", "developed_by": "Atlassian", "version": None, "start_date": "2023-02-01", "end_date": "2024-02-01", "license_key": "JIRA87654", "current_usage": 200, "subscription_plan": "Trimestral", "priority": "Média"},
    {"software_name": "Sublime Text", "license_type": "Perpétua", "status": "Expirada", "developed_by": "Sublime HQ", "version": "v3.0", "start_date": "2019-06-01", "end_date": "2022-06-01", "license_key": "SUBLIME43210", "current_usage": 25, "subscription_plan": None, "priority": "Baixa"},
    {"software_name": "Notepad++", "license_type": "Perpétua", "status": "Ativa", "developed_by": "Notepad++ Team", "version": "v7.8", "start_date": "2022-05-01", "end_date": "2027-05-01", "license_key": "NOTEPAD56789", "current_usage": 90, "subscription_plan": None, "priority": "Média"},
    {"software_name": "GitHub", "license_type": "Assinatura", "status": "Pendente", "developed_by": "GitHub, Inc.", "version": None, "start_date": "2023-08-01", "end_date": "2024-08-01", "license_key": "GITHUB34567", "current_usage": 50, "subscription_plan": "Anual", "priority": "Alta"},
    {"software_name": "GitLab", "license_type": "Assinatura", "status": "Ativa", "developed_by": "GitLab, Inc.", "version": None, "start_date": "2023-04-15", "end_date": "2024-04-15", "license_key": "GITLAB87654", "current_usage": 45, "subscription_plan": "Semestral", "priority": "Média"},
    {"software_name": "Node.js", "license_type": "Perpétua", "status": "Ativa", "developed_by": "OpenJS Foundation", "version": "v16.0", "start_date": "2021-09-01", "end_date": "2026-09-01", "license_key": "NODEJS99876", "current_usage": 120, "subscription_plan": None, "priority": "Baixa"},
    {"software_name": "MongoDB", "license_type": "Perpétua", "status": "Ativa", "developed_by": "MongoDB, Inc.", "version": "v4.2", "start_date": "2020-01-01", "end_date": "2025-01-01", "license_key": "MONGO12345", "current_usage": 80, "subscription_plan": None, "priority": "Alta"},
    {"software_name": "PostgreSQL", "license_type": "Perpétua", "status": "Ativa", "developed_by": "PostgreSQL Global Development Group", "version": "v13.4", "start_date": "2020-03-01", "end_date": "2025-03-01", "license_key": "POSTGRES54321", "current_usage": 150, "subscription_plan": None, "priority": "Média"},
    {"software_name": "MySQL", "license_type": "Perpétua", "status": "Ativa", "developed_by": "Oracle Corporation", "version": "v8.0", "start_date": "2021-05-01", "end_date": "2026-05-01", "license_key": "MYSQL87654", "current_usage": 200, "subscription_plan": None, "priority": "Alta"},
    {"software_name": "Redis", "license_type": "Perpétua", "status": "Ativa", "developed_by": "Redis Labs", "version": "v6.2", "start_date": "2022-02-01", "end_date": "2027-02-01", "license_key": "REDIS23456", "current_usage": 100, "subscription_plan": None, "priority": "Média"},
    {"software_name": "Vue.js", "license_type": "Perpétua", "status": "Ativa", "developed_by": "Evan You", "version": "v3.0", "start_date": "2021-10-01", "end_date": "2026-10-01", "license_key": "VUEJS45678", "current_usage": 180, "subscription_plan": None, "priority": "Baixa"}
]

# Inserir as 20 licenças no banco de dados
for license_data in licenses_data:
    new_license = License(
        software_name=license_data['software_name'],
        license_type=license_data['license_type'],
        status=license_data['status'],
        developed_by=license_data['developed_by'],
        version=license_data['version'],
        start_date=datetime.strptime(license_data['start_date'], "%Y-%m-%d"),
        end_date=datetime.strptime(license_data['end_date'], "%Y-%m-%d"),
        license_key=license_data['license_key'],
        current_usage=license_data['current_usage'],
        subscription_plan=license_data['subscription_plan'],
        priority=license_data['priority']
    )
    session.add(new_license)

# Commit para salvar no banco de dados
session.commit()

print("As 20 licenças foram inseridas no banco de dados com sucesso!")

# Fechar a sessão
session.close()
