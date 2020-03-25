docker pull puckel/docker-airflow
docker run -d -p 8080:8080 -v /c/Users/ROG/WD/gits/ml_workflow_orchestration/airflow/airflow_home/dags:/usr/local/airflow/dags puckel/docker-airflow webserver



