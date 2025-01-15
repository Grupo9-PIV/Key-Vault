# Configuração de Ambiente de Desenvolvimento e Uso das Ferramentas

## Requisitos do Projeto

Este projeto utiliza o framework **FastAPI** e gerenciador de dependências **Poetry**. A seguir, são detalhadas as instruções para configurar o ambiente de desenvolvimento e utilizar as ferramentas disponíveis.

---

## Configuração do Ambiente de Desenvolvimento

### 1. Pré-requisitos

- **Python 3.13** ou superior.
- **Pipx** instalado no sistema.
- **Poetry** para gerenciar dependências e tarefas.

### 2. Instalação do Poetry e Configuração Inicial

1. Instale o **Pipx**:

   ```bash
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```

2. Instale o **Poetry**:

   ```bash
   pipx install poetry
   ```

   > **Nota:** Pode ser necessário recarregar o shell para atualizar o `PATH`.

3. Instale as dependências do projeto:

   - Modo produção (somente dependências principais):

     ```bash
     poetry install --without dev
     ```

   - Modo desenvolvimento (inclui dependências de desenvolvimento):

     ```bash
     poetry install --with dev
     ```

---

## Tarefas Automatizadas com Makefile

O projeto fornece um `Makefile` para facilitar a execução de tarefas comuns.

### Alvos Disponíveis

#### 1. **Configuração do Ambiente**

```bash
make setup
```

Configura o ambiente instalando o **Pipx** e o **Poetry**.

#### 2. **Instalação das Dependências**

- Produção:

  ```bash
  make install
  ```

- Desenvolvimento:

  ```bash
  make dev
  ```

#### 3. **Execução do Servidor**

```bash
make run
```

Executa o servidor FastAPI em modo de desenvolvimento.

#### 4. **Verificação de Código (Lint)**

```bash
make lint
```

Executa o **Ruff** para análise de código.

#### 5. **Formatação de Código**

```bash
make format
```

Formata o código utilizando o **Ruff**.

#### 6. **Testes**

```bash
make test
```

Executa os testes com **pytest** e gera relatórios de cobertura.

#### 7. **Cobertura de Testes**

```bash
make coverage
```

Gera um relatório HTML com a cobertura dos testes.

#### 8. **Limpeza do Ambiente**

```bash
make clean
```

Remove o ambiente virtual, caches e relatórios de cobertura.

---

## Estrutura de Arquivos Relevantes

- **`pyproject.toml`**: Gerenciamento de dependências e configuração de ferramentas.
- **`Makefile`**: Automação de tarefas comuns.
