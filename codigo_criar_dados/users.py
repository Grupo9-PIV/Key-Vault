from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import engine
from src.models.user import User
from datetime import datetime
import random
import faker
from src.enums import UserRole

# Criar a sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inicializar o gerador de dados fictícios
fake = faker.Faker()

# Criar dados dos usuários
users_data = []

# Definir as opções de cargos, departamentos e o papel do usuário
roles = [UserRole.ADMIN, UserRole.USER, UserRole.MANAGER]
departments = ['TI', 'RH', 'Marketing', 'Financeiro', 'Vendas', 'Jurídico']

# Gerar 50 usuários fictícios
for _ in range(50):
    name = fake.name()
    email = fake.email()
    role = random.choice(roles)
    department = random.choice(departments)
    password_hash = fake.sha256()  # Simulando um hash de senha
    is_first_login = random.choice([True, False])  # Aleatório entre True e False

    user = {
        "name": name,
        "email": email,
        "password_hash": password_hash,
        "role": role,
        "department": department,
        "is_first_login": is_first_login,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    users_data.append(user)

# Inserir os dados no banco de dados
for user_data in users_data:
    new_user = User(
        name=user_data['name'],
        email=user_data['email'],
        password_hash=user_data['password_hash'],
        role=user_data['role'],
        department=user_data['department'],
        is_first_login=user_data['is_first_login'],
        created_at=user_data['created_at'],
        updated_at=user_data['updated_at']
    )
    session.add(new_user)

# Commit para salvar no banco de dados
session.commit()

print("Os 50 usuários foram inseridos no banco de dados com sucesso!")

# Fechar a sessão
session.close()
