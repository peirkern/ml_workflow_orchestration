from __future__ import print_function
import time
from builtins import range
from pprint import pprint
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
from io import BytesIO
from zipfile import ZipFile

args = {
    'owner': 'pk',
    'depends_on_past': False,
    'email': ['peirkern@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='trial_ml',
    default_args=args,
    tags=['example'],
	catchup=True, 
	schedule_interval='0 1 * * *', 
	start_date=datetime(2020, 3, 15)
)

def task_download_data(**kwargs):
	content = requests.get('https://archive.org/download/datasets_202003/aps-failure-at-scania-trucks-data-set.zip')
	f = ZipFile(BytesIO(content.content))
	f.extractall("/tmp/airflow/output/trial_ml/" + str(kwargs['execution_date'])[0:10] + "/download_data")

t1 = PythonOperator(
	task_id='task_download_data',
    python_callable=task_download_data,
    provide_context=True,
    dag=dag,
)
