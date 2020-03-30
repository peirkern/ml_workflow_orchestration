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
import pandas as pd
from sklearn.externals import joblib
from boruta import boruta_py

args = {
    'owner': 'pk',
    'depends_on_past': False,
    'email': ['peirkern@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='demo_inference',
    default_args=args,
    tags=['example'],
	catchup=True, 
	schedule_interval='0 1 * * *', 
	start_date=datetime(2020, 3, 24)
)

def task_download_data(**kwargs):
	content = requests.get('https://archive.org/download/datasets_202003/aps-failure-at-scania-trucks-data-set.zip')
	f = ZipFile(BytesIO(content.content))
	f.extractall("/tmp/airflow/output/demo_inference/" + str(kwargs['execution_date'])[0:10] + "/download_data")
	
def process_data(**kwargs):
	test_ds =  pd.read_csv("/tmp/airflow/output/demo_inference/" + str(kwargs['execution_date'])[0:10] + "/download_data/aps_failure_test_set_processed_8bit.csv", na_values='na')
	test_features = test_ds.drop('class', axis=1)
	test_features_balanced = test_features
	scaler = joblib.load("/tmp/airflow/models/MinMaxScaler.save")
	test_features_balanced = pd.DataFrame(scaler.transform(test_features_balanced), columns=test_features_balanced.columns)
	test_features_balanced.to_csv("/tmp/airflow/output/demo_inference/" + str(kwargs['execution_date'])[0:10] + "/processed_data.csv", index = False, header=True)

def predict(**kwargs):
	train_features_balanced = pd.read_csv("/tmp/airflow/output/demo_inference/" + str(kwargs['execution_date'])[0:10] + "/processed_data.csv")
	boruta_pipeline = joblib.load("/tmp/airflow/models/boruta_pipeline.save") 
	y_pred = boruta_pipeline.predict_proba(train_features_balanced.values)
	pd.DataFrame(y_pred).to_csv("/tmp/airflow/output/demo_inference/" + str(kwargs['execution_date'])[0:10] + "/result.csv", index = False, header=True)

t1 = PythonOperator(
	task_id='task_download_data',
    python_callable=task_download_data,
    provide_context=True,
    dag=dag,
)

t2 = PythonOperator(
	task_id='task_process_data',
    python_callable=process_data,
    provide_context=True,
    dag=dag,
)

t3 = PythonOperator(
	task_id='task_predict',
    python_callable=predict,
    provide_context=True,
    dag=dag,
)

t1 >> t2 >> t3
