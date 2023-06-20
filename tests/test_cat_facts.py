from unittest.mock import Mock
from lib.cat_facts import *


def test_calls_api_to_cat_facts():
    requester_mock = Mock(name="requester") # This name is just for readability
    response_mock = Mock(name="response")

    # We tell `requester_mock` to return `response_mock` 
    # when we call `get()` on it.
    requester_mock.get.return_value = response_mock

    # We tell `response_mock` to return a sample output of the API when
    # we call `json()` on it.
    # I got this sample using `curl "https://www.boredapi.com/api/activity"`.
    response_mock.json.return_value = {"fact":"In just 7 years, one un-spayed female cat and one un-neutered male cat and their offspring can result in 420,000 kittens.","length":121}

    cat_facts = CatFacts(requester_mock)
    result = cat_facts.provide()
    assert result == "Cat fact: In just 7 years, one un-spayed female cat and one un-neutered male cat and their offspring can result in 420,000 kittens."