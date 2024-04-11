# Weather API

Una aplicación Python para obtener datos meteorológicos de ciudades utilizando la API de AccuWeather. (WIP)

## Instalación

1. Clona este repositorio.
2. Instala las dependencias utilizando pip:
    ```
    pip install -r requirements.txt
    ```

## Uso

1. Configura tus credenciales en el archivo `config.py`.
2. Ejecuta el script `main.py` para cargar los datos climatologicos a la base de datos.

## Docker

1. Ejecutar los siguientes comandos para crear imagen y ejecutar
    ```
    docker build -t <nombre_de_imagen> .
    docker run <nombre_de_imagen>
    ```

## Airflow

1. Configurar variable de entorno creando .env con la siguiente variable (en caso de Windows)
    ```
    AIRFLOW_UID=50000
    ```
2. Ejecutar el comando
    ```
    docker compose up
    ```