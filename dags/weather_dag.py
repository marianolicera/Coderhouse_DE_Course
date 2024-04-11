from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

default_args={
    'owner' : 'Mariano',
    'retries' : 5,
    'retry_delay' : timedelta(minutes= 2)
},

with DAG(
    'Coderhouse_DE_Course',
    default_args=default_args,
    description = 'Dag para obtener datos del clima en 150 ciudades y subirlas a una BD',
    start_date=datetime(2024, 4, 11, 2), #Se inicia el 11 de abril de 2024 y se ejecuta diariamente,
    schedule_interval = '@daily',
    catchup = False,
    tags = ['Course'],
) as dag:
    task1 = PythonOperator(
    task_id = 'weather_api ejecute',
    python_callable =  main()
    )
