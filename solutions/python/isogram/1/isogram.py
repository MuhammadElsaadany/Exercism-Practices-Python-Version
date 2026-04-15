def is_isogram(string):
    filtered_list = [x for x in str(string).lower() if x.isalpha()]
    validator = set(filtered_list)
    return len(filtered_list) == len(validator)