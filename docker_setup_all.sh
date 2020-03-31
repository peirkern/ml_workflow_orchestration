docker build -t mlflow ./mlflow
docker-compose -f docker-compose.yml up -d

docker run -d -p 9000:9000 --name minio -v /c/Users/ROG/WD/gits/ml_workflow_orchestration/minio/data:/data minio/minio server /data

# additional install
docker exec -u root -t -i airflow /bin/sh -c "pip install sklearn;pip install boruta"
docker exec -u root -t -i mlflow /bin/sh -c "pip install boto3"

