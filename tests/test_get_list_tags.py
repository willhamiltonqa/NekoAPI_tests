# https://api.nekosapi.com/v5/docs#tag/Images/operation/list_tags_tags_get
# List Tags:
# Returns a paginated list of tags, ordered by name.
import pytest


class TestGetListTagsNoQuery:
    @pytest.mark.smoke
    def test_get_list_tags_status_code_success(self, get_list_tags_status_code):
        assert get_list_tags_status_code == 200

    @pytest.mark.smoke
    def test_get_list_tags_response_body_is_not_none(self, get_list_tags_response_body):
        assert get_list_tags_response_body is not None, "Response body is None"

    @pytest.mark.smoke
    def test_get_list_tags_response_body_length(self, get_list_tags_response_body):
        assert len(get_list_tags_response_body) == 2, "Response should contain 2 keys"

    def test_get_list_tags_response_body_key_items_presence(self, get_list_tags_response_body):
        assert 'items' in get_list_tags_response_body, "Response body key 'items' is missing"

    def test_get_list_tags_response_body_key_items_type(self, get_list_tags_response_body):
        assert type(get_list_tags_response_body['items']) is list, "Is not list of items on page."

    def test_get_list_tags_response_body_key_items_default_limit(self, get_list_tags_response_body):
        assert len(get_list_tags_response_body['items']) == 25, \
            "Response body key 'items' should return 25 items by default"

    def test_get_list_tags_response_body_key_total_presence(self, get_list_tags_response_body):
        assert 'total' in get_list_tags_response_body, "Response body key 'total' is missing"

    def test_get_list_tags_response_body_key_total_value(self, get_list_tags_response_body):
        assert get_list_tags_response_body['total'] == 55, "Response body key 'total' should return amount of 55 tags"

class TestGetListTagsQueryLimit:
    def test_get_list_tags_response_body_query_limit_set_1(self, get_list_tags_response_body_query_limit_1):
        assert len(get_list_tags_response_body_query_limit_1['items']) == 1, \
            "Response body key 'items' should be limited to 1"

    @pytest.mark.skip(reason="TBD: Find a way how to place 100 tags")
    def test_get_list_tags_response_body_query_limit_set_100(self, get_list_tags_response_body_query_limit_0):
        assert len(get_list_tags_response_body_query_limit_0['items']) == 100, \
            "Response body key 'items' should be limited to 100"

    def test_get_list_tags_response_body_query_limit_set_0(self, get_list_tags_response_body_query_limit_0):
        assert len(get_list_tags_response_body_query_limit_0['items']) == 0, \
            "Response body key 'items' should be limited to 0"

    def test_get_list_tags_status_code_query_limit_set_101(self, get_list_tags_status_code_query_limit_101):
        assert get_list_tags_status_code_query_limit_101 == 422

    def test_get_list_tags_response_body_query_limit_set_101(self, get_list_tags_response_body_query_limit_101):
        assert get_list_tags_response_body_query_limit_101 == 'Input should be less than or equal to 100', \
            "Response body key 'items' limitation over 100 should return propper error message"

    @pytest.mark.skip(reason="BUG #1: Server error 500 is returned when limit is set to -1.")
    def test_get_list_tags_status_code_query_limit_set_minus_1(self, get_list_tags_status_code_query_limit_minus_1):
        assert get_list_tags_status_code_query_limit_minus_1 == 422, \
            "Response body key 'items' limited to -1 should return an error message"

    @pytest.mark.skip(reason="BUG #1: Server error 500 is returned when limit is set to -1.")
    def test_get_list_tags_response_body_query_limit_set_minus_1(self, get_list_tags_response_body_query_limit_minus_1):
        assert 'Input should be a valid integer' in get_list_tags_response_body_query_limit_minus_1, \
            "Response body key 'items' limited to -1 should return an error message"

class TestGetListTagsResponseBodyItemsContent:
    def test_get_list_tags_response_body_full_items_content(self):
        pass

