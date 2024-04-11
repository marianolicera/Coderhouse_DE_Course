from extract import extract_data
from transform import transform_data
from load import load_data
from config import api_key, redshift_host, redshift_database, redshift_user, redshift_pwd, redshift_port

def etl_main_function():
    # Data extraction
    data_extracted = extract_data(api_key)

    # Data transformation
    data_transformed = transform_data(data_extracted)

    # Data loading to redshift
    load_data(data_transformed, redshift_host, redshift_database, redshift_user, redshift_pwd, redshift_port)

    print("ETL process successfully completed.")
