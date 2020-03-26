from __future__ import print_function
import time
from builtins import range
from pprint import pprint
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'pk',
    'depends_on_past': False,
    'start_date': datetime(2020, 3, 15),
    'email': ['peirkern@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
	'schedule_interval': '@daily',
}

dag = DAG(
    dag_id='trial_ml',
    default_args=args,
    tags=['example'],
	catchup=True
)

def task_download_data(ds, **kwargs):
	print("task: task_download_data")
	content = requests.get('https://archive.org/download/datasets_202003/aps-failure-at-scania-trucks-data-set.zip')
	f = ZipFile(BytesIO(content.content))
	f.extractall("/tmp/airflow/trial_ml/"+context['execution_date']+"/data")

t1 = PythonOperator(
	task_id='download_data',
    python_callable=task_download_data(),
    provide_context=True,
    dag=dag
)



	