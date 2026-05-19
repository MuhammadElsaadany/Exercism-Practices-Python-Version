def flatten(iterable):
    output = []
    validator = 0
    while True:
        for i in iterable:
            if not isinstance(i, list):
                output.append(i)
            else:
                for i in i:
                    output.append(i)
                validator = 0
        iterable = output.copy()
        output.clear()
        for i in iterable:
            if isinstance(i, list):
                validator += 1
        if validator == 0:
            break
    final = [i for i in iterable if isinstance(i, int)]
    return final