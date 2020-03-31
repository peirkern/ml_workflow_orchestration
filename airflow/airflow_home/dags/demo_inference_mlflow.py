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
import mlflow
import mlflow.sklearn

args = {
    'owner': 'pk',
    'depends_on_past': True,
    'email': ['peirkern@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

dag_id = "demo_inference_mlflow"
dag = DAG(
    dag_id=dag_id,
    default_args=args,
    tags=['example'],
	catchup=True, 
	schedule_interval='0 1 * * *', 
	start_date=datetime(2020, 3, 24)
)

mlflow.set_tracking_uri("http://192.168.99.100:5000")
mlflow.set_experiment("demo_ml")

boruta_pipeline = mlflow.sklearn.load_model("runs:/7232bf8e8c314e728b1cb99036024d4d/Pipeline")
scaler = mlflow.sklearn.load_model("runs:/7232bf8e8c314e728b1cb99036024d4d/MinMaxScaler")

output_folder = "/tmp/airflow/output/" + dag_id

def task_download_data(**kwargs):
	content = requests.get('https://archive.org/download/datasets_202003/aps-failure-at-scania-trucks-data-set.zip')
	f = ZipFile(BytesIO(content.content))
	folder = output_folder + "/" + str(kwargs['execution_date'])[0:10] + "/download_data"
	f.extractall(folder)
	
def process_data(**kwargs):
	file = "/tmp/airflow/output/" + dag_id + "/" + str(kwargs['execution_date'])[0:10] + "/download_data/aps_failure_test_set_processed_8bit.csv"
	test_ds =  pd.read_csv(file, na_values='na')
	
	test_features = test_ds.drop('class', axis=1)
	test_features_balanced = test_features
	test_features_balanced = pd.DataFrame(scaler.transform(test_features_balanced), columns=test_features_balanced.columns)
	
	test_features_balanced.to_csv(output_folder + "/" + str(kwargs['execution_date'])[0:10] + "/processed_data.csv", index = False, header=True)

def predict(**kwargs):
	file = output_folder + "/" + str(kwargs['execution_date'])[0:10] + "/processed_data.csv"
	train_features_balanced = pd.read_csv(file)
	
	y_pred = boruta_pipeline.predict_proba(train_features_balanced.values)
	
	file = output_folder + "/" + str(kwargs['execution_date'])[0:10] + "/result.csv"
	pd.DataFrame(y_pred).to_csv(file, index = False, header=True)

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
