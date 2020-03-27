docker pull puckel/docker-airflow
docker-compose -f docker-compose-airflow-setup.yml up -d
docker exec -u root -t -i airflow /bin/sh -c "pip install sklearn;pip install boruta"
