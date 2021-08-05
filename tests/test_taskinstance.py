import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_task_instances():
    response = requests.get(
        base_url + 'dags/LOAD_NY_COVID_DLY/dagRuns/scheduled__2021-02-10T17:14:06.467941+00:00/taskInstances?limit=100',
        auth=authToken)
    # This also works
    # response = requests.get(
    #     base_url + '/dags/LOAD_NY_COVID_DLY/dagRuns/~/taskInstances',
    #     auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_task_instance_by_taskid():
    response = requests.get(
        base_url + 'dags/LOAD_NY_COVID_DLY/dagRuns/scheduled__2021-02-10T17:14:06.467941+00:00/taskInstances/loaddata',
        auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_task_instance_extra_links():
    response = requests.get(
        base_url + 'dags/LOAD_NY_COVID_DLY/dagRuns/scheduled__2021-02-10T17:14:06.467941+00:00/taskInstances/get_ny_covid_data_by_date/links',
        auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200
