def convert(number):
    sound = []
    if number % 3 == 0:
        sound.append("Pling")
    if number % 5 == 0:
        sound.append("Plang")
    if number % 7 == 0:
        sound.append("Plong")
    return "".join(sound) or str(number)
