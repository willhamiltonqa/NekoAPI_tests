# https://api.nekosapi.com/v5/docs#tag/Images/operation/list_images_images_get
# List Images:
# Returns a paginated list of images, filtered by the given parameters.
# The results are ordered by creation date, with the most recent images first.
import pytest
from utils import find_tag_in_response_body
from data import tags_not_nsfw


@pytest.mark.smoke
def test_get_list_images_status_code_success(get_list_images_status_code):
    assert get_list_images_status_code == 200


@pytest.mark.smoke
def test_get_list_images_response_body_is_not_none(get_list_images_response_body):
    assert get_list_images_response_body is not None, "Response body is None"


@pytest.mark.smoke
def test_get_list_images_response_body_length(get_list_images_response_body):
    assert len(get_list_images_response_body) == 2, "Response body should contain 2 keys"


def test_get_list_images_response_body_key_items(get_list_images_response_body):
    assert 'items' in get_list_images_response_body, "Response body doesn't contain 'items' key"


def test_get_list_images_response_body_key_total(get_list_images_response_body):
    assert 'total' in get_list_images_response_body, "Response body doesn't contain 'total' key"


def test_get_list_images_response_body_value_items_type(get_list_images_response_body):
    assert isinstance(get_list_images_response_body['items'], list), "'items' should be of type list"


def test_get_list_images_response_body_value_total_type(get_list_images_response_body):
    assert isinstance(get_list_images_response_body['total'], int), "'total' should be of type int"


@pytest.mark.parametrize("tag", tags_not_nsfw)
def test_get_list_images_response_body_values_not_nsfw_tags(get_list_tags_response_body_items_all_tags, tag):
    assert find_tag_in_response_body(tag, get_list_tags_response_body_items_all_tags['items']), \
        f"{tag} tag is not present in list of returned items"
