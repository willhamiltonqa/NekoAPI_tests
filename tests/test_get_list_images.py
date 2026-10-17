# https://api.nekosapi.com/v5/docs#tag/Images/operation/list_images_images_get
# List Images:
# Returns a paginated list of images, filtered by the given parameters.
# The results are ordered by creation date, with the most recent images first.

def test_get_list_images_status_code_success(get_list_images_status_code):
    assert get_list_images_status_code == 200

def test_get_list_images_response_data_is_not_none(get_list_images_response_body):
    assert get_list_images_response_body is not None, "Response body is None"