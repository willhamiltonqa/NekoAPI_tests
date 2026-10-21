# https://api.nekosapi.com/v5/docs#tag/Images/operation/list_tags_tags_get
# List Tags:
# Returns a paginated list of tags, ordered by name.

def test_get_list_tags_status_code_success(get_list_tags_status_code):
    assert get_list_tags_status_code == 200

def test_get_list_tags_response_body_is_not_none(get_list_tags_response_body):
    assert get_list_tags_response_body is not None, "Response body is None"

def test_get_list_tags_response_body_length(get_list_tags_response_body):
    assert len(get_list_tags_response_body) == 2, "Response should contain 2 keys"

def test_get_list_tags_response_body_key_items_presence(get_list_tags_response_body):
    assert 'items' in get_list_tags_response_body, "Response body key 'items' is missing"

def test_get_list_tags_response_body_key_items_default_limit(get_list_tags_response_body):
    assert len(
        get_list_tags_response_body['items']) == 26, "Response body key 'items' should return 25 items by default"

def test_get_list_tags_response_body_key_total_presence(get_list_tags_response_body):
    assert 'total' in get_list_tags_response_body, "Response body key 'total' is missing"


def test_get_list_tags_response_body_key_total_value(get_list_tags_response_body):
    assert get_list_tags_response_body['total'] == 55, "Response body key 'total' should return amount of 55 tags"
