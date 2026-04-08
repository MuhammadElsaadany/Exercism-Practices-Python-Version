def square(number):
    if number == 1:
        grains_number = 1
        return grains_number
    if 1 < number <= 64:
        grains_number = 2
        for i in range(2, number):
            grains_number = grains_number * 2
        return grains_number
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total_grains_number = 2
    for i in range(1, 64):
        total_grains_number = total_grains_number * 2
    return total_grains_number - 1
