import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_pools():
    response = requests.get(base_url + 'pools', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_post_create_pool():
    data = {
        "name": "apitest",
        "slots": 20
    }
    response = requests.post(base_url + 'pools', auth=authToken, json=data)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_pool_by_name():
    response = requests.get(base_url + 'pools/default_pool', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_patch_pool_by_name():
    data = {
        "name": "apitest",
        "slots": 20
    }
    response = requests.patch(base_url + 'pools/apitest?update_mask=slots', auth=authToken, json=data)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

def test_delete_pool():
    response = requests.delete(base_url + 'pools/apitest', auth=authToken)
    print(response.text)
    assert response.status_code == 204