from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG

from src.load.insert import upsert

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 1, 1),
}

with DAG('inserting', default_args=default_args, schedule_interval=timedelta(minutes=5)) as dag:
    upsert_task = PythonOperator(
        task_id='upsert',
        python_callable=upsert
    )

    upsert_task