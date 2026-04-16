import math

def classify(number):

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    
    numbers_buffer = []
    breaker = 1

    while breaker <= math.floor(number ** 0.5):
        if number % breaker == 0:
            numbers_buffer.append(breaker)
            divisor = number // breaker
            if divisor != number and divisor != breaker:
                numbers_buffer.append(divisor)
        breaker += 1

    numbers_sum = sum(numbers_buffer)

    if numbers_sum == number:
        return "perfect"
    if numbers_sum > number:
        return "abundant"
    if numbers_sum < number:
        return "deficient"