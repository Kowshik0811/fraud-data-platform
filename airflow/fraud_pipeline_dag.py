from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "data_engineer",
    "start_date": datetime(2024, 1, 1)
}

dag = DAG(
    "fraud_detection_pipeline",
    default_args=default_args,
    schedule_interval="@hourly"
)

start_producer = BashOperator(
    task_id="start_transaction_producer",
    bash_command="python data_producer/kafka_producer.py",
    dag=dag
)

run_spark = BashOperator(
    task_id="run_spark_streaming",
    bash_command="python data_pipeline/spark_streaming.py",
    dag=dag
)

start_producer >> run_spark