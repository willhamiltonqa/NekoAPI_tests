# https://api.nekosapi.com/v5/docs#tag/Images/operation/list_images_images_get
# List Images:
# Returns a paginated list of images, filtered by the given parameters.
# The results are ordered by creation date, with the most recent images first.

import requests

def test_get_list_images_status_code_success():
    result = requests.get(url="https://api.nekosapi.com/v5/images")

    print()
    assert result.status_code == 200
