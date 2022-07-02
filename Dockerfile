FROM ubuntu:16.04

#MAINTANER Your Name "brunonunest@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

FROM python:3.8-slim-buster

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]