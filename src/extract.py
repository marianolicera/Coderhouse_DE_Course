import requests
import pandas as pd
from datetime import datetime

def extract_data(api_key):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/topcities/150?apikey=' + api_key
    response = requests.get(url).json()

    countries = []
    cities = []
    description = []
    temperature = []
    measure_date = []

    for data in response:
        country_name = data['Country']['LocalizedName']
        city_name = data['LocalizedName']
        weather_text = data['WeatherText']
        temperature_C = data['Temperature']['Metric']['Value']
        timestamp = data['LocalObservationDateTime']
        datetime_insertion = datetime.now()

        countries.append(country_name)
        cities.append(city_name)
        description.append(weather_text)
        temperature.append(temperature_C)
        measure_date.append(timestamp)

    df = pd.DataFrame({
        "Country Name": countries,
        "City Name": cities,
        "Description": description,
        "Temperature (C)": temperature,
        "Measure date": measure_date,
        "Insertin date": datetime_insertion
    })
    return df
