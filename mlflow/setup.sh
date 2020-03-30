docker build -t mlflow .
docker-compose -f docker-compose.yml up -d
docker exec -u root -t -i mlflow /bin/sh -c "pip install boto3"
