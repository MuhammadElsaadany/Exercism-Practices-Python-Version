def label(colors):
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
    factor = 1
    if colors:
        for first_color in colors_index:
            if colors[0] in first_color:
                final_resistance.append(str(first_color[colors[0]]))
        for second_color in colors_index:
            if colors[1] in second_color:
                final_resistance.append(str(second_color[colors[1]]))
        for third_color in colors_index:
            if colors[2] in third_color and colors[2] != "black":
                factor = 10 ** int(third_color[colors[2]])
                
        if final_resistance[0] == "0":
            final_resistance.remove("0")
        ohms = int("".join(final_resistance)) * int(factor)
        if 1000 < ohms < 1000000:
            kiloohms = int(ohms / 1000)
            return f"{kiloohms} kiloohms"
        elif 1000000 < ohms < 1000000000:
            megaohms = int(ohms / 1000000)
            return f"{megaohms} megaohms"
        elif 1000000000 < ohms:
            gigaohms = int(ohms / 1000000000)
            return f"{gigaohms} gigaohms"
        else:
            return f"{ohms} ohms"