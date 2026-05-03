def color_code(color):
    color_index = [{"black": 0},
                    {"brown": 1},
                    {"red": 2},
                    {"orange": 3},
                    {"yellow": 4},
                    {"green": 5},
                    {"blue": 6},
                    {"violet": 7},
                    {"grey": 8},
                    {"white": 9}]
    if color:
        for i in color_index:
            if color in i:
                return i[color]

def colors():
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
