def packer(value):
    global attempts
    attempts = 0
    while value >= 1000:
        attempts += 1
        value = value / 1000
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    return value

def resistor_label(colors):
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
    colors_tolerance_index = [{"grey": 0.05},
                              {"violet": 0.1},
                              {"blue": 0.25},
                              {"green": 0.5},
                              {"brown": 1},
                              {"red": 2},
                              {"gold": 5},
                              {"silver": 10}]
    final_resistance = []
    factor = 1
    ohms_family = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    tolerance = None
#---------------- if 1 color: ----------------
    if len(colors) == 1:
        for first_color in colors_index:
            if colors[0] in first_color:
                final_resistance = int(first_color[colors[0]])
                
        value = packer(final_resistance)
            
        return f"{value} {ohms_family[attempts]}"
#---------------- if 2 colors: ----------------
    if len(colors) == 2:
        for first_color in colors_index:
            if colors[0] in first_color:
                final_resistance.append(str(first_color[colors[0]]))
        for second_color in colors_index:
            if colors[1] in second_color:
                final_resistance.append(str(second_color[colors[1]]))
                
        if final_resistance[0] == "0":
            final_resistance.remove("0")
            
        resistancevalue = int("".join(final_resistance))
        
        value = packer(resistancevalue)
            
        return f"{value} {ohms_family[attempts]}"
#---------------- if 3 colors: ----------------
    if len(colors) == 3:
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
            
        resistancevalue = int("".join(final_resistance)) * int(factor)
        
        value = packer(resistancevalue)
            
        return f"{value} {ohms_family[attempts]}"
#---------------- if 4 colors: ----------------
    if len(colors) == 4:
        for first_color in colors_index:
            if colors[0] in first_color:
                final_resistance.append(str(first_color[colors[0]]))
        for second_color in colors_index:
            if colors[1] in second_color:
                final_resistance.append(str(second_color[colors[1]]))
        for third_color in colors_index:
            if colors[2] in third_color and colors[2] != "black":
                factor = 10 ** int(third_color[colors[2]])
        for fourth_color in colors_tolerance_index:
            if colors[3] in fourth_color:
                tolerance = fourth_color[colors[3]]
                
        if final_resistance[0] == "0":
            final_resistance.remove("0")
            
        resistancevalue = int("".join(final_resistance)) * int(factor)
        
        value = packer(resistancevalue)
            
        return f"{value} {ohms_family[attempts]} \u00b1{tolerance}%"
#---------------- if 5 colors: ----------------
    if len(colors) == 5:
        for first_color in colors_index:
            if colors[0] in first_color:
                final_resistance.append(str(first_color[colors[0]]))
        for second_color in colors_index:
            if colors[1] in second_color:
                final_resistance.append(str(second_color[colors[1]]))
        for third_color in colors_index:
            if colors[2] in third_color:
                final_resistance.append(str(third_color[colors[2]]))
        for fourth_color in colors_index:
            if colors[3] in fourth_color and colors[3] != "black":
                factor = 10 ** int(fourth_color[colors[3]])
        for fifth_color in colors_tolerance_index:
            if colors[4] in fifth_color:
                tolerance = fifth_color[colors[4]]
                
        if final_resistance[0] == "0":
            final_resistance.remove("0")
            
        resistancevalue = int("".join(final_resistance)) * int(factor)
        
        value = packer(resistancevalue)
            
        return f"{value} {ohms_family[attempts]} \u00b1{tolerance}%"