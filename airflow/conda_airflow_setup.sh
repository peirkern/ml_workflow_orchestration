# TO BE FIGURE OUT LATER
# docker pull puckel/docker-airflow
# docker run -d -p 8080:8080 puckel/docker-airflow webserver

conda create -n airflow python=3.6
conda.bat activate airflow

export AIRFLOW_HOME=/d/WD/gits/ml_workflow_orchestration/airflow/airflow_home

# install from pypi using pip
pip install apache-airflow

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080

# start the scheduler
airflow scheduler