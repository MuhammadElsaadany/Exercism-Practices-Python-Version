def is_armstrong_number(number):
    validation = []
    for i in str(number):
        validation.append(int(i) ** len(str(number)))
    return sum(validation) == number