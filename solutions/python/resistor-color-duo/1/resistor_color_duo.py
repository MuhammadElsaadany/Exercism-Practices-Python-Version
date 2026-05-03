def value(colors):
    colors_index = [{"black": 0},
                    {"brown": 1},
                    {"red": 2},
                    {"orange": 3},
                    {"yellow": 4},
                    {"green": 5},
                    {"blue": 6},
                    {"violet": 7},
                    {"grey": 8},
                    {"white": 9}]
    final_resistance = []
    if colors:
        for first_color in colors_index:
            if colors[0] in first_color:
                final_resistance.append(str(first_color[colors[0]]))
        for second_color in colors_index:
            if colors[1] in second_color:
                final_resistance.append(str(second_color[colors[1]]))
        print(final_resistance)
        if final_resistance[0] == "0":
            final_resistance.remove("0")
        return int("".join(final_resistance))