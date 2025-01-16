# Path do ambiente virtual do Poetry
VENV := $(shell poetry env info --path)

# Alvos
.PHONY: setup install dev run lint format test coverage clean

setup:
	@echo "Instalando pipx..."
	python3 -m pip install --user pipx
	python3 -m pipx ensurepath
	@echo "Instalando Poetry com pipx..."
	@export PATH="$$PATH:$$HOME/.local/bin" && pipx install poetry
	@echo "Poetry instalado com sucesso!"
	@echo "Pode ser necessário recarregar o shell para atualizar o PATH..."

install:
	poetry install --without dev

dev:
	poetry install --with dev

run:
	poetry run task run

lint:
	poetry run task lint

format:
	poetry run task format

test:
	poetry run task test

coverage:
	poetry run task post_test

clean:
	@echo "Deletando o ambiente virtual..."
	rm -rf $(VENV)
	@echo "Limpando o cache do projeto..."
	rm -rf .pytest_cache .ruff_cache coverage .coverage coverage.xml htmlcov
	@echo "Concluído com sucesso!"
