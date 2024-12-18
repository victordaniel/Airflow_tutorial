from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

# Default arguments for tasks
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 1, 1),
}

# Define the DAG
dag = DAG(
    dag_id='example_dag',
    description='A simple DAG example',
    schedule_interval='@daily',  # Runs daily
    default_args=default_args,
    catchup=False,  # Do not backfill missed intervals
    max_active_runs=1,  # Only one active run at a time
    tags=['example']
)

# Define tasks
start = DummyOperator(task_id='start', dag=dag)
task_1 = DummyOperator(task_id='task_1', dag=dag)
task_2 = DummyOperator(task_id='task_2', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Set task dependencies
start >> task_1 >> task_2 >> end
