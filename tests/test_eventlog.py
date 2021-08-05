import json

import requests

from airflowapi import authToken
from airflowapi import base_url


def test_get_event_logs():
    response = requests.get(base_url + 'eventLogs', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200


def test_get_event_log_by_id():
    response = requests.get(base_url + 'eventLogs/77', auth=authToken)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    assert response.status_code == 200
