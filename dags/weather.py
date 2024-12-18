
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 12, 18),
    'retries': 1,
    'catch_up': False  # Moved catch_up to default_args
}

# Define the DAG
with DAG('simple_dag',
         default_args=default_args,
         description='A simple tutorial DAG',
         schedule_interval='@once',  # Run once, immediately after the start_date
         ) as dag:

    # Task 1: Dummy start task
    start_task = DummyOperator(task_id='start')

    # Task 2: Dummy end task
    end_task = DummyOperator(task_id='end')

    # Define the order of task execution
    start_task >> end_task
