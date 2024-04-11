from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from src.main import etl_main_function

default_args={
    'owner' : 'Mariano',
    'retries' : 5,
    'retry_delay' : timedelta(minutes= 2)
},

with DAG(
    dag_id = 'a_etl_process_weather',
    default_args=default_args,
    description = 'Dag para obtener datos del clima en 150 ciudades y subirlas a una BD',
    start_date=datetime(2024, 4, 11, 2), #Se inicia el 11 de abril de 2024 y se ejecuta diariamente,
    schedule_interval = '@daily',
    catchup = False,
    tags = ['Course'],
) as dag:

    def send_mail_function():
        print('Sending mail with OK status')

    etl_process = PythonOperator(
        task_id = 'weather_api ejecute',
        python_callable =  etl_main_function()
    )
    mail_sending = PythonOperator(
        task_id = 'sending mail with OK status',
        python_callable = send_mail_function()
    )

    etl_process >> mail_sending