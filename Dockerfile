FROM python:3.11

WORKDIR /app
ADD pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry config virtualenvs.create true --local
RUN poetry config virtualenvs.in-project true --local

RUN poetry install --no-dev

RUN chmod +x .venv/bin/activate

COPY . /app

ENV LOGIN="admin"\
    EMAIL="admin@admin.pl"\
    ADMIN_PASSWORD="cF3dizpkHR37tHx"

ENTRYPOINT ["sh", "-c", " \
    PATH=.venv/bin:$PATH && \
    python -m pytest && \
    python manage.py collectstatic --no-input --clear && \
    python manage.py migrate && \
    python create_superuser.py $LOGIN $EMAIL $ADMIN_PASSWORD && \
    python manage.py runserver 0.0.0.0:8080 \
"]
