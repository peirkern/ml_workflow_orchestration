docker build -t mlflow .
docker-compose -f docker-compose-mlflow-server-setup.yml up -d
docker exec -u root -t -i mlflow_server /bin/sh -c "pip install boto3"
