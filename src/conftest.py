# File serves as a centralized repository for shared fixtures, hooks, and configuration settings.
import pytest
import src.utils


@pytest.fixture
def get_list_images_status_code():
    response = src.utils.get_list_images()

    return response.status_code


@pytest.fixture
def get_list_images_response_body():
    response = src.utils.get_list_images()
    data = response.json()

    return data


@pytest.fixture
def get_list_tags_status_code():
    response = src.utils.get_list_tags()

    return response.status_code


@pytest.fixture
def get_list_tags_response_body():
    response = src.utils.get_list_tags()
    data = response.json()

    return data


@pytest.fixture
def get_list_tags_response_body_query_limit_1():
    response = src.utils.get_list_tags_with_limit(1)
    data = response.json()

    return data


@pytest.fixture
def get_list_tags_response_body_query_limit_0():
    response = src.utils.get_list_tags_with_limit(0)
    data = response.json()

    return data


@pytest.fixture
def get_list_tags_status_code_query_limit_101():
    response = src.utils.get_list_tags_with_limit(101)
    return response.status_code


@pytest.fixture
def get_list_tags_response_body_query_limit_101():
    response = src.utils.get_list_tags_with_limit(101)
    error_message = response.json()['detail'][0]['msg']

    return error_message


@pytest.fixture
def get_list_tags_status_code_query_limit_minus_1():
    response = src.utils.get_list_tags_with_limit(-1)
    return response.status_code


@pytest.fixture
def get_list_tags_response_body_query_limit_minus_1():
    response = src.utils.get_list_tags_with_limit(-1)
    error_message = response.json()['detail'][0]['msg']

    return error_message


@pytest.fixture
def get_list_tags_response_body_items_all_tags():
    response = src.utils.get_list_tags_with_limit(56)
    data = response.json()

    return data
