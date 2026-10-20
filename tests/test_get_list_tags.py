# https://api.nekosapi.com/v5/docs#tag/Images/operation/list_tags_tags_get
# List Tags:
# Returns a paginated list of tags, ordered by name.

def test_get_list_tags_status_code_success(get_list_tags_status_code):
    assert get_list_tags_status_code == 200

def test_get_list_tags_response_body_is_not_none(get_list_tags_response_body):
    assert get_list_tags_response_body is not None, "Response body is None"