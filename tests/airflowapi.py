from requests.auth import HTTPBasicAuth

base_url = 'http://localhost:8080/api/v1/'
authToken = HTTPBasicAuth('airflow', 'airflow')
