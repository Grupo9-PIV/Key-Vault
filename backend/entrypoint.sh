#!/bin/sh

# Executa as migrations no banco de dados
poetry run alembic upgrade head

# Inicia a API
poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000