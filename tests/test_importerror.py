import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_import_errors():
    response = requests.get(base_url + 'importErrors', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200

# def test_get_import_error_by_id():
#     response = requests.get(base_url + 'importErrors/1', auth=authToken)
#     print(json.dumps(response.json(), indent=4, sort_keys=True))
#     assert response.status_code == 200

