FROM python:3.9.6-slim

ARG REQUIREMENTS="--system --dev"

ENV PYTHONUNBUFFERED 1
ENV TZ 'America/Sao_Paulo'

COPY utils/docker/entrypoint.sh .

WORKDIR /api

COPY src ./src

COPY requirements.txt .
COPY requirements-dev.txt .
COPY utils/docker/wait-for-it.sh /wait-for-it.sh

RUN pip install -r requirements-dev.txt

EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]