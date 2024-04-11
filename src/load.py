from functions import connect_to_redshift
from psycopg2.extras import execute_values

def load_data(df, redshift_url, redshift_database, redshift_user, redshift_pwd, redshift_port):
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
