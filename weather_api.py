# Import necessary libraries
import requests
import pandas as pd
from datetime import datetime
from config import api_key, redshift_database, redshift_host, redshift_port, redshift_pwd, redshift_user
from functions import connect_to_redshift
from psycopg2.extras import execute_values

#Getting base URL from API Service and API KEY
url = 'http://dataservice.accuweather.com/currentconditions/v1/topcities/150?apikey='
api_key = api_key

# Building full URL with API KEY
full_url = url + api_key

response = requests.get(full_url).json()

# Initialize lists to store the data obtained from the API

countries = []
cities = []
description = []
temperature = []
measure_date = []
datetimes = []

# Iterate over each element of the obtained JSON
for data in response:
    # Extract relevant data
    country_name = data['Country']['LocalizedName']
    city_name = data['LocalizedName']
    weather_text = data['WeatherText']
    temperature_C = data['Temperature']['Metric']['Value']
    timestamp = data['LocalObservationDateTime']
    datetime_insertion = datetime.now()

    # Append data to lists
    countries.append(country_name)
    cities.append(city_name)
    description.append(weather_text)
    temperature.append(temperature_C)
    measure_date.append(timestamp)

    # Create DataFrame
    df = pd.DataFrame({
        "Country Name": countries,
        "City Name": cities,
        "Description":description,
        "Temperature (C)": temperature,
        "Measure date": measure_date,
        "Insertion date": datetime_insertion
    })

# Create RedShift connection
redshift_url = redshift_host
redshift_database = redshift_database
redshift_user = redshift_user
redshift_pwd = redshift_pwd
redshift_port = redshift_port
conn = connect_to_redshift(redshift_url, redshift_database, redshift_user, redshift_pwd, redshift_port)

#Creating table if not exist, adding an auto increment ID
with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS marianolicera3_coderhouse.weather
        (
            id_meansure INT IDENTITY(1,1) PRIMARY KEY,
            country_name VARCHAR(255),
            city_name VARCHAR(255),
            description VARCHAR(50),
            temperature FLOAT,
            date_meansure DATETIME,
            date_insertion DATETIME 
        )
    """)
    conn.commit()

# Insert data into RedShift table
with conn.cursor() as cur:
    execute_values(
        cur,
        '''
        INSERT INTO weather (country_name, city_name, description, temperature, date_meansure, date_insertion)
        VALUES %s
        ''',
        [tuple(row) for row in df.values],
        page_size=len(df)
    )
    conn.commit()

# Closing connections
cur.close()
conn.close()