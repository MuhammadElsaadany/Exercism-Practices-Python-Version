def square_of_sum(number):
    #the efficient method:
    return (number*(number+1)//2)**2
    #the not so efficient method:
    # start = 0
    # sum_list = []
    # if isinstance(number, int):
    #     for i in range(number):
    #         start = start + 1
    #         sum_list.append(start)
    #     return sum(sum_list) ** 2


def sum_of_squares(number):
    #the efficient method:
    return number*(number+1)*(2*number+1)//6
    #the not so efficient method:
    # start = 0
    # squares_list = []
    # if isinstance(number, int):
    #     for i in range(number):
    #         start = start + 1
    #         squares_list.append(start ** 2)
    #     return sum(squares_list)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)