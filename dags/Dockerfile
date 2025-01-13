FROM apache/airflow:2.3.0

USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev

RUN pip install psycopg2 pandas

RUN mkdir -p /opt/airflow/logs/scheduler && \
    chmod -R 777 /opt/airflow/logs && \
    chown -R airflow:airflow /opt/airflow/logs/scheduler

USER airflow
