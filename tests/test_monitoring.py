import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_instance_status():
    response = requests.get(base_url + 'health', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_version_info():
    response = requests.get(base_url + 'version', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200
