import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_config():
    response = requests.get(base_url + 'config', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

