import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_xcom_entries():
    #     Query Used: select * from task_instance ti join dag_run dr on ti.dag_id = dr.dag_id
    #     and ti.execution_date = dr.execution_date
    #     where ti.dag_id ='LOAD_NY_COVID_DLY' order by ti.execution_date ;

    dag_id = 'LOAD_NY_COVID_DLY'
    dag_run_id = 'scheduled__2021-02-19T22:53:10.852790+00:00'
    task_id = 'getTodayDate'
    url = base_url + f'dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries'
    response = requests.get(url=url, auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_xcom_key():
    dag_id = 'LOAD_NY_COVID_DLY'
    dag_run_id = 'scheduled__2021-02-19T22:53:10.852790+00:00'
    task_id = 'getTodayDate'
    xcom_key = 'return_value'
    url = f'{base_url}dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key}'
    print(url)
    response = requests.get(url=url, auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200
