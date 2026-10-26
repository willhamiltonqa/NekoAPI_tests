# https://api.nekosapi.com/v5/docs#tag/Images/operation/list_tags_tags_get
# List Tags:
# Returns a paginated list of tags, ordered by name.
import pytest
import requests

@pytest.mark.smoke
def test_get_list_tags_status_code_success(get_list_tags_status_code):
    assert get_list_tags_status_code == 200


@pytest.mark.smoke
def test_get_list_tags_response_body_is_not_none(get_list_tags_response_body):
    assert get_list_tags_response_body is not None, "Response body is None"

@pytest.mark.smoke
def test_get_list_tags_response_body_length(get_list_tags_response_body):
    assert len(get_list_tags_response_body) == 2, "Response should contain 2 keys"

def test_get_list_tags_response_body_key_items_presence(get_list_tags_response_body):
    assert 'items' in get_list_tags_response_body, "Response body key 'items' is missing"

def test_get_list_tags_response_body_key_items_default_limit(get_list_tags_response_body):
    assert len(get_list_tags_response_body['items']) == 25, \
        "Response body key 'items' should return 25 items by default"

def test_get_list_tags_response_body_key_total_presence(get_list_tags_response_body):
    assert 'total' in get_list_tags_response_body, "Response body key 'total' is missing"


def test_get_list_tags_response_body_key_total_value(get_list_tags_response_body):
    assert get_list_tags_response_body['total'] == 55, "Response body key 'total' should return amount of 55 tags"

def test_get_list_tags_response_body_query_limit_set_1(get_list_tags_response_body_query_limit_1):
    assert len(get_list_tags_response_body_query_limit_1['items']) == 1, \
        "Response body key 'items' should be limited to 1"

def test_get_list_tags_response_body_query_limit_set_0(get_list_tags_response_body_query_limit_0):
    assert len(get_list_tags_response_body_query_limit_0['items']) == 0, \
        "Response body key 'items' should be limited to 0"

@pytest.mark.skip(reason="TBD: Find a way how to place 100 tags")
def test_get_list_tags_response_body_query_limit_set_100(get_list_tags_response_body_query_limit_0):
    assert len(get_list_tags_response_body_query_limit_0['items']) == 100, \
        "Response body key 'items' should be limited to 100"

def test_get_list_tags_status_code_query_limit_set_101(get_list_tags_status_code_query_limit_101):
    assert get_list_tags_status_code_query_limit_101 == 422

def test_get_list_tags_response_body_query_limit_set_101(get_list_tags_response_body_query_limit_101):
    assert get_list_tags_response_body_query_limit_101 == 'Input should be less than or equal to 100', \
        "Response body key 'items' limitation over 100 should return propper error message"

@pytest.mark.skip(reason="BUG #1: Server error 500 is returned when limit is set to -1.")
def test_get_list_tags_status_code_query_limit_set_minus_1(get_list_tags_status_code_query_limit_minus_1):
    assert get_list_tags_status_code_query_limit_minus_1 == 422, \
        "Response body key 'items' limited to -1 should return an error message"

@pytest.mark.skip(reason="BUG #1: Server error 500 is returned when limit is set to -1.")
def test_get_list_tags_response_body_query_limit_set_minus_1(get_list_tags_response_body_query_limit_minus_1):
    assert 'Input should be a valid integer' in get_list_tags_response_body_query_limit_minus_1, \
        "Response body key 'items' limited to -1 should return an error message"
