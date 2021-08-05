import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_dag_runs():
    response = requests.get(base_url + 'dags/LOAD_NY_COVID_DLY/dagRuns', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


# def test_post_trigger_dag_run():

# def test_delete_dag_run_by_id():

def test_get_dag_run_by_id():
    response = requests.get(base_url + 'dags/LOAD_NY_COVID_DLY/dagRuns/scheduled__2021-02-15T22:53:10.657725+00:00',
                            auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_post_get_dag_runs():
    data = {
        "dag_ids": [
            "LOAD_NY_COVID_DLY"
        ],
        "end_date_gte": "2021-02-14T19:59:23.346Z",
        "end_date_lte": "2021-02-17T19:59:23.346Z",
        "execution_date_gte": "2021-02-14T19:59:23.346Z",
        "execution_date_lte": "2021-02-17T19:59:23.346Z",
        "page_limit": 1,
        "page_offset": 0,
        "start_date_gte": "2021-02-14T19:59:23.346Z",
        "start_date_lte": "2021-02-17T19:59:23.346Z"
    }
    response = requests.post(base_url+'dags/~/dagRuns/list', auth = authToken, json=data)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

