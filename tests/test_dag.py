import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_dag_by_id():
    response = requests.get(base_url + 'dags/LOAD_NY_COVID_DLY', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


# This gives us the complete DAG Code. We can get file_token by calling the get dag by dag id
def test_get_dag_by_file_token():
    response = requests.get(
        base_url + 'dagSources/Ii9vcHQvYWlyZmxvdy9kYWdzL2NvdmlkTnlEYWlseS5weSI.8k71CS4mT3aWzF6M_UHWAVZRm_c'
        , auth=authToken)
    print(response.text)
    assert response.status_code == 200

def test_get_dags():
    response = requests.get(base_url+'dags', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_patch_dag_by_id():
    #Description is read only
    #data = {"is_paused": True, "description": "Updated Description"}
    data = {"is_paused": True}
    response = requests.patch(base_url+'dags/NY_COVID_INITIAL_LD?update_mask=is_paused', auth=authToken, json=data)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

#def test_post_clear_task_instances():
# TODO: Implement this test

def test_get_dag_details():
    response = requests.get(base_url+'dags/LOAD_NY_COVID_DLY/details', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_dag_tasks():
    response = requests.get(base_url+'dags/LOAD_NY_COVID_DLY/tasks', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

def test_get_dag_task_details():
    response = requests.get(base_url + 'dags/LOAD_NY_COVID_DLY/tasks/loaddata', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

# def test_post_update_task_instances_state():
# TODO: Implement this test