FROM python:3.11

WORKDIR /app
ADD pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry config virtualenvs.create true --local
RUN poetry config virtualenvs.in-project true --local

RUN poetry install --no-dev

RUN chmod +x .venv/bin/activate

COPY . /app