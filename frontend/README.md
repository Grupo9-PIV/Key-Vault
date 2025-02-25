# Configuração de Ambiente de Desenvolvimento e Uso das Ferramentas (Frontend)

## Requisitos do Projeto

Este projeto utiliza **React** com **Vite** como bundler, **Yarn** como gerenciador de pacotes, **Axios** para requisições HTTP e **Bootstrap** para estilização. A seguir, são detalhadas as instruções para configurar o ambiente de desenvolvimento e utilizar as ferramentas disponíveis.

---

## Configuração do Ambiente de Desenvolvimento

### 1. Pré-requisitos

- **Node.js v23.2.0** ou superior.
- **Yarn** instalado globalmente.

### 2. Instalação do Yarn e Configuração Inicial

1. Instale o **Node.js**:

   - Baixe e instale a versão 23.2.0 do Node.js a partir do [site oficial](https://nodejs.org/) ou use um gerenciador de versões como **nvm** (Node Version Manager).

2. Instale o **Yarn** globalmente:

   ```bash
   npm install -g yarn
   ```

3. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/Grupo9-PIV/Key-Vault.git
   cd frontend
   ```

4. Instale as dependências do projeto:

   ```bash
   yarn install
   ```

---

## Execução do Projeto

### 1. Modo de Desenvolvimento

Para rodar o projeto em modo de desenvolvimento, utilize o seguinte comando:

```bash
yarn dev
```

Isso iniciará o servidor de desenvolvimento do Vite, e o projeto estará disponível em `http://localhost:5173` (ou outra porta, se configurada).

### 2. Build para Produção

Para gerar uma versão otimizada do projeto para produção, execute:

```bash
yarn build
```

Os arquivos de produção serão gerados na pasta `dist`.

### 3. Preview do Build de Produção

Para visualizar o build de produção localmente, utilize:

```bash
yarn preview
```

Isso iniciará um servidor local para visualizar o projeto como estará em produção.

---

## Tarefas Automatizadas com Scripts do Yarn

O projeto utiliza scripts do Yarn para facilitar a execução de tarefas comuns. Abaixo estão os principais scripts disponíveis:

### 1. **Execução do Servidor de Desenvolvimento**

```bash
yarn dev
```

Inicia o servidor de desenvolvimento do Vite.

### 2. **Build para Produção**

```bash
yarn build
```

Gera os arquivos otimizados para produção na pasta `dist`.

### 3. **Preview do Build de Produção**

```bash
yarn preview
```

Inicia um servidor local para visualizar o build de produção.

### 4. **Verificação de Código (Lint)**

```bash
yarn lint
```

Executa o **ESLint** para análise de código.

### 5. **Formatação de Código**

```bash
yarn format
```

Formata o código utilizando o **Prettier**.

### 6. **Testes**

Executar todos os testes:

```bash
yarn test
```

Executar testes em modo de observação (watch mode):

```bash
yarn test:watch
```

Executar testes e gerar relatório de cobertura:

```bash
yarn test:coverage
```

Executa os testes utilizando o **Jest**.

---

## Estrutura de Arquivos Relevantes

- **`package.json`**: Gerenciamento de dependências e scripts.
- **`vite.config.js`**: Configuração do Vite.
- **`src/`**: Pasta principal do código-fonte do projeto.
  - **`src/main.jsx`**: Ponto de entrada da aplicação.
  - **`src/App.jsx`**: Componente principal da aplicação.
  - **`src/components/`**: Componentes reutilizáveis.
  - **`src/styles/`**: Estilos globais e específicos.
  - **`src/api/`**: Configurações e chamadas HTTP com Axios.

---

## Adicionando Novas Dependências

Para adicionar uma nova dependência ao projeto, utilize o Yarn:

- Dependência de produção:

  ```bash
  yarn add nome-da-dependencia
  ```

- Dependência de desenvolvimento:

  ```bash
  yarn add -D nome-da-dependencia
  ```

Para atualizar os pacotes do Yarn utilize o comando:

```bash
yarn upgrade --latest
```

---

## Contribuindo com o Projeto

1. Crie uma branch para sua feature ou correção:

   ```bash
   git checkout -b minha-feature
   ```

1. Faça as alterações necessárias e certifique-se de que o código está formatado antes de enviar suas alterações:

   ```bash
   yarn format
   ```

1. Execute os testes para garantir que tudo está funcionando corretamente:

   ```bash
   yarn test
   ```

1. Faça o commit:

   ```bash
   git commit -m "Minha nova feature"
   ```

1. Envie as alterações para o repositório remoto:

   ```bash
   git push origin minha-feature
   ```

1. Abra um Pull Request no repositório.

---

## Dúvidas e Suporte

Se tiver dúvidas ou precisar de suporte, entre em contato com a equipe de desenvolvimento ou abra uma issue no repositório.
