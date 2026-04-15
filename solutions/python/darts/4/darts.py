def score(x, y):
    distance_to_center = x ** 2 + y ** 2
    if distance_to_center <= 1 ** 2:
        return 10
    if distance_to_center <= 5 ** 2:
        return 5
    if distance_to_center <= 10 ** 2:
        return 1
    return 0