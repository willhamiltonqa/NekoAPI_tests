def find_tag_in_response_body(tag_id, list_of_tags):
    index = 0
    for item in list_of_tags:
        if tag_id == item['name']:
            return True
        index += 1
    return False
