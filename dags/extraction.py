from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG

from src.extract.api import (get_exchange_rate, 
                             get_credit_balance_cooperatives, 
                             get_credit_balance_with_direct_resources)

from src.extract.scraping import get_brazil_indicators

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 1, 1),
}

with DAG('extract', default_args=default_args, schedule_interval=timedelta(minutes=5)) as dag:
    get_exchange_rate_task = PythonOperator(
        task_id='get_exchange_rate',
        python_callable=get_exchange_rate,
        op_kwargs={'currency': 'USD'}
    )
    get_exchange_rate_task2 = PythonOperator(
        task_id='get_exchange_rate2',
        python_callable=get_exchange_rate,
        op_kwargs={'currency': 'BRL'}
    )
    get_credit_balance_cooperatives_task = PythonOperator(
        task_id='get_credit_balance_cooperatives',
        python_callable=get_credit_balance_cooperatives
    )
    get_credit_balance_with_direct_resources_task = PythonOperator(
        task_id='get_credit_balance_with_direct_resources',
        python_callable=get_credit_balance_with_direct_resources
    )

    get_brazil_indicators_task = PythonOperator(
        task_id='get_brazil_indicators',
        python_callable=get_brazil_indicators
    )

    get_exchange_rate_task >> get_exchange_rate_task2 >> get_credit_balance_cooperatives_task >> get_credit_balance_with_direct_resources_task