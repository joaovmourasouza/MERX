from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG

from src.transform.optmize import (optimized_exchange_rate,
                                   optimized_credit_balance,
                                   optimized_brazil_indicators)

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 1, 1),
}

with DAG('optmization', default_args=default_args, schedule_interval=timedelta(minutes=5)) as dag:
    optimized_exchange_rate_task = PythonOperator(
        task_id='optimized_exchange_rate',
        python_callable=optimized_exchange_rate
    )
    optimized_credit_balance_task = PythonOperator(
        task_id='optimized_credit_balance',
        python_callable=optimized_credit_balance
    )
    optimized_brazil_indicators_task = PythonOperator(
        task_id='optimized_brazil_indicators',
        python_callable=optimized_brazil_indicators
    )

    optimized_exchange_rate_task >> optimized_credit_balance_task >> optimized_brazil_indicators_task