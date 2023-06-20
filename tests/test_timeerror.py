
from unittest.mock import Mock
from lib.timeerror import *
import time

def test_calls_api_to_provide_difference_in_time():
    requester_mock = Mock(name="requester") # This name is just for readability
    response_mock = Mock(name="response")

    # We tell `requester_mock` to return `response_mock` 
    # when we call `get()` on it.
    requester_mock.get.return_value = response_mock

    # We tell `response_mock` to return a sample output of the API when
    # we call `json()` on it.
    # I got this sample using `curl "https://www.boredapi.com/api/activity"`.
    response_mock.json.return_value = {"abbreviation":"BST","client_ip":"92.40.218.189","datetime":"2023-06-19T10:28:31.799884+01:00","day_of_week":1,"day_of_year":170,"dst":True,"dst_from":"2023-03-26T01:00:00+00:00","dst_offset":3600,"dst_until":"2023-10-29T01:00:00+00:00","raw_offset":0,"timezone":"Europe/London","unixtime":1687166911,"utc_datetime":"2023-06-19T09:28:31.799884+00:00","utc_offset":"+01:00","week_number":25}

    time_error = TimeError(requester_mock)
    result = time_error.error()
    assert result == 1687166911 - time.time()