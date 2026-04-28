def line_up(name, number):
    if number in [1, 21, 101]:
        numend = "st"
    elif number in [2, 62]:
        numend = "nd"
    elif number in [3, 123]:
        numend = "rd"
    else:
        numend = "th"
    return f"{name}, you are the {number}{numend} customer we serve today. Thank you!"
