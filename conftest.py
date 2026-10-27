# File serves as a centralized repository for shared fixtures, hooks, and configuration settings.
import pytest
import requests

@pytest.fixture
def get_list_images_status_code():
    response = requests.get(url="https://api.nekosapi.com/v5/images")

    return response.status_code

@pytest.fixture
def get_list_images_response_body():
    response = requests.get(url="https://api.nekosapi.com/v5/images")
    data = response.json()

    return data

@pytest.fixture
def get_list_tags_status_code():
    response = requests.get(url="https://api.nekosapi.com/v5/tags")

    return response.status_code

@pytest.fixture
def get_list_tags_response_body():
    response = requests.get(url="https://api.nekosapi.com/v5/tags")
    data = response.json()

    return data

# TODO: Is it possible to make it dynamic?
@pytest.fixture
def get_list_tags_response_body_query_limit_1():
    response = requests.get(url="https://api.nekosapi.com/v5/tags?limit=1")
    data = response.json()

    return data

@pytest.fixture
def get_list_tags_response_body_query_limit_0():
    response = requests.get(url="https://api.nekosapi.com/v5/tags?limit=0")
    data = response.json()

    return data

@pytest.fixture
def get_list_tags_status_code_query_limit_101():
    response = requests.get(url="https://api.nekosapi.com/v5/tags?limit=101")
    return response.status_code

@pytest.fixture
def get_list_tags_response_body_query_limit_101():
    response = requests.get(url="https://api.nekosapi.com/v5/tags?limit=101")
    error_message = response.json()['detail'][0]['msg']

    return error_message

@pytest.fixture
def get_list_tags_status_code_query_limit_minus_1():
    response = requests.get(url="https://api.nekosapi.com/v5/tags?limit=-1")
    return response.status_code

@pytest.fixture
def get_list_tags_response_body_query_limit_minus_1():
    response = requests.get(url="https://api.nekosapi.com/v5/tags?limit=-1")
    error_message = response.json()['detail'][0]['msg']

    return error_message
