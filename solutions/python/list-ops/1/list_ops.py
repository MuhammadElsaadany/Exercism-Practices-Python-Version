def append(list1, list2):
    semi_mega_list = list1 + list2
    return semi_mega_list


def concat(lists):
    mega_list = []
    for i in lists:
        mega_list += i
    return mega_list


def filter(function, list):
    filtered_list = []
    for i in list:
        if function(i):
            filtered_list += [i]
    return filtered_list



def length(list):
    number = 0
    for i in list:
        number += 1
    return number


def map(function, list):
    mapped_list = []
    for i in list:
        mapped_list.append(function(i))
    return mapped_list


def foldl(function, list, initial):
    modified_list = list.copy()
    if not modified_list:
        return initial
    accumulator = function(initial, modified_list[0])
    modified_list.pop(0)
    while modified_list:
        accumulator = function(accumulator, modified_list[0])
        modified_list.pop(0)
    return accumulator


def foldr(function, list, initial):
    modified_list = list.copy()
    if not modified_list:
        return initial
    accumulator = function(initial, modified_list[-1])
    modified_list.pop(-1)
    while modified_list:
        accumulator = function(accumulator, modified_list[-1])
        modified_list.pop(-1)
    return accumulator


def reverse(list):
    reversed_list = []
    for i in list:
        reversed_list.insert(0, i)
    return reversed_list
