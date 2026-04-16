def classify(number):

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    
    numbers_buffer = []
    breaker = number - 1

    while not breaker == 0:
        if number % breaker == 0:
            numbers_buffer.append(breaker)
            breaker -= 1
        else:
            breaker -= 1

    if sum(numbers_buffer) == number:
        return "perfect"
    if sum(numbers_buffer) > number:
        return "abundant"
    if sum(numbers_buffer) < number:
        return "deficient"