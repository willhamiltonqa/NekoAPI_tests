def find_tag_in_response_body(tag_id, list_of_tags):
    for item in list_of_tags:
        if tag_id == item['name']:
            return True
    return False
