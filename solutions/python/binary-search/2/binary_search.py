def find(search_list, value):
    if not isinstance(search_list, list)  or not value in search_list:
        raise ValueError("value not in array")
    left_index = 0
    right_index = len(search_list) - 1
    middle_index = (left_index + right_index) // 2
    while search_list[middle_index] != value:
        if search_list[middle_index] > value:
            right_index = middle_index - 1
            middle_index = (left_index + right_index) // 2
        if search_list[middle_index] < value:
            left_index = middle_index + 1
            middle_index = (left_index + right_index) // 2
    return middle_index