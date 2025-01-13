from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG

from src.transform.shape import (trasform_exchange_rate, 
                                 transform_credit_balance, 
                                 transform_brazil_indicators)

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 1, 1),
}

with DAG('transform', default_args=default_args, schedule_interval=timedelta(minutes=5)) as dag:
    trasform_exchange_rate_task = PythonOperator(
        task_id='trasform_exchange_rate',
        python_callable=trasform_exchange_rate
    )
    transform_credit_balance_task = PythonOperator(
        task_id='transform_credit_balance',
        python_callable=transform_credit_balance
    )
    transform_brazil_indicators_task = PythonOperator(
        task_id='transform_brazil_indicators',
        python_callable=transform_brazil_indicators
    )

    trasform_exchange_rate_task >> transform_credit_balance_task >> transform_brazil_indicators_task