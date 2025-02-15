import random
from datetime import datetime, timedelta
import csv

# Definindo um conjunto de dados possíveis
license_ids = list(range(1, 21))  # IDs das licenças (de 1 a 20)
user_ids = list(range(1, 51))  # IDs dos usuários (de 1 a 50)
status_options = ['pendente', 'aprovada', 'rejeitada']
reasons = [
    "Necessidade de atualizar versão do software.",
    "Licença expirando em breve.",
    "Mudança de setor que exige renovação.",
    "Expansão do uso da licença.",
    "Licença não está mais atendendo às necessidades.",
    "Atraso no pagamento, renovação necessária.",
    "Problemas de compatibilidade com a versão atual.",
    "Aumento do número de usuários.",
    "Novo recurso adquirido, renovação necessária.",
    "Problemas técnicos com a versão anterior."
]
feedbacks = [
    "Aguardando aprovação do gerente.",
    "Aprovado pelo gerente.",
    "Aguardando recursos financeiros para renovação.",
    "Licença em revisão.",
    "Esperando documentação complementar."
]

# Função para gerar dados fictícios para a tabela de RenewalRequests
def generate_renewal_requests(num_requests):
    requests = []
    for _ in range(num_requests):
        license_id = random.choice(license_ids)  # Seleciona uma licença aleatória
        requested_by_id = random.choice(user_ids)  # Seleciona um usuário aleatório para a solicitação
        manager_id = random.choice(user_ids)  # Seleciona um gerente aleatório
        reason = random.choice(reasons)  # Seleciona um motivo aleatório
        feedback = random.choice(feedbacks)  # Seleciona um feedback aleatório
        status = random.choice(status_options)  # Seleciona o status da solicitação
        created_at = datetime.now() - timedelta(days=random.randint(1, 30))  # Data aleatória de criação
        updated_at = created_at if random.random() < 0.5 else created_at + timedelta(days=random.randint(1, 15))  # Atualização aleatória
        
        # Cria o dicionário com os dados da solicitação
        request = {
            'id': _ + 1,
            'license_id': license_id,
            'requested_by_id': requested_by_id,
            'manager_id': manager_id,
            'reason': reason,
            'feedback': feedback,
            'status': status,
            'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': updated_at.strftime('%Y-%m-%d %H:%M:%S') if updated_at else None,
        }
        requests.append(request)
    
    return requests

# Gerar 20 solicitações de renovação
renewal_requests = generate_renewal_requests(20)

# Salvar em um arquivo CSV
with open('renewal_requests.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=renewal_requests[0].keys())
    writer.writeheader()
    writer.writerows(renewal_requests)

print("Arquivo 'renewal_requests.csv' gerado com sucesso!")
