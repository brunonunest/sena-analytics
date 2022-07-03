FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

FROM python:3.8-slim-buster

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements-docker.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]