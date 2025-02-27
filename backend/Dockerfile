ARG PYTHON_VERSION=3.13.0
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY backend .

RUN apt-get update && apt-get install -y --no-install-recommends make

RUN pip install poetry

RUN poetry config installer.max-workers 10

RUN make install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.app:app", "--host=0.0.0.0", "--port=8000"]