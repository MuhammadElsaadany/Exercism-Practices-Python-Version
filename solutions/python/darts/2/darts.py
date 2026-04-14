def score(x, y):
    distance = x ** 2 + y ** 2
    if distance <= 1 ** 2:
        return 10
    if distance <= 5 ** 2:
        return 5
    if distance <= 10 ** 2:
        return 1
    else:
        return 0