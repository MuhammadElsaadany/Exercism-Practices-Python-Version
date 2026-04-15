def is_isogram(string):
    filtered_list = [x for x in str(string).lower() if x.isalpha()]
    return len(filtered_list) == len(set(filtered_list))