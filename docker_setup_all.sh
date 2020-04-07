docker build -t mlflow ./mlflow
docker-compose -f docker-compose.yml up -d

docker run -d -p 9000:9000 --name minio -v /c/Gits/ml_workflow_orchestration/minio/data:/data minio/minio server /data

# additional install
docker exec -u root -t -i airflow //bin/sh -c "pip install sklearn;pip install boruta;pip install mlflow==1.7.2;pip install boto3"
docker exec -u root -t -i mlflow //bin/sh -c "pip install boto3"

