def egg_count(display_value):
    binary_value = bin(display_value)[2:]
    eggs_number = 0
    for i in str(binary_value):
        if i == "1":
            eggs_number += 1
    return eggs_number
