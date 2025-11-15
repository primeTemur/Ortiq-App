FROM python:3.14-rc-slim-bookworm

ENV PYTONONDONTWRITEBYTECODE=1 \
PYTONUNBUFFERED=1

WORKDIR /app

RUN apt-get update 

RUN pip install --no-cache-dir django djangorestframework psycopg2-binary

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY /requirements.txt .
RUN uv pip install -r requirements.txt --system

COPY / .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

