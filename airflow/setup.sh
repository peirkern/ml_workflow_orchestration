docker pull puckel/docker-airflow
docker-compose -f docker-compose.yml up -d
docker exec -u root -t -i airflow /bin/sh -c "pip install sklearn;pip install boruta;pip install mlflow==1.7.2;pip install boto3"
