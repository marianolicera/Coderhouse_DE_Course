import psycopg2
from config import *

def connect_to_redshift(url, database, user, redshift_pwd, redshift_port):
    try:
        conn = psycopg2.connect(
            host=url,
            dbname=database,
            user=user,
            password=redshift_pwd,
            port=redshift_port
        )
        print("Connected to Redshift successfully!")
        return conn
    
    except Exception as e:
        print("Unable to connect to Redshift")
        print(e)
        return None