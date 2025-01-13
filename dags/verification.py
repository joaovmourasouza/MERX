from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG

from src.load.check import (check_exchange_rate, 
                            check_credit_balance, 
                            check_brazil_indicators)

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 1, 1),
}

with DAG('checking', default_args=default_args, schedule_interval=timedelta(minutes=5)) as dag:
    
    check_exchange_rate_task = PythonOperator(
        task_id='check_exchange_rate',
        python_callable=check_exchange_rate
    )

    check_credit_balance_task = PythonOperator(
        task_id='check_credit_balance',
        python_callable=check_credit_balance
    )

    check_brazil_indicators_task = PythonOperator(
        task_id='check_brazil_indicators',
        python_callable=check_brazil_indicators
    )

    check_exchange_rate_task >> check_credit_balance_task >> check_brazil_indicators_task