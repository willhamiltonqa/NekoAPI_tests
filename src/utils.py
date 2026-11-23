import requests


def find_tag_in_response_body(tag_id, list_of_tags):
    for item in list_of_tags:
        if tag_id == item['name']:
            return True
    return False


def get_list_images():
    response = requests.get(url="https://api.nekosapi.com/v5/images")

    return response


def get_list_tags():
    response = requests.get(url="https://api.nekosapi.com/v5/tags")

    return response


def get_list_tags_with_limit(limit):
    response = requests.get(url=f"https://api.nekosapi.com/v5/tags?limit={limit}")

    return response
