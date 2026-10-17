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
