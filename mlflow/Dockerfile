FROM python:3.7-slim-buster

LABEL maintainer "PK <peirkern@gmail.com>"

RUN mkdir /mlflow/

RUN pip install mlflow==1.7.2

EXPOSE 5000

ENV MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
ENV AWS_ACCESS_KEY_ID=minioadmin
ENV AWS_SECRET_ACCESS_KEY=minioadmin

CMD mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --host 0.0.0.0 \
    --default-artifact-root s3://mlflow/artifacts
	


