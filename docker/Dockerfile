# Dockerfile for Airflow DAG

# Choosing lenguage and version
FROM python:3.11

# Creating FileSystem
RUN mkdir /app

# Copying our folder into FS
COPY . /app/

# END OF SETTING

# Declaring our workspace
WORKDIR /app

# Installing all dependencies
RUN pip install -r requirements.txt

# Execute python file
CMD ["python","./main.py"]