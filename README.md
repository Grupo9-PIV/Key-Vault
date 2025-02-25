# Projeto-Integrador-V
Projeto Integrador V: Análise de Soluções Integradas para Organizações


# 💻 Gerenciamento de Licenças de Software

## ✨ Introdução
Este projeto tem como objetivo desenvolver um sistema de gerenciamento de licenças de software para uma empresa. O sistema permite registrar e acompanhar informações sobre licenças adquiridas, incluindo onde estão instaladas, origem, custo, vencimento, quem está usando e o histórico de uso. Com essa ferramenta, a empresa pode otimizar o uso das licenças e garantir conformidade com os contratos.

## 📚 Funcionalidades Principais
- ✅ Cadastro e listagem de licenças de software
- 📊 Detalhamento de cada licença
- ⚠️ Controle de status (ativa, expirada, pendente)
- 👥 Acompanhamento do número de usuários
- 👤 Listagem e gerenciamento de usuários
- 🔐 Autenticação segura via JWT
- 🔍 Pesquisa e ordenação de registros

## 💪 Tecnologias Utilizadas
### Backend
- **FastAPI** - Framework para criação da API
- **SQLAlchemy** - ORM para interação com o banco de dados
- **Pydantic** - Validação de dados
- **JWT** - Autenticação segura

### Frontend
- **React com Vite** - Desenvolvimento da interface
- **Axios** - Consumo da API
- **Tailwind CSS** - Estilização

### Infraestrutura
- **Docker** - Contêinerização do ambiente
- **Nginx** - Proxy reverso
- **GitHub Actions** - CI/CD para automação de deploy

## ⚙️ Instalação e Execução
### ⚡ Requisitos
- Python 3.10+
- Node.js 16+
- Docker (opcional, mas recomendado)

### ✨ Configuração do Backend
1. Clone o repositório:
   ```bash
   git clone git@github.com:Grupo9-PIV/Key-Vault.git
   cd backend
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente em um arquivo `.env`
4. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```

### 🚀 Configuração do Frontend
1. Acesse a pasta do frontend:
   ```bash
   cd ../frontend
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```

## 👥 Contribuição
Contribuições são bem-vindas! Siga o fluxo padrão de pull request e mantenha o código bem documentado.

## ⚖️ Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

