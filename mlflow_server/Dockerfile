FROM python:3.7-slim-buster

LABEL maintainer "PK <peirkern@gmail.com>"

RUN mkdir /mlflow/

RUN pip install mlflow==1.7.2

EXPOSE 5000

CMD mlflow server \
    --file-store /mlflow \
    --host 0.0.0.0
