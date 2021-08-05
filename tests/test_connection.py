import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_connections():
    response = requests.get(base_url+'connections', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    #print(response.json()['connections'][0]['connection_id'])
    assert response.status_code == 200
    assert response.json()['connections'][0]['connection_id'] == "postgres_new"

#Getting 409 if connection id already exists
def test_post_connection():
    sampleConnectionDict={
        "conn_type": "postgres",
        "connection_id": "postgres_api",
        "host": "airflow",
        "login": "airflow",
        "port": 5433,
        "schema": "userdata",
        "extra": "string",
        "password": "airflow"
    }
    response = requests.post(base_url+'connections',
                             auth=authToken, json=sampleConnectionDict)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

def test_get_connection_id():
    response = requests.get(base_url+'connections/postgres_api', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

#This is how we call a Patch request for a connection ID
def test_patch_connection_id():
    sampleConnectionDict = {
        "conn_type": "postgres",
        "connection_id": "postgres_api",
        "host": "airflow",
        "login": "airflow",
        "port": 5434,
        "schema": "userdata",
        "extra": "extrastring2",
        "password": "airflow"
    }
    response = requests.patch(base_url+'connections/postgres_api?update_mask=extra,port',
                              auth=authToken, json=sampleConnectionDict)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_delete_connection_id():
    response = requests.delete(base_url+'connections/postgres_api',
                               auth=authToken)
    print(response.text)
    assert response.status_code == 204
