from pytest import fixture

import requests

from config import SERVICE_URL


@fixture
def get_total_and_objects_ids():
    response = requests.get(url=SERVICE_URL + "objects")
    return response


@fixture
def get_existing_art_object_by_id():
    return requests.get(url=SERVICE_URL + "objects/1")

@fixture
def get_nonexisting_art_object_by_id():
    return requests.get(url=SERVICE_URL + "objects/0")


def _search_request(param, value):

    return requests.get(url=SERVICE_URL + 'search?' + param + '=' + value)


@fixture
def search_request():
    return _search_request
