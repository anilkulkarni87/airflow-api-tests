import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_post_variable():
    data = {
        "key": "variable_by_api",
        "value": "Temporary"
    }
    response = requests.post(f'{base_url}variables', json=data, auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_variable_by_key():
    variable_key = 'variable_by_api'
    response = requests.get(f'{base_url}variables/{variable_key}', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_patch_variable_by_key():
    variable_key = 'variable_by_api'
    data = {
        "key": "variable_by_api",
        "value": "updatedTemporary"
    }
    response = requests.patch(f'{base_url}variables/{variable_key}?update_mask=value', auth=authToken, json=data)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_all_variables():
    response = requests.get(f'{base_url}variables', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_delete_variable():
    variable_key = 'variable_by_api'
    response = requests.delete(f'{base_url}variables/{variable_key}', auth=authToken)
    print(response.text)
    assert response.status_code == 204
