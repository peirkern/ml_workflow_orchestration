docker build -t mlflow ./mlflow
docker-compose -f docker-compose.yml up -d

#docker run -d -p 9000:9000 --name minio -v //c/Gits/ml_workflow_orchestration/minio/data:/data minio/minio:RELEASE.2020-04-04T05-39-31Z server /data

# additional install
docker exec -u root -t -i airflow //bin/sh -c "pip install sklearn;pip install boruta;pip install mlflow==1.7.1;pip install boto3==1.12.32"

